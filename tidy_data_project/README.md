# Tidy Data Project

# Overview
This project demonstrates how to clean and transform a dataset into tidy format using Python and pandas. The dataset I chose contains Olympic medalists from 2008, but it is initially stored in an untidy format where multiple variables are combined into column names. For example, gender and sport are combined into one column, and there are many missing values.

The goal of this project is to restructure the dataset so that it follows tidy data principles, making it easier to analyze and visualize.

# Tidy Data Principles
According to tidy data principles:
- Each variable should have its own column
- Each observation should have its own row
- Each type of observational unit should form its own table

This project applies these principles to reorganize the dataset into a clean and usable format, to later create visualizations based on the information. 

# Dataset Information
The dataset contains Olympic medalists from 2008:
- Athlete names are stored in one column  
- Other columns combine gender and sport (e.g: 'male_archery', or 'female_athletics')  
- Medal types (gold, silver, bronze) are stored as values  

This structure makes the dataset difficult to analyze, so it must be reshaped.

# Tools Used
- Python
- pandas
- matplotlib
- seaborn

# Key Steps

## 1. Data Cleaning
- Reshaped the dataset using 'melt()' to convert from wide to long format  
- Removed missing values using 'dropna()'  
- Split combined columns into separate variables using 'str.split()' 
- Cleaned text using 'str.replace()'  

## 2. Data Transformation
- Created a tidy dataset with the following columns:
  - medalist_name  
  - gender  
  - sport  
  - medal  

## 3. Pivot Table
- Used 'pd.pivot_table()' to summarize medal counts by sport and medal type  

## 4. Visualizations
- Bar chart showing top sports by number of medals  
- Bar chart showing distribution of medal types  

# How to Run This Project

1. Clone this repository:
git clone https://github.com/mmolina2/Molina-Data-Science-Portfolio

2. Navigate to the project folder

3. Install required libraries (if needed):
pip install pandas matplotlib seaborn

4. Open the notebook:
tidy_data_project.ipynb

5. Run all cells to reproduce the analysis and visualizations

# References
- Pandas Cheat Sheet  
- Tidy Data by Hadley Wickham