# Molina – Data Science Portfolio

## Overview
This repository serves as my **semester-long data science portfolio** for the *Introduction to Data Science* course. It documents my progress throughout the semester, following the data science pipeline from data cleaning and exploratory data analysis to visualization, modeling, and interactive applications.

Each project emphasizes not only technical methods, but also how data can be used to answer real-world questions and support informed decision-making.

## At a Glance

- **Unsupervised Machine Learning App** – Interactive clustering and PCA tool using Streamlit  
- **Machine Learning Explorer App** – Supervised learning with model selection and evaluation  
- **Spotify Tracks Explorer** – Interactive data filtering and visualization app  
- **Tidy Data Project** – Data cleaning and transformation using pandas  

## Purpose
The purpose of this repository is to organize and showcase my data science work as it develops over time. Projects emphasize working with real datasets, preparing data for analysis, and communicating insights clearly through code, visualizations, and interactive tools.

📌 This portfolio will be updated regularly as new topics are introduced throughout the course.

## Current Projects

### Unsupervised Machine Learning Explorer App  
[View Project](./MLUnsupervisedApp)

This project extends my portfolio by applying unsupervised machine learning techniques through an interactive Streamlit application. The app allows users to upload their own dataset, select numeric features, and explore clustering and dimensionality reduction methods in real time.  

Users can experiment with K-Means clustering, hierarchical clustering, and principal component analysis (PCA), adjusting parameters such as the number of clusters or components to observe how results change. The app provides visual outputs including cluster scatter plots, dendrograms, and explained variance charts.  

To support interpretation, the app includes performance metrics such as silhouette scores and dynamic feedback that explains the quality of clustering results (e.g., strong separation vs. overlapping clusters). This helps connect technical outputs to meaningful insights.  

This project demonstrates my ability to build interactive data science tools, apply unsupervised learning techniques, tune model parameters, and communicate results clearly through visualization and user-focused design. It also builds on earlier projects by introducing model exploration without labeled data and deploying a fully functional web app.

<img width="500" height="280" alt="Screenshot 2026-04-29 at 10 40 55 PM" src="https://github.com/user-attachments/assets/769ebbdb-4ec6-47d9-9899-cb61bee596f2" />


### Machine Learning Explorer App
[View Project](./MLStreamlitApp)

An interactive Streamlit application that allows users to explore machine learning workflows using their own datasets. Users can upload a CSV file, select a target variable, choose a classification model, adjust hyperparameters, and evaluate model performance in real time.

The app currently supports Logistic Regression and Decision Tree Classification. It includes preprocessing steps such as handling missing values, encoding categorical variables, and removing identifier-like columns. Users can view evaluation metrics including accuracy, precision, recall, and F1 score, along with a confusion matrix for deeper insight into model predictions.

A key feature of this app is dynamic performance feedback, which categorizes model results as high, moderate, or low performance based on accuracy thresholds. This helps users better understand model effectiveness and potential limitations.

This project demonstrates my ability to build interactive machine learning tools, apply preprocessing techniques, tune models, and communicate results clearly through both metrics and visualizations.

<img width="500" height="250" alt="Screenshot 2026-04-14 at 11 58 32 PM" src="https://github.com/user-attachments/assets/5872ecc0-7343-449c-bd94-20265baa85f6" />


### Streamlit Data App (Spotify Tracks Explorer)
[View Project](./Streamlitapp-Project)

An interactive Streamlit application that allows users to explore and filter a Spotify tracks dataset. Users can filter songs by genre, popularity, tempo (BPM), and search for specific artists or tracks, as well as sort and analyze the data dynamically.

This project demonstrates my ability to build simple, interactive data applications, implement user-driven filtering, and work with real-world music data using Python, pandas, and Streamlit.

<img width="500" height="260" alt="Screenshot 2026-03-19 at 4 31 00 PM" src="https://github.com/user-attachments/assets/4f617853-7610-4136-ae5a-9d5da111bd33" />


### Tidy Data Project
[View Project](./TidyData-Project)

This project focuses on transforming an untidy Olympic medal dataset into a clean, structured (tidy) format using Python and pandas. The goal was to prepare the data for analysis by organizing variables into clear columns, making it easier to explore patterns and relationships. Through this project, I practiced key data cleaning techniques such as reshaping data, handling missing values, separating combined variables, and creating visualizations from the cleaned dataset. After cleaning the data, I used a pivot table and multiple charts to analyze medal distributions and identify which sports appeared most frequently.

This project complements my portfolio by demonstrating foundational data science skills, including data wrangling, exploratory data analysis, and data visualization. It builds on my ability to work with real-world datasets and prepares me for more advanced analysis and modeling later on.

<img width="450" height="300" alt="Screenshot 2026-03-19 at 4 35 43 PM" src="https://github.com/user-attachments/assets/ded4ec87-4d4d-4349-89f8-74ce749c07b1" />


## Repository Structure
`MLUnsupervisedApp/`  
Contains the Unsupervised Machine Learning Streamlit application, including clustering, PCA, and interactive model exploration.

`MLStreamlitApp/`
Contains the Machine Learning Explorer Streamlit application, including model training, evaluation, and user-interactive features.

`Streamlitapp-Project/`
Contains the Spotify Tracks Explorer Streamlit application and related project files.

`TidyData-Project/`
Contains the Tidy Data Project notebook and related project files.

`class_work/`
Contains weekly notebooks, in-class exercises, and coursework completed throughout the semester.

## Skills Demonstrated
- Data cleaning and transformation with pandas
- Exploratory data analysis
- Data visualization with matplotlib, pandas plotting, and seaborn
- Building interactive applications with Streamlit
- Organizing projects and documentation using GitHub

## Author
Maria Jose Molina  
GitHub: https://github.com/mmolina2
