import requests
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("API_KEY")

# Streamlit app code
st.title("Shelf Smart")

recipe_input = st.text_area("Paste your recipe here:")
diet_option = st.selectbox("Choose your dietary preferences:", ["None", "Vegan", "Gluten-free", "Low-carb", "Low-calorie"])

if st.button("Get Recipe Modifications"):
    if recipe_input:
        data = {
            "recipe": recipe_input,
            "diet": diet_option
        }
        
        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }
        
        # Example API request using your key
        response = requests.post("https://api.yourservice.com/modify-recipe", json=data, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            st.write("Modified Recipe:")
            st.write(result['substitutions'])
            st.write("Nutritional Information:")
            st.write(result['nutrition'])
        else:
            st.write("Error: Could not retrieve the data.")
    else:
        st.write("Please input a recipe.")
