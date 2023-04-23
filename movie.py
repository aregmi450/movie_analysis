#!/usr/bin/env python
# coding: utf-8

# ## Importing the necessary modules and libraries for the project. Also importing the dataset. 

# In[ ]:


#importing the libraries needed 
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


# In[ ]:


#importing the dataset 
movieRatings = pd.read_csv("tv_shows.csv", index_col= [0])
movieRatings.head()


# In[ ]:


movieRatings.dtypes


# ## Cleaning the dataset 
# 1. First checking the duplicate datas in the dataset 
# 2. Checking the null values in the dataset
# 3. Dropping the row containing null values and replacing some null values with 0 

# In[ ]:


#check duplicate values
movieRatings.duplicated()


# In[ ]:


movieRatings.isnull()


# In[ ]:


#dropping null values 
movieRatings.dropna(axis=0, how ='any').shape
movieRatings.dropna(axis=0, how ='any', inplace = True)


# ## Renaming the column names for easily accessible operations 

# In[ ]:


movieRatings.rename(columns = {"Rotten Tomatoes": "RottenTomatoes"}, inplace=True)
movieRatings.rename(columns = {"Prime Video": "PrimeVideo"}, inplace=True)


# In[ ]:


movieRatings.head()


# ## Converting the data type from object to integer and changing fraction to integer 

# In[ ]:


# finding the top 10 movies in Rotten Tomatoes Ranking 
movieRatings['RottenTomatoes'] = movieRatings['RottenTomatoes'].fillna('0/100').apply(lambda x: int((x).split('/')[0]))
movieRatings['IMDb'] = movieRatings['IMDb'].fillna('0.0/10').apply(lambda x: float((x).split('/')[0]))


# In[ ]:


movieRatings.sort_values(by= "RottenTomatoes", ascending=False).head(10)


# ### Pie Chart Showing Shows Around Different OTT Pltaforms 

# In[ ]:


netflix = movieRatings['Netflix'].sum()
hulu = movieRatings['Hulu'].sum()
disney = movieRatings['Disney+'].sum()
prime = movieRatings['PrimeVideo'].sum()
labels = ['Netflix', 'Hulu', 'Disney+', 'Prime Video']
values = [netflix, hulu, disney, prime]
plt.pie(values, labels = labels);
plt.legend(title="Users Around Different OTT Pltafroms");


# The pie chart formed shows that the highest number of shows are available on Netflix, followed by Hulu and Prime Video.
# Disney+ has comparatively less number of shows among the OTT Pltaforms. This shows why Netflix is popular among all the OTT 
# Pltaforms. Disney+ might have less number of shows due to its late coming in the market. 

# # Analysis of Data Related to Age 

# In[ ]:


year = movieRatings['Age'].unique()
year


# In[ ]:


#removing + from age column to change the datatype to integer 

movieRatings['Age'] = movieRatings['Age'].replace(['18+', '16+', '7+', '13+', 'all'],['18', '16', '7', '13', '1'])
movieRatings["Age"] = pd.to_numeric(movieRatings["Age"])


# ## Bar Graph Showing Age wise Show Distribution

# In[ ]:


sns.countplot(x='Age', data=movieRatings);
plt.title('Bar Graph Showing Age wise Show Distribution');


# This shows the graph plot showing the count of shows in the dataset according to the agewise censorship. Most of the TV Shows 
# were for mature audience who were above 16 years of age, Least number of shows were for audiences who were just starting their
# teenage. I think more shows regarding the changes they might face in their older years must be built on to provide them 
# knowledge on how to deal with the problems they might face in the future. 

# # Scatter Plot of Age vs Year 

# In[ ]:


sns.scatterplot(y='Year', x='Age', data=movieRatings);
plt.title('Scatter Plot Showing Age vs Release Year');


# The scatter plot shows the distribution between the year of movies released versus the age group the movie could be watched by.
# The scatter plot shows that most of the movies are for the audiences of all age and comparative number of shows are of the 
# viewers above age of 16 but few amounts of show are targeted to the viewers above age of 13. 
# 

# ### Top 10 Movies on Each Rating Sites 

# In[ ]:


top10movies = movieRatings.nlargest(10, ['RottenTomatoes'])
top10movies


# In[ ]:


sns.barplot(y="Title", x="RottenTomatoes", data=top10movies);
plt.title('Top 10 Movies on Rotten Tomatoes');


# The bar graph expresses the result obtained from the query above. This shows that Breaking Bad and RicK & Morty are the 
# best rated TV shows in the Rotten Tomatoes platform.

# In[ ]:


top10moviesIMDb = movieRatings.nlargest(10, ['IMDb'])
top10moviesIMDb


# In[ ]:


sns.barplot(y='Title', x='IMDb', data=top10moviesIMDb);
plt.title('Top 10 movies on IMDB');


# The bar graph is created to form the visualization obtained in the above query. The result obtained from both the visualizations
# shows that "Rick and Morty ", "Breaking Bad", and "Avatar: The Last Airbender" are the three shows which are in the top 10 
# rankings for both rating platform. 

# ### Calculating the movies in dataset with 100 Rotten Tomatoes rating 

# In[ ]:


movieRatings[movieRatings.RottenTomatoes == 100].count()


# The result shows that the dataset consists of two entries with 100 rating on Rotten Tomatoes. 

# ## Line Graph Between movies before and after 2000 on the basis of age categories 

# In[ ]:


#Movies before 2000 
Before2000 = movieRatings[(movieRatings['Year'] <= 2000 )]
Before2000


# In[ ]:


#movies after 2000
After2000 = movieRatings[(movieRatings['Year'] > 2000)]
After2000


# In[ ]:



#imdb rating plot 
a =movieRatings.IMDb
b = movieRatings.RottenTomatoes;
plt.plot(a, color='r', label='IMDB');
plt.plot(b, color='g',label='RottenTomatoes');
plt.title('Line Plot Showing IMDB and Rotten Tomatoes Ratings for every show in the data');
plt.legend();


# The plot above shows the overall range of ratings on two different platforms, As IMDB ratings are 1-10 on rating they are at lower part of the visualization whereas the Rotten Tomatoes rating are fluctuating a lot due to the rating being carried out on a higher rate.  
