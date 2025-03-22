#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss

st.set_page_config(layout="wide")

p01 = st.Page("st_page_01.py", title="Interactive")
p02 = st.Page("st_page_02.py", title="Data info")
p03 = st.Page("st_page_03.py", title="Explanations")
p04 = st.Page("st_page_04.py", title="Examples")
p05 = st.Page("st_page_05.py", title="References")
p06 = st.Page("st_page_06.py", title="Changes")

pg = st.navigation([p01, p06, p02, p03, p04, p05])

pg.run()

with st.sidebar:

    st.header(''':red[**CLUSTERING UNSELECTED BIO-ACOUSTIC RECORDINGS**]''')
    st.markdown(''':red[**Alpha - under development**]''')
    st.markdown(''' 
        Spectrogram clusters obtained via auto-encoders, dimensionality reduction and unsupervised clustering.
        This page only features dim reduction and clustering.
        Once ready, this tool could pre-label dataset and boost the annotation of datasets for supervised models.                   
        ''')
    
    st.markdown(''':red[LINKS]''')
    st.page_link("https://xeno-canto.org/", label=":gray[xeno-canto]")
    st.page_link("https://github.com/sergezaugg/xeno_canto_organizer", label=":gray[xeno-canto organizer]")
