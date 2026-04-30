import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage, dendrogram


# Basic page setup
st.set_page_config(page_title="Unsupervised ML Explorer", layout="wide")

st.title("Unsupervised Machine Learning Explorer")
st.write(
    "Upload a CSV file and explore unsupervised machine learning methods: "
    "K-Means clustering, hierarchical clustering, and PCA."
)

# Upload section
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


def load_data(file):
    # Reads the uploaded CSV file into a pandas dataframe.
    return pd.read_csv(file)


def clean_numeric_data(data):
    # Clustering and PCA need numeric data, so I keep only number columns.
    numeric_data = data.select_dtypes(include=np.number)

    # I drop missing rows here so the models can run without errors.
    clean_data = numeric_data.dropna()

    return clean_data


def explain_silhouette(score):
    # I use this to give the user a simple interpretation of the silhouette score.
    # The score ranges from -1 to 1, and higher values usually mean better clusters.
    if score >= 0.50:
        st.success(
            "The clusters look fairly well separated. This means the model is finding "
            "groups that are more distinct from each other."
        )
    elif score >= 0.25:
        st.warning(
            "The clusters show some separation, but they may overlap. Changing the number "
            "of clusters or choosing different columns might improve the result."
        )
    else:
        st.warning(
            "The clusters do not look very well separated. This dataset or set of columns "
            "may not have strong natural groups."
        )

    st.write("**Silhouette score guide:**")
    st.write("- Closer to **1** means clusters are more clearly separated.")
    st.write("- Around **0** means clusters are overlapping.")
    st.write("- Below **0** can mean points may be assigned to the wrong cluster.")


def explain_pca_variance(total_variance):
    # This gives a short explanation of how much information PCA kept.
    if total_variance >= 0.80:
        st.success(
            "These components explain a large amount of the variation in the data. "
            "This means PCA is summarizing the dataset well with fewer dimensions."
        )
    elif total_variance >= 0.50:
        st.info(
            "These components explain a moderate amount of the variation in the data. "
            "The PCA plot may show some patterns, but it does not capture everything."
        )
    else:
        st.warning(
            "These components explain a smaller amount of the variation in the data. "
            "Using more components may give a better summary."
        )

    st.write("**Variance explained guide:**")
    st.write("- Higher percentages mean PCA kept more information from the original columns.")
    st.write("- Lower percentages mean more information was lost when reducing dimensions.")
    st.write("- PCA is useful when many columns need to be summarized into fewer components.")


if uploaded_file is not None:
    # Load the uploaded file
    df = load_data(uploaded_file)

    # Show the user what the dataset looks like before modeling
    st.subheader("Dataset Preview")
    st.write(f"Rows: {df.shape[0]:,} | Columns: {df.shape[1]:,}")
    st.caption("Preview of the dataset (first 10 rows)")
    st.dataframe(df.head(10), height=250)

    # Clean the dataset for unsupervised learning
    numeric_df = clean_numeric_data(df)

    st.subheader("Data Used for Modeling")
    st.write(
        f"The app found **{numeric_df.shape[1]} numeric columns** and "
        f"kept **{numeric_df.shape[0]:,} rows** after removing missing values."
    )

    # Basic checks so the app does not crash with a dataset that cannot be modeled
    if numeric_df.shape[1] < 2:
        st.error("This dataset needs at least two numeric columns for these methods.")
        st.stop()

    if numeric_df.shape[0] < 5:
        st.error("This dataset needs more rows after cleaning.")
        st.stop()

    # Let the user choose which numeric columns they want to use
    selected_columns = st.multiselect(
        "Choose numeric columns to use",
        options=numeric_df.columns.tolist(),
        default=numeric_df.columns.tolist()[: min(5, numeric_df.shape[1])]
    )

    if len(selected_columns) < 2:
        st.warning("Please select at least two numeric columns.")
        st.stop()

    model_data = numeric_df[selected_columns]

    # Scaling is important because columns can be on very different scales.
    # For example, income and age would not have the same size numbers.
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(model_data)

    st.info(
        "The selected numeric columns were scaled before modeling so that one large-scale "
        "column does not dominate the results."
    )

    # Tabs keep the app organized by method
    tab1, tab2, tab3 = st.tabs(["K-Means Clustering", "Hierarchical Clustering", "PCA"])

    with tab1:
        st.header("K-Means Clustering")
        st.write(
            "K-Means groups rows into clusters by trying to place similar observations "
            "close together."
        )

        # User controls the number of clusters
        k = st.slider("Number of clusters (k)", 2, 10, 3)

        # Fit the K-Means model
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        clusters = kmeans.fit_predict(X_scaled)

        # Silhouette score gives a basic way to judge how separated clusters are
        score = silhouette_score(X_scaled, clusters)

        st.subheader("K-Means Results")
        st.metric("Silhouette Score", round(score, 3))
        explain_silhouette(score)

        # PCA is used here only to make the clusters visible in a 2D plot
        pca_for_plot = PCA(n_components=2)
        points_2d = pca_for_plot.fit_transform(X_scaled)

        fig, ax = plt.subplots(figsize=(4, 3))
        ax.scatter(points_2d[:, 0], points_2d[:, 1], c=clusters)
        ax.set_title("K-Means Clusters")
        ax.set_xlabel("PCA Component 1")
        ax.set_ylabel("PCA Component 2")
        plt.tight_layout()
        st.pyplot(fig, use_container_width=False)

        st.write(
            "This scatterplot uses PCA to reduce the data to two dimensions so the "
            "clusters can be visualized. Each color represents a cluster created by K-Means."
        )

        # Elbow plot tests different k values and compares inertia
        st.subheader("Elbow Plot")

        max_k = min(10, len(model_data))
        inertias = []

        for i in range(1, max_k + 1):
            temp_model = KMeans(n_clusters=i, random_state=42, n_init=10)
            temp_model.fit(X_scaled)
            inertias.append(temp_model.inertia_)

        fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.plot(range(1, max_k + 1), inertias, marker="o")
        ax2.set_title("Elbow Plot")
        ax2.set_xlabel("Number of Clusters")
        ax2.set_ylabel("Inertia")
        plt.tight_layout()
        st.pyplot(fig2, use_container_width=False)

        st.write(
            "The elbow plot helps estimate a reasonable number of clusters. A bend in the "
            "line can suggest a good value for k. Inertia usually goes down as k increases, "
            "so I look for where the improvement starts to slow down."
        )

    with tab2:
        st.header("Hierarchical Clustering")
        st.write(
            "Hierarchical clustering builds clusters step by step and shows how observations "
            "are connected using a dendrogram."
        )

        # User controls the cluster count and linkage method
        cluster_count = st.slider("Number of clusters", 2, 10, 3, key="hier_clusters")
        linkage_method = st.selectbox(
            "Linkage method",
            ["ward", "complete", "average", "single"]
        )

        # Fit the hierarchical clustering model
        hier_model = AgglomerativeClustering(
            n_clusters=cluster_count,
            linkage=linkage_method
        )

        hier_clusters = hier_model.fit_predict(X_scaled)
        hier_score = silhouette_score(X_scaled, hier_clusters)

        st.subheader("Hierarchical Clustering Results")
        st.metric("Silhouette Score", round(hier_score, 3))
        explain_silhouette(hier_score)

        # Again, PCA is only used here to help show clusters in 2D
        pca_for_hier = PCA(n_components=2)
        hier_2d = pca_for_hier.fit_transform(X_scaled)

        fig3, ax3 = plt.subplots(figsize=(4, 3))
        ax3.scatter(hier_2d[:, 0], hier_2d[:, 1], c=hier_clusters)
        ax3.set_title("Hierarchical Clusters")
        ax3.set_xlabel("PCA Component 1")
        ax3.set_ylabel("PCA Component 2")
        plt.tight_layout()
        st.pyplot(fig3, use_container_width=False)

        st.write(
            "This scatterplot shows the hierarchical clustering results in two dimensions. "
            "The colors show the cluster labels assigned by the model."
        )

        # Dendrogram shows the cluster building process
        st.subheader("Dendrogram")

        # Large dendrograms are hard to read, so I use a sample if the dataset is big.
        sample_size = min(75, len(model_data))
        sample_data = X_scaled[:sample_size]

        linked = linkage(sample_data, method=linkage_method)

        fig4, ax4 = plt.subplots(figsize=(5, 3))
        dendrogram(linked, ax=ax4)
        ax4.set_title("Hierarchical Clustering Dendrogram")
        ax4.set_xlabel("Sample Index")
        ax4.set_ylabel("Distance")
        plt.tight_layout()
        st.pyplot(fig4, use_container_width=False)

        st.write(
            "The dendrogram shows how rows are merged into clusters. Shorter distances "
            "mean observations are more similar. Larger jumps in distance can suggest "
            "places where the data naturally separates into groups."
        )

    with tab3:
        st.header("Principal Component Analysis (PCA)")
        st.write(
            "PCA reduces many numeric columns into fewer components while trying to keep "
            "as much information as possible."
        )

        # User chooses how many principal components to calculate
        max_components = min(len(selected_columns), 10)
        n_components = st.slider("Number of PCA components", 2, max_components, 2)

        # Fit PCA on the scaled data
        pca = PCA(n_components=n_components)
        pca_result = pca.fit_transform(X_scaled)

        explained_variance = pca.explained_variance_ratio_
        total_variance = explained_variance.sum()

        st.subheader("PCA Results")
        st.metric("Variance Explained", f"{total_variance:.2%}")
        explain_pca_variance(total_variance)

        # Bar chart shows how much each component explains
        fig5, ax5 = plt.subplots(figsize=(4, 3))
        ax5.bar([f"PC{i+1}" for i in range(n_components)], explained_variance)
        ax5.set_title("Explained Variance by Component")
        ax5.set_xlabel("Principal Component")
        ax5.set_ylabel("Explained Variance Ratio")
        plt.tight_layout()
        st.pyplot(fig5, use_container_width=False)

        st.write(
            "This chart shows how much variation each principal component explains. "
            "The first component usually explains the largest share."
        )

        # Scatterplot uses the first two principal components
        fig6, ax6 = plt.subplots(figsize=(4, 3))
        ax6.scatter(pca_result[:, 0], pca_result[:, 1])
        ax6.set_title("PCA Scatterplot")
        ax6.set_xlabel("Principal Component 1")
        ax6.set_ylabel("Principal Component 2")
        plt.tight_layout()
        st.pyplot(fig6, use_container_width=False)

        st.write(
            "The PCA scatterplot shows the dataset in two dimensions. If points form groups, "
            "that may suggest patterns worth exploring further. PCA does not create clusters "
            "by itself, but it helps make high-dimensional data easier to visualize."
        )

else:
    st.info("Upload a CSV file to begin.")
