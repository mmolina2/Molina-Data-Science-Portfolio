# Spotify Tracks Explorer (Streamlit App)

This project is a simple Streamlit app that allows users to explore a Spotify tracks dataset. The goal was to build an interactive tool where users can filter, sort, and search through music data.

## Features

- Load a dataset from a CSV file  
- Filter tracks by:
  - Genre  
  - Popularity  
  - Tempo (BPM)  
  - Track name or artist (search)  
- Sort tracks by popularity, tempo, or danceability  
- Display filtered results in a table  
- View a bar chart of the most frequent artists in the filtered data  

## How to Run the App

1. Clone this repository:
git clone https://github.com/mmolina2/Molina-Data-Science-Portfolio
2. Navigate to the project folder:
cd Streamlitapp-Project
3. Install the required libraries
streamlit
pandas
4. Run the app:
streamlit run main.py

## Example Output

### App Interface
![App Interface](images/app_interface.png)

### Filters and Results
![Filters](images/filters.png)

### Top Artists Chart
![Top Artists](images/top_artists.png)

## Notes

- The dataset is loaded from a local CSV file inside the project  
- Filters are applied step-by-step so results update dynamically  
- The app was built using Streamlit to practice creating interactive data tools  

## Tools Used

- Python  
- Streamlit  
- Pandas  

## What I Learned

- How to build an interactive app using Streamlit  
- How to filter and manipulate data using pandas  
- How to organize a project and connect it to GitHub  