# Basic Streamlit App

This Streamlit app is part of my Introduction to Data Science portfolio.  
It allows users to explore a dataset interactively using filters and summary statistics.

## Dataset

This app uses a **Spotify tracks dataset** from Kaggle.  
The dataset contains information about individual songs, including audio features
(such as popularity, energy, and danceability) as well as categorical attributes like
genre and artist.

This dataset is well-suited for exploratory data analysis because it includes both
numeric and categorical variables, making it easy to filter and compare different
types of music.

## How to Run the App

From the root of this repository, run:

```bash
pip install streamlit pandas
streamlit run basic_streamlit_app/main.py
