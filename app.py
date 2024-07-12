import streamlit as st
import pickle
import pandas as pd

#8265bd1679663a7ea12ac168da84d2e8
#https://api.themoviedb.org/3/movie/%7Bmovie_id%7D?api_key=%3C%3Capi_key%3E%3E&language=en-US
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommender System')

similarity = pickle.load(open('similarity.pkl','rb'))


selected_movie_name = st.selectbox("Choose your movie",movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)