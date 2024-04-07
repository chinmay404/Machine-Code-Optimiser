from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
import json
import streamlit as st




def llm_response(user_question,machine):
    
    with st.spinner("Optimizing your machine code..."):
        load_dotenv()
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro", temperature=0.1, convert_system_message_to_human=True
        )
        x = prompt_creation(user_question, machine=machine)
        # print(x)
        ans = llm.invoke(x)
        response_message = ans.content
        response_message = response_message.replace("```json", "").strip()
        response_message = response_message.replace("```", "").strip()
        # print(response_message)
        with open("response.json", "w") as f:
            json.dump(response_message, f)
        response_data = json.loads(response_message)
        machine_name = response_data.get("machine_name", "")
        optimised_report = response_data.get("optimised_Report", "")
        cycle_time_analysis = response_data.get("cycle_time_analysis", "")
        st.success("Machine code optimization complete!",)
        st.subheader("RESPONSE :")
        st.write("Machine Name:", machine_name)
        st.divider()
        st.text_area("Optimised Report:", optimised_report)
        st.divider()
        st.text_area("Cycle Time Analysis:", cycle_time_analysis)

        with open("optimised_report.txt", "w") as f:
            f.write(optimised_report)
        st.download_button(
            label="Download Optimised Report",
            data=optimised_report,
            file_name="optimised_report.txt",
        )
    return ans


def prompt_creation(user_question, machine):

    try:
        machine_name_schema = ResponseSchema(name="machine_name",
                                             description="This refers to the name of the Machine")
        optimised_resport_schema = ResponseSchema(name="optimised_Report",
                                                  description="This refers to the Optimised version of report")
        cycle_time_schema = ResponseSchema(name="cycle_time_analysis",
                                           description="This refers to the Cycle Time analysis Of Previous code and optimised code")
        response_schema = [
            machine_name_schema,
            optimised_resport_schema,
            cycle_time_schema
        ]

        output_parser = StructuredOutputParser.from_response_schemas(
            response_schema)
        format_instructions = output_parser.get_format_instructions()

        template = '''You are a Machine Code Optimiser who had done thousands of machine code  optimisation of machine. Pluse show Cycle Time analysis without giving previous code and optimised code . Strictly give response in Json Format.
        feilds are complsary be in reposne 'machine_name' , 'optimised_Report' ,'cycle_time_analysis'
        format should be like this: 
        
        "machine_name": "",
        "optimised_Report": "",
        "cycle_time_analysis": ""
        
        user Machine Code :{user_question}
        machine : {machine}
        {format_instructions}
        
        '''
        prompt_template = ChatPromptTemplate.from_template(template)
        return prompt_template.format_messages(machine=machine, format_instructions=format_instructions, user_question=user_question)
    except Exception as e:
        print(f"EXCEPTION : {e}")
