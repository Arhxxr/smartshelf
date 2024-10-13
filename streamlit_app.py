import requests
import streamlit as st

# API URL of the backend (adjust the localhost/host URL)
API_URL = "http://localhost:5000/modify-recipe"

# Input for recipe
st.title("Shelf Smart")
recipe_input = st.text_area("Paste your recipe here:")
diet_option = st.selectbox("Choose your dietary preferences:", ["None", "Vegan", "Gluten-free", "Low-carb", "Low-calorie"])

if st.button("Get Recipe Modifications"):
    # Send request to backend
    if recipe_input:
        data = {
            "recipe": recipe_input,
            "diet": diet_option
        }
        response = requests.post(API_URL, json=data)
        
        if response.status_code == 200:
            # Display the modified recipe and nutrition
            modified_recipe = response.json()
            st.write("Modified Recipe: ")
            st.write(modified_recipe['substitutions'])
            st.write("Nutritional Information: ")
            st.write(modified_recipe['nutrition'])
        else:
            st.write("Error: Could not modify the recipe.")
    else:
        st.write("Please input a recipe.")
