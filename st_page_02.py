#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import os
import streamlit as st
import pandas as pd
from utils import load_meta_data

path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")
df_meta = load_meta_data(path = path_meta_data)

c00, c01  = st.columns([0.5, 0.2])
with c00:
    with st.container(border=True) :   
        st.subheader('''Many thanks to all the passionate people that shared their recordings via the xeno-canto platform.''')
        st.text('''For a detailed list of recordists see the field "rec" in the table below. Each files has a Creative Commons license, see field "lic" in the table below.''')
        st.dataframe(df_meta, hide_index = True, height=300)
        st.page_link("https://xeno-canto.org/", label=":gray[Link to xeno-canto web]")
        # st.divider()

        c1, c2, c3 = st.columns([0.9, 0.2, 0.2])
       
        with c1:
            st.text("Files: Country vs primary species")
            st.dataframe(pd.crosstab( df_meta['full_spec_name'], df_meta['cnt']) ,  height=600, use_container_width = True)  
        with c2:
            st.text("File durations")
            st.dataframe(df_meta['length'].value_counts(), use_container_width = True)
        with c3:
            st.text("File sampl. rates")
            st.dataframe(df_meta['smp'].value_counts(), use_container_width = True)




            

            