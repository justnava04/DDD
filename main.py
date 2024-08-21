import streamlit as st
import seaborn as sns
df = sns.load_dataset('iris')
df

st.sidebar.title('Classifiers')
classifier = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'DT', 'RF', 'NN'))
