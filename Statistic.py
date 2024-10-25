import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Main Page")

# Create a sidebar
st.sidebar.title("Main Page")

# Main content
st.header("Mexico Disease Spread Report")
st.subheader("This is the report regarding Mexico Disease Statistics in 2024")

# Import and display image
im = Image.open('shrdc_logo (1).png')
st.image(im, width=700)