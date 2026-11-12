from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatOllama(
    model="llama3.2",
    temperature=0,
)
st.header("Research Tool")
profession = st.text_input("Enter the Profession")
what_info_want = st.text_input("Want kind of info you want")
entered_prompt =  f"""
Act as {profession} who is working more than 10 years.
give information about {what_info_want}.
keep tone proffessional and give summary in every easy to understand manner for non technical people.
use graphs and numbers where required. keep data reserched and not vague numbers.
keep it sweet and simple have boundries to the report.
"""
result = ""
button = st.button(
    "generate the Report",
)
if  entered_prompt and button:
    st.write("getting the data.....")
    result = model.invoke(entered_prompt)
    print(result)
    st.write(result.content)
   

