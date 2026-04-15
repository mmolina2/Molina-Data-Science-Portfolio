# Machine Learning Explorer App

## Overview

This project demonstrates how to build an interactive machine learning application using Python and Streamlit. The app allows users to upload their own dataset, select a target variable, choose a classification model, adjust hyperparameters, and evaluate model performance.

The goal of this project is to create a flexible tool that can work with different datasets, helping users understand how machine learning models behave under different conditions and settings.

---

## App Features

The application includes the following functionality:

* Upload a CSV dataset
* Select any column as the target variable
* Automatically preprocess data:

  * Handle missing values
  * Encode categorical variables
  * Remove identifier-like columns
* Choose between models:

  * Logistic Regression
  * Decision Tree Classifier
* Adjust hyperparameters interactively
* Train and evaluate models
* View performance metrics and visualizations

---

## Model Workflow

### 1. Data Preprocessing

* Removed missing values from the target column
* Filled missing values in numeric columns using the median
* Filled missing values in categorical columns with "Missing"
* Converted categorical variables using one-hot encoding
* Automatically removed identifier columns (e.g., IDs)

---

### 2. Model Selection

The app allows users to choose between two supervised learning models:

* Logistic Regression
* Decision Tree Classifier

---

### 3. Hyperparameter Tuning

#### Logistic Regression

* Adjusted regularization strength (`C`)
* Controlled number of iterations (`max_iter`)

#### Decision Tree

* Adjusted tree depth (`max_depth`)
* Controlled splitting criteria (`min_samples_split`)

---

### 4. Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC Curve (for binary classification)

---

## Visualizations

* Bar chart showing target class distribution
* Confusion matrix showing prediction performance
* ROC curve for binary classification problems

---

## Performance Interpretation

To help interpret results, the app provides a performance guide:

* **High performance:** Accuracy ≥ 0.80
* **Moderate performance:** Accuracy between 0.60 and 0.79
* **Low performance:** Accuracy < 0.60

The app also provides dynamic feedback explaining model performance based on these ranges.

---

## How to Run This Project

1. Clone this repository:
   https://github.com/mmolina2/Molina-Data-Science-Portfolio

2. Navigate to the project folder:
   MLStreamlitApp

3. Install required libraries:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

---

## Example Output

### App Interface

---

## Key Takeaways

* Model performance depends heavily on the dataset and feature relationships
* Different models perform differently on the same data
* Hyperparameter tuning can improve or degrade performance
* Visualizations help interpret model strengths and weaknesses

---

## Tools Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Matplotlib

---

## References

* Scikit-learn Documentation: https://scikit-learn.org/
* Streamlit Documentation: https://docs.streamlit.io/
* Course materials and lectures
