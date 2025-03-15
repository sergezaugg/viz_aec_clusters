#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# run locally : streamlit run stmain.py
#--------------------

import streamlit as st
from streamlit import session_state as ss

# stuff shared across pages 
if 'colors_1' not in ss:
    ss['colors_1'] = ['#0000ff']
if 'colors_2' not in ss:
    ss['colors_2'] = ['#0055ff', '#0077dd', '#0099bb']

st.set_page_config(layout="wide")

p01 = st.Page("st_page_01.py", title="Interactive")
p02 = st.Page("st_page_02.py", title="Data detes and licences")
p03 = st.Page("st_page_03.py", title="Methods")

pg = st.navigation([p01, p02, p03])

pg.run()

with st.sidebar:

    st.header(''':red[**CLUSTERING UNSELECTED BIO-ACOUSTIC RECORDINGS**]''')
    st.markdown(''':red[**Preliminary and still under development**]''')
    st.markdown(''' 
        **SUMMARY:**
        Explore spectrogram clusters obtained via auto-encoders, dimensionality reduction and unsupervised clustering.
        This page currently only features clustering with DBSCAN.
        Feature extraction with auto-encoders and dimensionality reduction with UMAP is currently performed offline and still experimental. 
         
        **CHALLENGE:**
        The training and test images are unselected: the audio files were sequentially cut into pieces, thus
        many clips contain only nuisance or background noise and calls are often truncated.
        All XC-recorings have mp3 artifacts and some have high/low pass filtering artifacts. 
                
        **LONG-TERM OBJECTIVE:**
        Once ready, this tool could contribute to automatically create pre-labelled dataset with a fine time-scale.
        This could considerably speed-up the the manually confirmed annotation of a huge dataset taken from XC to train supervised models.                   
        ''')
    
    # st.title(""); st.title("")
    st.markdown(''':red[LINKS]''')
    st.page_link("https://xeno-canto.org/", label=":gray[xeno-canto]")
    st.page_link("https://github.com/sergezaugg/xeno_canto_organizer", label=":gray[xeno-canto organizer]")







