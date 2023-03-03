from cgi import test
import streamlit as st

st.set_page_config(page_title="test web page", layout="wide")

st.header("what is up GSWL")
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']