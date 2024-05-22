import streamlit as st 
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os 
from dotenv import load_dotenv

load_dotenv()
parser = StrOutputParser()

api_key_groq = os.getenv('grok_api')
llm = ChatGroq(temperature=0, groq_api_key=api_key_groq, model_name="mixtral-8x7b-32768")


prompt_template = """
            You are a very reputable arabic text summarizer, Your job is to
            summarize this given arabic text {text} .

            """
prompt = PromptTemplate(
    input_variables=["text"], template=prompt_template
)


chain = prompt | llm | parser

with st.sidebar:
    st.markdown('''
هذا مشروع قامت به هند رحيم عراق الميالي. هذا المشروع عبارة عن ملخص نص عربي
            باستخدام نموذج لغة كبير.
''')
    
st.title('ملخص النص العربي')
text = st.text_input('أدخل بعض النصوص العربية هنا لتلخيصها')
if text:
    st.write(chain.invoke(text))

