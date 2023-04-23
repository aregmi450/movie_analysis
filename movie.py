# ## Importing the necessary modules and libraries for the project. Also importing the dataset.

# importing the libraries needed
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

st.write("### Showing Movie Dataset Stats")

# importing the dataset
movieRatings = pd.read_csv("tv_shows.csv", index_col=[0])

# st.table(movieRatings)


# # movieRatings.dtypes


# # ## Cleaning the dataset
# # 1. First checking the duplicate datas in the dataset
# # 2. Checking the null values in the dataset
# # 3. Dropping the row containing null values and replacing some null values with 0


# # check duplicate values
# # movieRatings.duplicated()


# # movieRatings.isnull()


# # dropping null values
# movieRatings.dropna(axis=0, how='any').shape
# movieRatings.dropna(axis=0, how='any', inplace=True)


# # ## Renaming the column names for easily accessible operations


# movieRatings.rename(
#     columns={"Rotten Tomatoes": "RottenTomatoes"}, inplace=True)
# movieRatings.rename(columns={"Prime Video": "PrimeVideo"}, inplace=True)


# # movieRatings.head()


# # ## Converting the data type from object to integer and changing fraction to integer


# # finding the top 10 movies in Rotten Tomatoes Ranking
# movieRatings['RottenTomatoes'] = movieRatings['RottenTomatoes'].fillna(
#     '0/100').apply(lambda x: int((x).split('/')[0]))
# movieRatings['IMDb'] = movieRatings['IMDb'].fillna(
#     '0.0/10').apply(lambda x: float((x).split('/')[0]))


# movieRatings.sort_values(by="RottenTomatoes", ascending=False).head(10)


# # ### Pie Chart Showing Shows Around Different OTT Pltaforms


# netflix = movieRatings['Netflix'].sum()
# hulu = movieRatings['Hulu'].sum()
# disney = movieRatings['Disney+'].sum()
# prime = movieRatings['PrimeVideo'].sum()
# labels = ['Netflix', 'Hulu', 'Disney+', 'Prime Video']
# values = [netflix, hulu, disney, prime]
# plt.pie(values, labels=labels)
# plt.legend(title="Users Around Different OTT Pltafroms")

# # DISPLAYING SELECT BOX TO SHOW YEAR WISE MOVIE LIST
year_list = movieRatings['Year'].unique().tolist()
age_group = movieRatings['Age'].unique().tolist()


year = st.selectbox('Choose a Year', year_list, 0)
age = st.multiselect('Choose preferred Age Group', age_group, default=[
    '18+', 'all'])

# visualization first one

st.write("""## Lists of movies filtered by  Released Year """)

# Filter the selectbox and multiselect widget for interactivity
new_genre_year = (movieRatings['Age'].isin(age)) \
    & (movieRatings['Year'] == year)

dataframe_genre_year = movieRatings[new_genre_year]\
    .groupby(['Title', 'Age'])['Year'].sum()
dataframe_genre_year = dataframe_genre_year.reset_index()
st.dataframe(dataframe_genre_year, width=400)


# The pie chart formed shows that the highest number of shows are available on Netflix, followed by Hulu and Prime Video.
# Disney+ has comparatively less number of shows among the OTT Pltaforms. This shows why Netflix is popular among all the OTT
# Pltaforms. Disney+ might have less number of shows due to its late coming in the market.

# # Analysis of Data Related to Age

# year = movieRatings['Age'].unique()
# year

# removing + from age column to change the datatype to integer

# movieRatings['Age'] = movieRatings['Age'].replace(
#     ['18+', '16+', '7+', '13+', 'all'], ['18', '16', '7', '13', '1'])
# movieRatings["Age"] = pd.to_numeric(movieRatings["Age"])


# ## Bar Graph Showing Age wise Show Distribution

# In[ ]:


agegraph = sns.countplot(x='Age', data=movieRatings)
plt.title('Bar Graph Showing Age wise Show Distribution')

# st.plotly_chart(agegraph)

# This shows the graph plot showing the count of shows in the dataset according to the agewise censorship. Most of the TV Shows
# were for mature audience who were above 16 years of age, Least number of shows were for audiences who were just starting their
# teenage. I think more shows regarding the changes they might face in their older years must be built on to provide them
# knowledge on how to deal with the problems they might face in the future.

# # Scatter Plot of Age vs Year

st.write('## Top 10 Rated Movies in Rotten Tomatoes')
movieRatings.rename(
    columns={"Rotten Tomatoes": "RottenTomatoes"}, inplace=True)
movieRatings['RottenTomatoes'] = movieRatings['RottenTomatoes'].fillna(
    '0/100').apply(lambda x: int((x).split('/')[0]))
top10movies = movieRatings.nlargest(10, ['RottenTomatoes'])
# st. table(top10movies)
st.bar_chart(x="Title", y="RottenTomatoes", data=top10movies)
