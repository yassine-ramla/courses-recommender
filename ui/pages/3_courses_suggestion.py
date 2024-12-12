import streamlit as st
import os
import random
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import fpgrowth, association_rules

st.set_page_config(
  page_title='courses recommender',
  page_icon="📚",
  layout="centered",
  # initial_sidebar_state: InitialSideBarState = "auto"
)

data_folder_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

user_courses = pd.read_csv(f'{data_folder_path}/user_with_courses.csv')

st.title('explore new courses 📚')

courses = pd.read_csv(f'{data_folder_path}/course_processed.csv')
courses.rename(columns={'COURSE_ID': 'course_id', 'TITLE': 'title', 'DESCRIPTION': 'description'}, inplace=True)

ratings = pd.read_csv(f'{data_folder_path}/ratings.csv')
ratings.rename(columns={'user': 'user_id', 'item': 'course_id'}, inplace=True)

unique_rated_course_ids = ratings['course_id'].unique()

rated_courses = courses[courses['course_id'].isin(unique_rated_course_ids)].reset_index(drop=True)

title_to_id = dict(zip(rated_courses['title'], rated_courses['course_id']))

selected_titles = st.multiselect(
    "# select the courses you've watched",
    rated_courses['title'], 
    help="Select the courses you have completed to get tailored recommendations.",
    label_visibility="visible",
  )

selected_ids = [title_to_id[title] for title in selected_titles]

algorithm = st.selectbox(
    "Choose an algorithm for recommendations:",
    ["apriori", "eclat", "fp_growth"],
    help="Choose the algorithm you prefer for generating course recommendations."
)

if st.button("Submit"):
    if not selected_ids:
        st.warning("Please select at least one course.")
    elif not algorithm:
        st.warning("Please choose an algorithm.")
    else:
        st.success(f"Generating recommendations using {algorithm}...")