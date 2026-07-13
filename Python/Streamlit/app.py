import streamlit as st
import pandas as pd

st.write("Hello World")

st.title("Hello Streamlit")

st.write("This is my first streamlit app")

st.header("Welcome to streamlit")
st.subheader("This is subheader")
st.text("This is plane text")

# buttons, checkboxes, sliders

button = st.button("Click me!")

if button :
    st.write("button clicked")

agree = st.checkbox("I agree")

if agree:
    st.write("You agreed")

level=st.slider("Select a level",1,10)  # 1 is default if 4th parameter not given. 

st.write(f"Selected Level : {level}")

uploaded_file = st.file_uploader("Upload a file", type=["csv","txt"])

if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    st.write(df.head())