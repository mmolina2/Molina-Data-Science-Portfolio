import streamlit as st
import pandas as pd

st.title("Basic Streamlit Data Explorer")
st.write(
    "This app loads a Spotify dataset from a CSV file and allows users to explore it "
    "using interactive filters."
)
df = pd.read_csv("basic_streamlit_app/data/dataset.csv.zip")

st.subheader("Dataset Preview")
st.dataframe(df)

st.sidebar.header("Filters")

filtered_df = df.copy()

if "genre" in df.columns:
    genre = st.sidebar.selectbox(
        "Select genre:",
        options=["All"] + sorted(df["genre"].dropna().unique().tolist())
    )
    if genre != "All":
        filtered_df = filtered_df[filtered_df["genre"] == genre]

if "popularity" in df.columns:
    min_pop = int(df["popularity"].min())
    max_pop = int(df["popularity"].max())
    popularity_range = st.sidebar.slider(
        "Popularity range:",
        min_value=min_pop,
        max_value=max_pop,
        value=(min_pop, max_pop)
    )
    filtered_df = filtered_df[
        (filtered_df["popularity"] >= popularity_range[0]) &
        (filtered_df["popularity"] <= popularity_range[1])
    ]

# Show filtered results
st.subheader("Filtered Results")
st.write(f"Number of tracks: {len(filtered_df)}")
st.dataframe(filtered_df)
