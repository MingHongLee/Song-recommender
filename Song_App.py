import streamlit as st
from PIL import Image
import pandas as pd  # Make sure to import pandas

# Title and description
st.title("ITI105 Song Recommender App")

logo = Image.open("images/spotify.png")
st.image(logo)

# Get user input
song = st.text_input("What is your favourite song?")

# Display message only if user has provided input
if song:
    st.write(f"Since you like '{song}', you may also like these similar songs:")

    # List of recommended songs by artists
    df = pd.DataFrame({
        'Song': ['Song 1', 'Song 2', 'Song 3', 'Song 4'],
        'Artist': ['Singer 1', 'Singer 2', 'Singer 3', 'Singer 4']
    })

    # Adjust index to start from 1
    df.index = df.index + 1

    # Display the DataFrame
    st.dataframe(df)
