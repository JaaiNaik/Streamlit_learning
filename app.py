import streamlit as st

st.header("_Learning_  is fun :blue[We are cool] :sunglasses:")

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python")

st.subheader("I am enjoying this, :green[check the code]")
st.subheader("I am enjoying this, :yellow[check the code]")
