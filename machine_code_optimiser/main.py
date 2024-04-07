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
    .element-container:has(>.stTextArea), .stTextArea {
        width: 800px !important;
    }
    .stTextArea textarea {
        height: 400px;
    }
</style>
'''





def main():
    st.set_page_config(page_title="Machine Code Optimiser")
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    st.header("MACHINE CODE OPTIMISER")
    # user_question = st.text_input("Ask a question :")
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload", accept_multiple_files=False)
        machine = st.text_input("Enter Machine Name :")
        button = st.button("Process")
    # if user_question:
    #     ans = llm_response(user_question)
        # formatted_ans = parse_llm_response(ans)
        # st.write(f"Your question: {user_question}")
        # st.write(f"Answer: {ans}")  
    if uploaded_file is not None and machine:
        try:
            file_data = uploaded_file.read().decode('utf-8')
            processed_data = file_data
            if button: 
                # st.write("**Processed Data:**")  
                # st.text(file_data)
                try:
                    llm_response(file_data,machine)
                except Exception as E:
                    st.error(f"LLM RESPONSE ERROR : {E}")
        except Exception as e:
            st.error(f"Error reading uploaded file: {e}")

    else:
        st.error(f"Some Feilds Are Missing")

    # response = lm(messages)



    

# def parse_llm_response(llm_output):
#     parsed_text = ""
#     essential_sections = ["previous code", "new optimised code", "cycle time difference"]

#     for section in essential_sections:
#         section_start = llm_output.lower().find(section)
#         if section_start != -1:
#             section_end = llm_output.find("\n", section_start)
#             if section_end != -1:
#                 section_content = llm_output[section_start:section_end].strip()
#                 parsed_text += f"**{section.title()}**:\n{section_content}\n\n"
#         else:
#             return None

#     if parsed_text:
#         return parsed_text
#     else:
#         return None


if __name__ == '__main__':
    main()
    