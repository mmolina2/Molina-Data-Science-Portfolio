import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")
# --- Button example ---
if st.button("Click me!"):
    st.write("🎉 You clicked the button! Nice work! 🚀")
else:
    st.write("Click the button to see what happens...")

# --- Color picker example ---
color = st.color_picker("Pick a color", "#00f900")
st.write(f"You picked: {color}")
import pandas as pd

st.subheader("Exploring Our Dataset")

# Load the CSV file
df = pd.read_csv("data/sample_data.csv")

st.write("Here's our data:")
st.dataframe(df)
# Filter by city
city = st.selectbox("Select a city", df["City"].unique())
filtered_df = df[df["City"] == city]

st.write(f"People in {city}:")
st.dataframe(filtered_df)

# Filter by occupation
occupation = st.selectbox("Select an occupation", df["Occupation"].unique())
filtered_df = df[(df["City"] == city) & (df["Occupation"] == occupation)]

st.write(f"{occupation}s in {city}:")
st.dataframe(filtered_df)

# Show summary statistics
st.subheader("Summary Statistics")
st.write(df.describe())