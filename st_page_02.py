#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import os
import streamlit as st
from utils import load_meta_data

path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")
df_meta = load_meta_data(path = path_meta_data)
st.header("xeno-canto data credits, licences and details")
st.page_link("https://xeno-canto.org/", label=":gray[Link to xeno-canto web]")
st.dataframe(df_meta)
# st.dataframe(df_meta['lic'].value_counts())
st.divider()
