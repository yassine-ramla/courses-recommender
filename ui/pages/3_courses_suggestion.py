import streamlit as st
import pandas as pd
from models.fp_growth import fp_growth_recommend
from models.apriori import apriori_recommend
import os
import re

st.set_page_config(
    page_title='Courses Recommender',
    page_icon="📚",
    layout="centered",
)

data_folder_path = os.path.join(os.path.dirname(__file__), '..', 'data')

# Use caching to load data and rules
@st.cache_data
def load_data():
    rated_courses = pd.read_csv(os.path.join(data_folder_path,'rated_courses.csv'))
    fp_growth_rules = pd.read_csv(os.path.join(data_folder_path,'fp_growth_association_rules.csv'))
    apriori_rules = pd.read_pickle(os.path.join(data_folder_path,'apriori_rules.pkl'))
    return rated_courses, fp_growth_rules, apriori_rules

rated_courses, fp_growth_rules, apriori_rules = load_data()


# UI
st.title('Explore New Courses 📚')

selected_titles = st.multiselect(
    "# Select the courses you've watched",
    rated_courses['title'] + ' (#' + rated_courses['course_id'] + ')',
    help="Select the courses you have completed to get tailored recommendations.",
)

selected_ids = {re.search(r"#(\w+)\)", title).group(1) for title in selected_titles if re.search(r"#(\w+)\)", title)}

algorithm = st.selectbox(
    "Choose an algorithm for recommendations:",
    ["apriori", "eclat", "fp_growth"],
    help="Choose the algorithm you prefer for generating course recommendations."
)

if st.button("Get Recommendations"):
    if algorithm == 'apriori':
        recommendations = apriori_recommend(apriori_rules, selected_ids)
    elif algorithm == 'eclat':
        pass
    else:
        recommendations = fp_growth_recommend(fp_growth_rules, selected_ids)
    if recommendations:
        recommended_courses = rated_courses[rated_courses['course_id'].isin(recommendations)]['title'].tolist()
        st.write("Recommended courses:", recommended_courses)
    else:
        st.write("No recommendations found.")
