import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import json
from custom_pasrser import *

css = '''
<style>

</style>
'''





def main():
    st.set_page_config(page_title="Machine Code Optimiser")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    st.header("MACHINE CODE OPTIMISER")
    st.divider()
    st.subheader('Machine Code Optimizer is a Streamlit web application that utilizes language models to optimize machine code. This tool allows users to upload machine code files, specify a machine name, and receive optimized code as well as cycle time analysis.')
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload", accept_multiple_files=False)
        machine = st.text_input("Enter Machine Name :")
        button = st.button("Process")
    if uploaded_file is not None and machine:
        try:
            file_data = uploaded_file.read().decode('utf-8')
            processed_data = file_data
            if button: 
                try:
                    llm_response(file_data,machine)
                except Exception as E:
                    st.error(f"LLM RESPONSE ERROR : {E}")
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")

    else:
        st.error(f"Some Feilds Are Missing")

if __name__ == '__main__':
    main()