# Spotify Tracks Explorer (Streamlit App)

This Streamlit app provides an interactive way to explore a Spotify tracks dataset. Users can filter, sort, and visualize tracks using a variety of controls.

## Features
- Load data from a CSV file
- Filter tracks by:
  - Genre
  - Popularity
  - Tempo (BPM)
  - Track or artist name (search)
- Sort tracks by popularity, tempo, or danceability
- Display a single filtered results table
- View the most frequent artists in the filtered dataset

## How to run

From the repository root:s

```bash
pip install streamlit pandas
streamlit run basic_streamlit_app/main.py