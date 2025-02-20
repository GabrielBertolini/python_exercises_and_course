import streamlit as st
import requests
import pandas as pd

url="https://viacep.com.br/ws/{cep}/json/"

st.title("CEP search")

cep=st.text_input("Search your CEP: ")

if cep != "":

    try:
        answer=requests.get(url.format(cep=cep))
        data= pd.DataFrame([answer.json()])
        st.dataframe(data,hide_index=True)
    
    except Exception as err:
        st.error("Enter a valid CEP")