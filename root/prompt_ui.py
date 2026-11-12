from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOllama(
    model="llama3.2",
    temperature=0,
)
st.header("Research Tool")
entered_prompt = st.text_input("Enter your promt")

if  entered_prompt:
    st.write("getting the data.....")
    result = model.invoke(entered_prompt)
    print(result)
    st.write(result.content)
   

