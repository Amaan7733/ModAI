import google.generativeai as genai
import os 
from dotenv import load_dotenv, find_dotenv
import streamlit as st
_ = load_dotenv(find_dotenv())

# A function to generate a solution
def genAI(prompt):
    os.environ["GRPC_VERBOSITY"] = "None"
    genai.configure(api_key=os.environ.get("API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
    res = model.generate_content(prompt)
    return res.text

# i have three features:

st.title("MoDAI")
st.header("______________")
st.text("let's build future together.")

# input
input = st.text_area("What's in your mind.")
st.text("Select your model")
option= st.radio("",("Text Genreation", "Text Summarization", "Text Translator"))
add_input = st.text_input("Type your preferred language*")
btn = st.button("Generate")

if btn and not input:
    st.text("Ooops!...It seems you does not provided input...")
elif btn and input:
    if option == "Text Genreation":
# 1. Text Genreation Model.
        prompt = f"""Provide some detail on this : '{input}'"""
        response = genAI(prompt)
    elif option == "Text Summarization":
# 2. Text Summarization model.
        prompt = f"""You have to summarize the input and present the output in concise way.
        the output will be in 70-90 words in last present some facts related this input.
        input: '{input}'"""
        response = genAI(prompt)
    else:
  

        prompt = f"""You are an expert translator and i want your help to translate the input in '{add_input}' language.
             the given input is: '{input}' """
        response = genAI(prompt)


# 3. Language Translation Model.

    st.text_area("Output",response, height=600)


