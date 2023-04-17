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
