import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    roc_curve,
    auc,
)

st.set_page_config(page_title="Machine Learning Explorer App", layout="wide")

st.title("Machine Learning Explorer App")
st.write(
    "Upload a CSV file, choose a target column, select a classification model, "
    "adjust hyperparameters, and evaluate model performance."
)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


def detect_id_like_columns(df: pd.DataFrame) -> list[str]:
    id_like = []
    for col in df.columns:
        col_lower = col.lower()
        unique_ratio = df[col].nunique(dropna=True) / max(len(df), 1)
        if "id" in col_lower or unique_ratio > 0.95:
            id_like.append(col)
    return id_like


def safe_read_csv(file) -> pd.DataFrame:
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Could not read the CSV file. Error: {e}")
        st.stop()


if uploaded_file is not None:
    df = safe_read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])
    c3.metric("Missing Values", int(df.isna().sum().sum()))

    st.subheader("Target Selection")
    target = st.selectbox("Select target column", df.columns)

    if target:
        target_unique = df[target].nunique(dropna=True)
        target_dtype = str(df[target].dtype)

        st.write(f"**Selected target:** `{target}`")
        st.write(f"**Target dtype:** {target_dtype}")
        st.write(f"**Unique target values:** {target_unique}")

        st.subheader("Target Distribution")
        target_counts = df[target].astype(str).value_counts(dropna=False)

        chart_left, chart_right = st.columns([1, 1.2])

        with chart_left:
            fig_target, ax_target = plt.subplots(figsize=(5, 3))
            target_counts.plot(kind="bar", ax=ax_target)
            ax_target.set_title("Target Class Distribution")
            ax_target.set_xlabel("Class")
            ax_target.set_ylabel("Count")
            plt.xticks(rotation=30)
            plt.tight_layout()
            st.pyplot(fig_target)

        with chart_right:
            st.markdown("### Target Feedback")
            st.write(
                "This chart shows how the selected target classes are distributed in the uploaded dataset."
            )
            if target_unique < 2:
                st.error("The selected target column must contain at least 2 unique values.")
                st.stop()
            elif target_unique > 20:
                st.warning(
                    "This target has many unique values, so it may not be ideal for classification."
                )
            else:
                st.success(
                    "This target looks appropriate for a classification task."
                )

        X = df.drop(columns=[target]).copy()
        y = df[target].copy()

        valid_rows = ~y.isna()
        X = X.loc[valid_rows].copy()
        y = y.loc[valid_rows].copy()

        id_like_cols = detect_id_like_columns(X)
        if id_like_cols:
            st.info(
                "The app detected and removed likely identifier columns from the features: "
                + ", ".join(id_like_cols)
            )
            X = X.drop(columns=id_like_cols, errors="ignore")

        if X.shape[1] == 0:
            st.error("No usable feature columns remain after removing the target and ID-like columns.")
            st.stop()

        numeric_cols = X.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = [col for col in X.columns if col not in numeric_cols]

        for col in numeric_cols:
            X[col] = X[col].fillna(X[col].median())

        for col in categorical_cols:
            X[col] = X[col].fillna("Missing")

        X = pd.get_dummies(X, drop_first=False)

        label_encoder = None
        if not pd.api.types.is_numeric_dtype(y):
            label_encoder = LabelEncoder()
            y_encoded = label_encoder.fit_transform(y.astype(str))
            class_names = list(label_encoder.classes_)
        else:
            y_encoded = y.values
            class_names = sorted(pd.Series(y).dropna().unique().tolist())

        st.subheader("Model Settings")
        left, right = st.columns(2)

        with left:
            test_size = st.slider("Test size", 0.1, 0.5, 0.2, 0.05)
            model_name = st.selectbox(
                "Choose model",
                ["Logistic Regression", "Decision Tree Classifier"]
            )

        with right:
            random_state = st.number_input("Random state", min_value=0, max_value=9999, value=42, step=1)

        model = None
        hyperparameter_notes = ""
        model_description = ""

        if model_name == "Logistic Regression":
            st.markdown("### Logistic Regression Hyperparameters")
            c_value = st.slider("Regularization Strength (C)", 0.01, 10.0, 1.0, 0.01)
            max_iter = st.slider("Max Iterations", 100, 2000, 1000, 100)

            model = LogisticRegression(
                C=c_value,
                max_iter=max_iter,
                random_state=int(random_state)
            )

            model_description = (
                "Logistic Regression is a linear classification model. It works best when class boundaries "
                "can be separated using linear relationships between variables."
            )

            hyperparameter_notes = (
                f"- **C = {c_value:.2f}**: Controls regularization strength. Lower values apply stronger regularization.\n"
                f"- **Max Iterations = {max_iter}**: Controls how long the algorithm is allowed to train."
            )

        elif model_name == "Decision Tree Classifier":
            st.markdown("### Decision Tree Hyperparameters")
            max_depth = st.slider("Max Depth", 1, 20, 5, 1)
            min_samples_split = st.slider("Min Samples Split", 2, 20, 2, 1)

            model = DecisionTreeClassifier(
                max_depth=max_depth,
                min_samples_split=min_samples_split,
                random_state=int(random_state)
            )

            model_description = (
                "Decision Trees split the data into branches based on feature values. "
                "They are useful for capturing nonlinear patterns and are often easier to interpret."
            )

            hyperparameter_notes = (
                f"- **Max Depth = {max_depth}**: Limits how deep the tree can grow. Smaller values may reduce overfitting.\n"
                f"- **Min Samples Split = {min_samples_split}**: Minimum number of samples required before a node can be split."
            )

        st.info(model_description)

        st.subheader("Train and Evaluate")
        train_button = st.button("Train Model")

        if train_button:
            try:
                X_train, X_test, y_train, y_test = train_test_split(
                    X,
                    y_encoded,
                    test_size=test_size,
                    random_state=int(random_state),
                    stratify=y_encoded if len(np.unique(y_encoded)) > 1 else None
                )

                model.fit(X_train, y_train)
                y_pred = model.predict(X_test)

                acc = accuracy_score(y_test, y_pred)
                prec = precision_score(y_test, y_pred, average="weighted", zero_division=0)
                rec = recall_score(y_test, y_pred, average="weighted", zero_division=0)
                f1 = f1_score(y_test, y_pred, average="weighted", zero_division=0)

                st.subheader("Model Performance")
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Accuracy", f"{acc:.2f}")
                m2.metric("Precision", f"{prec:.2f}")
                m3.metric("Recall", f"{rec:.2f}")
                m4.metric("F1 Score", f"{f1:.2f}")

                left_results, right_results = st.columns([1, 1])

                with left_results:
                    st.subheader("Confusion Matrix")
                    fig_cm, ax_cm = plt.subplots(figsize=(4.8, 4))
                    cm = confusion_matrix(y_test, y_pred)
                    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
                    disp.plot(ax=ax_cm, colorbar=False)
                    plt.xticks(rotation=30)
                    plt.tight_layout()
                    st.pyplot(fig_cm)

                    unique_classes = np.unique(y_encoded)
                    if len(unique_classes) == 2 and hasattr(model, "predict_proba"):
                        st.subheader("ROC Curve")
                        y_prob = model.predict_proba(X_test)[:, 1]
                        fpr, tpr, _ = roc_curve(y_test, y_prob)
                        roc_auc = auc(fpr, tpr)

                        fig_roc, ax_roc = plt.subplots(figsize=(4.8, 4))
                        ax_roc.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
                        ax_roc.plot([0, 1], [0, 1], linestyle="--")
                        ax_roc.set_xlabel("False Positive Rate")
                        ax_roc.set_ylabel("True Positive Rate")
                        ax_roc.set_title("ROC Curve")
                        ax_roc.legend()
                        plt.tight_layout()
                        st.pyplot(fig_roc)

                with right_results:
                    st.subheader("Model Feedback")
                    st.markdown(f"**Selected model:** {model_name}")
                    st.markdown(f"**Target column:** {target}")

                    st.markdown("**What this model does:**")
                    st.write(model_description)

                    st.markdown("**Hyperparameter summary:**")
                    st.markdown(hyperparameter_notes)

                    st.markdown("**What the metrics mean:**")
                    st.markdown(
                        "- **Accuracy**: overall percentage of correct predictions.\n"
                        "- **Precision**: how often predicted classes are correct.\n"
                        "- **Recall**: how well the model finds the true class labels.\n"
                        "- **F1 Score**: a balance between precision and recall."
                    )

                    st.markdown("**Performance guide:**")
                    st.markdown(
                        "- **High performance:** Accuracy ≥ 0.80\n"
                        "- **Moderate performance:** Accuracy between 0.60 and 0.79\n"
                        "- **Low performance:** Accuracy < 0.60\n\n"
                        "*These ranges are general guidelines and should be interpreted in the context of the uploaded dataset.*"
                    )

                    st.markdown("**Performance summary:**")
                    if acc >= 0.80:
                        st.success(
                            "The model is performing strongly on this dataset. The selected features seem useful for predicting the target."
                        )
                    elif acc >= 0.60:
                        st.info(
                            "The model shows moderate performance. It captures some useful patterns, but results could likely improve with different settings or features."
                        )
                    else:
                        st.warning(
                            "The model shows relatively low performance on this dataset. This may mean the selected features are not strongly related to the target, or that a different model/hyperparameter setting may work better."
                        )

                    st.markdown("**Confusion matrix interpretation:**")
                    st.write(
                        "The confusion matrix shows where the model makes correct predictions and where it confuses one class with another. "
                        "A stronger model would show more values concentrated on the diagonal."
                    )

                st.subheader("Overall Interpretation")
                st.write(
                    f"This run used **{model_name}** to predict **{target}** from the uploaded dataset. "
                    "The results above demonstrate how model choice, preprocessing, and hyperparameter settings "
                    "can affect classification performance."
                )

                st.success("Model training complete!")

            except Exception as e:
                st.error(f"An error occurred during training or evaluation: {e}")

else:
    st.info("Upload a CSV file to begin.")