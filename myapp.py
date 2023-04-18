# importing the libraries needed
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# importing the dataset
movieRatings = pd.read_csv("tv_shows.csv", index_col=[0])

# Creating sidebar widget unique values from our movies dataset

age_list = movieRatings['Age'].unique().tolist()
year_list = movieRatings['Year'].unique().tolist()


st.write("Select your preferred age group and type the year from which series you want to search: ")

# create a multiselect widget to display genre
new_age_list = st.multiselect('Choose Age Range:', age_list, default=[
                              '18+', '16+', '7+', 'all'])
# create a selectbox option that holds all unique years
year = st.selectbox('Choose a Year', year_list, 0)

# Filter the selectbox and multiselect widget for interactivity
new_genre_year = (movieRatings['Age'].isin(new_age_list)) \
    & (movieRatings['Year'] == year)


# visualization
col1, col2 = st.columns(2)
with col1:
    st.write("""#### Lists of movies filtered by Age Group and Release Year """)
    dataframe_genre_year = movieRatings[new_genre_year]\
        .groupby(['Title', 'Age'])['Year'].sum()
    dataframe_genre_year = dataframe_genre_year.reset_index()
    st.dataframe(dataframe_genre_year, width=400)

# with col1:
#     st.write("""#### Lists of movies filtered by year  """)
#     year_list = movieRatings[year]\
#         .groupby(['name', 'genre'])['year'].sum()
#     year_list = year_list.reset_index()
#     st.dataframe(year_list, width=400)
