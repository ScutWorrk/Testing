import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

#load_dotenv()
genai.configure(api_key = st.secrets.GOOGLE_API_KEY)

# Set up Streamlit app
st.title('Image Caption Generator')

# Drag and drop functionality for image upload
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)

    # Generate caption using Gemini
    llm = ChatGoogleGenerativeAI(model="gemini-pro-vision", google_api_key=os.getenv("GOOGLE_API_KEY"))
    
    message = HumanMessage(
        content=[
            {
            "type":"text",
            "text":"""You are an influencer on instagram. Make a short and trendy caption in a single sentence 
                    for sosial media to attract people attention.
                    For example this image "https://www.instagram.com/p/C4vUWQ6pVWN/" with the caption 
                    Good afternoon 🐾 
                    Meow meow meow 😽💕 
                    It's Wednesday Holiday 
                    Holidays in the middle of the week are priceless 😳 
                    Well, let's work hard for two more days 😂
                    Relax and relax

                    #catsoftheday #catto #cat_delight #cutecats_oftheworld 
                    #cat_features #cataccount #catpage #catmeow #cats_of_world 
                    #cats_of_instaworld #catstocker #meowed #meowdeling 
                    #meowcats #meowmeowmeow
                        
                    Include hastags and emojis.
                    Maximum 3 hastags and moderate emojis"""
            },
            {
                "type": "image_url",
                "image_url": uploaded_image
            }
        ]
    )
    
    response = llm.invoke([message])
    
    # Display the generated caption
    st.write('Generated Caption:')
    st.write(response.content)