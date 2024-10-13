import streamlit as st

# Title and description
st.title("Shelf Smart")
st.write("An AI-powered tool to help you modify your recipes for healthier and dietary-friendly alternatives.")

# Input section for recipe
st.header("Input Your Recipe")
recipe_input = st.text_area("Paste your recipe here (ingredients and instructions):")

# Dropdown for dietary preferences
st.header("Select Dietary Preferences")
diet_option = st.selectbox(
    "Choose your dietary preferences:",
    ("None", "Vegan", "Gluten-free", "Low-carb", "Low-calorie")
)

# Submit button
if st.button("Get Recipe Modifications"):
    st.write("Processing your recipe...")
    # Send data to backend here