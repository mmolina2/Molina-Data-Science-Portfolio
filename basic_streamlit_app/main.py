import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------- Page setup ----------------
st.set_page_config(page_title="Spotify Tracks Explorer", layout="wide")

st.title("Spotify Tracks Explorer")
st.write(
    "This app loads a Spotify tracks dataset from a CSV file and lets you filter, "
    "sort, and explore tracks interactively."
)

# ---------------- Load data ----------------
DATA_PATH = Path(__file__).parent / "data" / "dataset.csv"

@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

try:
    df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error(f"Could not find dataset at: {DATA_PATH}")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("The dataset file is empty or not a valid CSV.")
    st.stop()

# ---------------- Dataset preview ----------------
st.subheader("Dataset Preview")
st.write(f"Rows: {len(df):,} | Columns: {df.shape[1]}")
st.dataframe(df.head(50), use_container_width=True)

# ---------------- Sidebar filters ----------------
st.sidebar.header("Filters")
filtered_df = df.copy()

# Genre filter
if "track_genre" in filtered_df.columns:
    genres = sorted(filtered_df["track_genre"].dropna().unique())
    selected_genres = st.sidebar.multiselect(
        "Select genre(s)",
        options=genres,
        default=genres[:5] if len(genres) >= 5 else genres
    )
    if selected_genres:
        filtered_df = filtered_df[filtered_df["track_genre"].isin(selected_genres)]

# Popularity filter
if "popularity" in filtered_df.columns:
    pop_min = int(filtered_df["popularity"].min())
    pop_max = int(filtered_df["popularity"].max())
    pop_range = st.sidebar.slider("Popularity", pop_min, pop_max, (pop_min, pop_max))
    filtered_df = filtered_df[filtered_df["popularity"].between(pop_range[0], pop_range[1])]

# Tempo filter
if "tempo" in filtered_df.columns:
    tempo_min = float(filtered_df["tempo"].min())
    tempo_max = float(filtered_df["tempo"].max())
    tempo_range = st.sidebar.slider("Tempo (BPM)", tempo_min, tempo_max, (tempo_min, tempo_max))
    filtered_df = filtered_df[filtered_df["tempo"].between(tempo_range[0], tempo_range[1])]

# Search filter
query = st.sidebar.text_input("Search track/artist")
if query and "track_name" in filtered_df.columns and "artists" in filtered_df.columns:
    q = query.lower()
    filtered_df = filtered_df[
        filtered_df["track_name"].astype(str).str.lower().str.contains(q, na=False)
        | filtered_df["artists"].astype(str).str.lower().str.contains(q, na=False)
    ]

# Sort controls
sort_by = st.sidebar.radio("Sort by", ["popularity", "tempo", "danceability"], index=0)
descending = st.sidebar.checkbox("Sort descending", value=True)

if sort_by in filtered_df.columns:
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=not descending)

# Show top N rows (controls the ONE table)
top_n_rows = st.sidebar.number_input(
    "Show top N rows",
    min_value=10,
    max_value=500,
    value=50,
    step=10
)

# ---------------- Display results (ONLY ONE table) ----------------
st.subheader("Filtered Results")
st.write(f"Filtered rows: {len(filtered_df):,}")
st.dataframe(filtered_df.head(int(top_n_rows)), use_container_width=True)

# ---------------- Top Artists chart ----------------
st.subheader("Top Artists (in filtered data)")
st.caption("Y-axis = number of tracks by each artist in the filtered results.")

if "artists" in filtered_df.columns:
    top_n_artists = st.slider("Top N artists", 5, 30, 10)
    top_artists = filtered_df["artists"].astype(str).value_counts().head(top_n_artists)
    st.bar_chart(top_artists)
else:
    st.info("No 'artists' column found in this dataset.")
