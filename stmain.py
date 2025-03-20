#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss
# import umap


# stuff shared across pages 
if 'colors_1' not in ss:
    ss['colors_1'] = ['#0000ff']
if 'colors_2' not in ss:
    ss['colors_2'] = ['#0055ff', '#0077dd', '#0099bb']

st.set_page_config(layout="wide")

p01 = st.Page("st_page_01.py", title="Interactive")
p02 = st.Page("st_page_02.py", title="Data info")
p03 = st.Page("st_page_03.py", title="Methods")
p04 = st.Page("st_page_04.py", title="Examples")
p05 = st.Page("st_page_05.py", title="References")

pg = st.navigation([p01, p02, p03, p04, p05])

pg.run()

with st.sidebar:

    st.header(''':red[**CLUSTERING UNSELECTED BIO-ACOUSTIC RECORDINGS**]''')
    st.markdown(''':red[**Preliminary and still under development**]''')
    st.markdown(''' 
        **SUMMARY:**
        Spectrogram clusters were obtained via auto-encoders, dimensionality reduction and unsupervised clustering.
        This page currently only features the last step, clustering with DBSCAN.
        Once ready, this tool could automatically create pre-labelled dataset.
        This could speed-up the annotation of datasets to train supervised models.                   
        ''')
    
    st.markdown(''':red[LINKS]''')
    st.page_link("https://xeno-canto.org/", label=":gray[xeno-canto]")
    st.page_link("https://github.com/sergezaugg/xeno_canto_organizer", label=":gray[xeno-canto organizer]")







