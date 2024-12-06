from langchain.document_loaders.pdf import PyPDFLoader
from langchain.indexes import VectorstorIndeCreator
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st

from watsonxlangchain import LangChainInterface

st.title('Ask watsonx')

prompt = st.chat_input('Ask a Question')

if prompt: