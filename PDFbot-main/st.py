# Frontend.py
from http.client import HTTPException

import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from PDF_reader import PDF_reader
from openai import OpenAI
from openai import OpenAIError

from BOT import BOT
from PDF_reader import PDF_reader




page_bg_img = """
<style>
[data-testid= "stAppViewContainer"] {
background-image: url("https://wallpapercave.com/wp/wp7921358.jpg");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}

[data-testid="stSidebar"]{
background-image: url("https://i.pinimg.com/564x/fd/ba/64/fdba646e4210ef03a987b8253d22a7a5.jpg");
background-size: cover;
}

[data-estid="element-Container"] {
background-color: rgb(192,192,192);
background-size: cover;
}

[data-testid="stContainer"] {
    background-color: lightgray;
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Galactico 💬")



bot = BOT()
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain
# from langchain.memory import ConversationBufferMemory
# from langchain.vectorstores import FAISS

pdf = None
load_dotenv()


user_question = st.text_input("Ask a question about your documents:")

with st.sidebar:
    st.write("To see the source code,click below:")
    st.write("[Learn More >](https://github.com/AnanyaBt/PDFbot)") 
    st.subheader("Your documents")
    pdf_docs = st.file_uploader(
            "Upload your PDFs here'",
        accept_multiple_files=False
        )

    if pdf_docs:
        with st.spinner('Processing'):

             pdf = PDF_reader(pdf_docs)



answer_container = st.container()

col1, col2 = st.columns(2)

if col1.button("Ask"):
    if pdf is not None:
        chunk, page_no = pdf.get_relevant_chunks(user_question)
        response = bot.answer(user_question, chunk, page_no)[0]
        with answer_container:
            st.markdown(f'<p style="color:#FFFFFF;font-size:14px;">{response}</p>', unsafe_allow_html=True)
            if page_no != 'none':
                st.markdown(f'<p style="color:#FFFFFF;font-size:14px;">Page {page_no}</p>', unsafe_allow_html=True)

if col2.button("Summary"):
    if pdf is not None:
        chunks = pdf.get_relevant_chunks(user_question)
        summary = bot.summarize(chunks)
        with answer_container:
            st.write(summary)

   






        
   





