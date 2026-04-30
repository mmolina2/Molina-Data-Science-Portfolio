# Unsupervised Machine Learning Explorer App

## Overview

This project demonstrates how to build an interactive unsupervised machine learning application using Python and Streamlit. The app allows users to upload their own dataset, select numeric features, and explore different unsupervised learning techniques.

The goal of this project is to create a flexible tool that works with different datasets while helping users understand how clustering and dimensionality reduction behave under different settings.

## App Features

The application includes the following functions:

- Upload a CSV dataset  
- Automatically preprocess data:
  - Select numeric columns  
  - Remove missing values  
  - Scale data for modeling  
- Choose between unsupervised methods:
  - K-Means Clustering  
  - Hierarchical Clustering  
  - Principal Component Analysis (PCA)  
- Adjust model parameters interactively  
- Visualize clustering results  
- View performance metrics and interpretation  

## Model Workflow

### 1. Data Preprocessing

- Selected only numeric columns since clustering and PCA require numeric data  
- Removed missing values to avoid errors during modeling  
- Scaled the data using StandardScaler so features are on the same scale  

### 2. Model Selection

The app allows users to explore three unsupervised learning methods:

- K-Means Clustering  
- Hierarchical Clustering  
- Principal Component Analysis (PCA)  

### 3. Parameter Tuning

#### K-Means
- Adjusted number of clusters (k)

#### Hierarchical Clustering
- Adjusted number of clusters  
- Selected linkage method (ward, complete, average, single)

#### PCA
- Adjusted number of principal components  

### 4. Model Evaluation

The app provides feedback using:

- Silhouette Score (for clustering models)  
- Elbow Plot (for K-Means)  
- Dendrogram (for hierarchical clustering)  
- Explained Variance (for PCA)  
- Scatterplots for visual interpretation  

## Performance Interpretation

To help interpret results, the app provides a simple guide:

### Silhouette Score
- High (≥ 0.50): clusters are well separated  
- Moderate (0.25 – 0.49): some overlap between clusters  
- Low (< 0.25): weak clustering structure  

### PCA Variance Explained
- High (≥ 80%): most of the data variation is preserved  
- Moderate (50% – 79%): some information is lost  
- Low (< 50%): significant information is lost  

The app also provides dynamic feedback explaining what these values mean in context.

## How to Run This Project

Clone this repository:  
https://github.com/mmolina2/Molina-Data-Science-Portfolio

Navigate to the project folder:  
MLUnsupervisedApp

Install required libraries:

pip install -r requirements.txt

Run the app:

streamlit run app.py

## Example Output

### App Interface  
<img width="502" height="260" alt="Screenshot 2026-04-29 at 9 58 54 PM" src="https://github.com/user-attachments/assets/f74ba9f1-73db-4010-b2a0-5d55ca1ac2ea" />

### K-Means Clustering  
<img width="340" height="474" alt="Screenshot 2026-04-29 at 10 01 39 PM" src="https://github.com/user-attachments/assets/78f19dbe-dd4f-487b-a66e-f1c9565fd5bc" />

### Hierarchical Clustering  
<img width="370" height="474" alt="Screenshot 2026-04-29 at 10 01 59 PM" src="https://github.com/user-attachments/assets/c6c3b018-482e-4f34-97c7-4f28913a0cf3" />

### PCA Visualization  
<img width="460" height="410" alt="Screenshot 2026-04-29 at 10 02 19 PM" src="https://github.com/user-attachments/assets/33d15f5c-0492-4877-85f1-f2f365a96fbb" />

## Concepts Behind the App

This project is based on core ideas from machine learning, especially unsupervised learning.

Unsupervised learning works with data that does not have labels, meaning there is no predefined outcome to predict. Instead, the goal is to explore the data and uncover patterns or structure. :contentReference[oaicite:0]{index=0}  

Two key techniques used in this app are:

### Clustering
Clustering groups similar data points together based on their features. Even without labels, the algorithm can identify patterns and separate the data into meaningful groups. For example, points that are close together in a graph are likely part of the same cluster. :contentReference[oaicite:1]{index=1}  

### Dimensionality Reduction (PCA)
Dimensionality reduction simplifies complex datasets by reducing the number of features while keeping the most important information. This makes the data easier to visualize and analyze, especially when working with many variables. :contentReference[oaicite:2]{index=2}  

These concepts allow the app to help users explore datasets and discover patterns without needing labeled data.

## Key Takeaways

- Unsupervised learning does not require labeled data  
- Clustering results depend heavily on the dataset and selected features  
- Choosing the number of clusters can significantly impact results  
- PCA helps reduce dimensionality while preserving important patterns  
- Visualizations make it easier to understand patterns in high-dimensional data  

## Tools Used

- Python  
- Streamlit  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- SciPy  

## References

Scikit-learn Documentation: https://scikit-learn.org/  
Streamlit Documentation: https://docs.streamlit.io/  
Course Text:
Grokking Machine Learning by Luis Serrano (Chapter 2: Types of Machine Learning), and other course materials and lectures  
