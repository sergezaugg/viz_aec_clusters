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
p02 = st.Page("st_page_02.py", title="Data details")

pg = st.navigation([p01, p02])

pg.run()








with st.sidebar:

    # st.markdown(''':red[#**Clustering unselected bio-acoustic data**]''')
    st.header(''':red[**Clustering unselected bio-acoustic data**]''')

    st.markdown(''':red[**-- Under development --**]''')

    st.markdown(''' 
        Explore spectrogram clusters obtained via auto-encoders, dimensionality reduction via UMAP, and clustering with DBSCAN.
        This page only features the last step, exploration of clustering with DBSCAN. Feature extraction (auto-encoders) and dimensionality reduction (UMAP) is currently performed offline and still heavily experimental.                          
        
        Currently based on a static dataset of 60560 grey-scale mini-images of 128x128 pixels.
        Images are MP3 recording downloaded from xeno-canto and transformed to spectrograms.
        
        ''')

    




    # st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title("")
    st.title(""); st.title(""); st.title(""); st.title("") 
    st.markdown(''':gray[Acoutic data from xeno-canto pre-processed with ]''')
    st.page_link("https://github.com/sergezaugg/xeno_canto_organizer", label=":gray[xeno-canto organizer]")
    st.page_link("https://xeno-canto.org/", label=":gray[xeno-canto]")



