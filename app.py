import streamlit as st
import pandas as pd
import pickle

# Load style
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load dataset
movies = pickle.load(open("movies.pkl","rb"))

st.title("🎬 Movie Recommendation System")

st.write("Deep Learning based Movie Recommender using CNN")

# Genre selection
genre = st.selectbox(
    "Select Movie Genre",
    sorted(movies["genres"].unique())
)

# Recommendation function
def recommend_movies(genre_name, top_n=10):

    recommendations = movies[movies["genres"]==genre_name]

    recommendations = recommendations.sort_values(
        by="averageRating",
        ascending=False
    )

    return recommendations[["primaryTitle","genres","averageRating"]].head(top_n)

# Button
if st.button("Recommend Movies"):

    result = recommend_movies(genre)

    st.write("### Top Recommended Movies")

    st.dataframe(result)