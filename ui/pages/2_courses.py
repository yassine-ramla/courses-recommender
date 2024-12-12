import streamlit as st
import pandas as pd
import random
import os

st.set_page_config(
  page_title='courses recommender',
  page_icon="📚",
  layout="centered",
  # initial_sidebar_state: InitialSideBarState = "auto"
)

# # courses 
data_folder_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')

courses = pd.read_csv(f'{data_folder_path}/course_processed.csv')
ratings = pd.read_csv(f'{data_folder_path}/ratings.csv')

courses.rename(columns={'COURSE_ID': 'course_id', 'TITLE': 'title', 'DESCRIPTION': 'description'}, inplace=True)
ratings.rename(columns={'user': 'user_id', 'item': 'course_id'}, inplace=True)
random.seed(7)
ratings['rating'] = ratings['rating'].apply(lambda _: random.choice([1, 1, 1.5, 2, 2.5, 2.5, 3, 3, 3, 3, 3.5, 3.5, 3.5, 3.5, 3.5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4.5, 4.5, 4, 4, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4, 4, 4, 5, 5, 5]))

st.header('📈 data story:')

st.subheader('courses head: ')
st.dataframe(courses.head())
st.subheader('courses tail: ')
st.dataframe(courses.tail())

ratings_courses = ratings.merge(courses, on='course_id')
avg_courses_rating = ratings_courses.groupby(by='course_id')['rating'].mean().reset_index().rename({'rating': 'average_rating'}, axis=1)
courses_ratings_number = ratings_courses.groupby(by='course_id')['rating'].count().reset_index().rename({'rating': 'ratings_number'}, axis=1)
courses_ratings_summery = avg_courses_rating.merge(courses_ratings_number, on='course_id').merge(courses, on='course_id')

st.subheader('average courses rating and ratings number: ')
st.dataframe(courses_ratings_summery.head())

ratings_number = courses['course_id'].nunique()
missing_vals = courses.isna().sum().sum()
courses_number = courses['course_id'].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("number of ratings", f'{ratings_number} ⭐')
col2.metric("missing values", f'{missing_vals} ❔')
col3.metric("number of rated courses", f'{courses_number} 📚')

best_rated_courses = courses_ratings_summery.sort_values(by='average_rating', ascending=False).head(10)
worst_rated_courses = courses_ratings_summery.sort_values(by='average_rating').head(10)
most_rated_courses = courses_ratings_summery.sort_values(by='ratings_number',  ascending=False).head(10)

st.markdown('## best rated courses:')
st.bar_chart(best_rated_courses, x='title', y='average_rating')

st.markdown('## worst rated courses:')
st.bar_chart(worst_rated_courses, x='title', y='average_rating')

st.markdown('## most rated courses:')
st.bar_chart(most_rated_courses, x='title', y='ratings_number')