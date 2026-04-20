import streamlit as st
import pandas as pd
from pathlib import Path

# Page title and short intro
st.set_page_config(page_title="Spotify Tracks Explorer", layout="wide")

st.title("Spotify Tracks Explorer")
st.write(
    "This app lets the user explore a Spotify tracks dataset by filtering, sorting, "
    "and searching for songs or artists."
)

# Load the dataset
DATA_PATH = Path(__file__).parent / "data" / "dataset.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


try:
    df = load_data()
except FileNotFoundError:
    st.error(f"Could not find the dataset file at: {DATA_PATH}")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("The dataset file is empty or not a valid CSV.")
    st.stop()

# Show a quick preview
st.subheader("Dataset Preview")
st.write(f"Rows: {len(df):,} | Columns: {df.shape[1]}")
st.dataframe(df.head(50), use_container_width=True)

# Make a copy so the original dataframe stays unchanged
filtered_df = df.copy()

# Create the sidebar filters
st.sidebar.header("Filters")

# Filter by genre
if "track_genre" in filtered_df.columns:
    genre_list = sorted(filtered_df["track_genre"].dropna().unique())

    selected_genres = st.sidebar.multiselect(
        "Select genre(s)",
        options=genre_list,
        default=genre_list[:5] if len(genre_list) >= 5 else genre_list
    )

    if selected_genres:
        filtered_df = filtered_df[filtered_df["track_genre"].isin(selected_genres)]

# Filter by popularity
if "popularity" in filtered_df.columns:
    min_popularity = int(filtered_df["popularity"].min())
    max_popularity = int(filtered_df["popularity"].max())

    popularity_range = st.sidebar.slider(
        "Popularity",
        min_popularity,
        max_popularity,
        (min_popularity, max_popularity)
    )

    filtered_df = filtered_df[
        filtered_df["popularity"].between(popularity_range[0], popularity_range[1])
    ]

# Filter by tempo
if "tempo" in filtered_df.columns:
    min_tempo = float(filtered_df["tempo"].min())
    max_tempo = float(filtered_df["tempo"].max())

    tempo_range = st.sidebar.slider(
        "Tempo (BPM)",
        min_tempo,
        max_tempo,
        (min_tempo, max_tempo)
    )

    filtered_df = filtered_df[
        filtered_df["tempo"].between(tempo_range[0], tempo_range[1])
    ]

# Search by track name or artist
search_text = st.sidebar.text_input("Search track/artist")

if search_text and "track_name" in filtered_df.columns and "artists" in filtered_df.columns:
    search_text = search_text.lower()

    filtered_df = filtered_df[
        filtered_df["track_name"].astype(str).str.lower().str.contains(search_text, na=False)
        | filtered_df["artists"].astype(str).str.lower().str.contains(search_text, na=False)
    ]

# Choose sort options
sort_options = ["popularity", "tempo", "danceability"]
available_sort_options = [col for col in sort_options if col in filtered_df.columns]

if available_sort_options:
    sort_by = st.sidebar.radio("Sort by", available_sort_options, index=0)
    sort_descending = st.sidebar.checkbox("Sort descending", value=True)

    filtered_df = filtered_df.sort_values(
        by=sort_by,
        ascending=not sort_descending
    )

# Control how many rows appear in the results table
top_n_rows = st.sidebar.number_input(
    "Show top N rows",
    min_value=10,
    max_value=500,
    value=50,
    step=10
)

# Show the filtered results
st.subheader("Filtered Results")
st.write(f"Filtered rows: {len(filtered_df):,}")

# Small summary to make the app more informative
summary_col1, summary_col2, summary_col3 = st.columns(3)

summary_col1.metric("Tracks Shown", min(len(filtered_df), int(top_n_rows)))
summary_col2.metric("Total Filtered Tracks", len(filtered_df))

if "track_genre" in filtered_df.columns:
    summary_col3.metric("Genres in Results", filtered_df["track_genre"].nunique())
else:
    summary_col3.metric("Genres in Results", 0)

st.dataframe(filtered_df.head(int(top_n_rows)), use_container_width=True)

# Top artists chart
st.subheader("Top Artists in Filtered Results")
st.caption("This chart shows which artists appear most often after the filters are applied.")

if "artists" in filtered_df.columns and len(filtered_df) > 0:
    top_n_artists = st.slider("Top N artists", 5, 30, 10)

    top_artists = (
        filtered_df["artists"]
        .astype(str)
        .value_counts()
        .head(top_n_artists)
    )

    st.bar_chart(top_artists)
else:
    st.info("No artist data is available for the current filtered results.")
<<<<<<< HEAD
    
=======
>>>>>>> dedff90f161e20ef0ca5ed8de95ad34c0880b769
