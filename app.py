import streamlit as st
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from g4f.client import Client

# Load environment variables from .env file
load_dotenv()

# Initialize the GPT client
client = Client()

# MongoDB connection URI
uri = os.getenv("MONGO_URI")
# Create a new client and connect to the server
mongo_client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    mongo_client.admin.command('ping')
    st.success("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    st.error(f"Error connecting to MongoDB: {e}")

# Streamlit app title
st.title("AI-Powered Smart Recipe Modifier")

# Input for recipe and dietary restrictions
recipe_name = st.text_input("Enter your recipe name:")
ingredients = st.text_area("Enter your ingredients (comma-separated):")
dietary_restrictions = st.text_input("Enter dietary restrictions (e.g., gluten-free, vegetarian):")

# Button to submit the inputs
if st.button("Submit"):
    if recipe_name and ingredients:
        st.write("Generating recipe suggestions...")
        
        # Prepare the input for the GPT model
        user_input = (
            f"Given the recipe name '{recipe_name}' with the following ingredients: {ingredients}, "
            f"and considering the dietary restrictions: {dietary_restrictions}, "
            "provide suggestions on how to modify this recipe."
        )
        
        # Call the GPT model to get a response
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": user_input
                    }
                ],
            )
            
            # Display the generated response
            st.success("Here are your recipe modification suggestions:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error retrieving response from the AI model: {e}")
    else:
        st.error("Please fill in both the recipe name and ingredients.")
