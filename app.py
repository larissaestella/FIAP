import streamlit as st

st.title("Earthquake Data Explorer")
st.text("This is a web app to explore earthquake data.")

uploaded_file = st.file_uploader ('Upload your file here')

