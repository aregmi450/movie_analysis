# importing the libraries needed
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

# importing the dataset
movieRatings = pd.read_csv("tv_shows.csv", index_col=[0])

# filling empty datasets

movieRatings.Age = movieRatings.Age.fillna('all')

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
st.write("""#### Lists of movies filtered by Age Group and Release Year """)
dataframe_genre_year = movieRatings[new_genre_year]\
    .groupby(['Title', 'Age'])['Year'].sum()
dataframe_genre_year = dataframe_genre_year.reset_index()
st.dataframe(dataframe_genre_year, width=650)


col1, col2 = st.columns(2)

# showing piechart on the dashboard
with col1:
    st.write("# Pie Chart Showing Shows from Different OTT")
    movieRatings.rename(columns={"Prime Video": "PrimeVideo"}, inplace=True)
    netflix = movieRatings['Netflix'].sum()
    hulu = movieRatings['Hulu'].sum()
    disney = movieRatings['Disney+'].sum()
    prime = movieRatings['PrimeVideo'].sum()
    labels = ['Netflix', 'Hulu', 'Disney+', 'Prime Video']
    values = [netflix, hulu, disney, prime]
    piechart, ax1 = plt.subplots(figsize=(10, 4))
    ax1.pie(values, labels=labels, startangle=90)
    ax1.axis('equal')
    st.pyplot(piechart)


# using seaborn to create plot
with col2:
    st.write("# Bar Chart Showing Age Wise Distribution of Shows")
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(x="Age", data=movieRatings)
    st.pyplot(fig)


# showing top 10 rated movies in Rotten Tomatoes

st.write('## Top 10 Rated Movies in Rotten Tomatoes')
movieRatings.rename(
    columns={"Rotten Tomatoes": "RottenTomatoes"}, inplace=True)
movieRatings['RottenTomatoes'] = movieRatings['RottenTomatoes'].fillna(
    '0/100').apply(lambda x: int((x).split('/')[0]))
top10movies = movieRatings.nlargest(10, ['RottenTomatoes'])
st. table(top10movies[["Title", "Year", "RottenTomatoes", "Age"]])

# showing top 10 rated movies in IMDb
st.write('## Top 10 Rated Movies in IMDB')
movieRatings['IMDb'] = movieRatings['IMDb'].fillna(
    '0/10').apply(lambda x: float((x).split('/')[0]))
top10movies = movieRatings.nlargest(10, ['IMDb'])
st. table(top10movies[["Title", "Year", "IMDb", "Age"]])
