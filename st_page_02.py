#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import os
import streamlit as st
from utils import load_meta_data

path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")
df_meta = load_meta_data(path = path_meta_data)

c00, c01  = st.columns([0.5, 0.2])
with c00:
    with st.container(border=True) :   
        st.subheader('''Many thanks to all the passionate people that shared their recordings via the xeno-canto platform.''')
        st.text('''For a detailed list of recordists see the field "rec" in the table below. Each files has a Creative Commons license, see field "lic" in the table below.''')
        st.dataframe(df_meta, hide_index = True)
        st.page_link("https://xeno-canto.org/", label=":gray[Link to xeno-canto web]")
        # st.divider()

        # c0, c1, c2 = st.columns([0.5, 0.3,0.3])
        # with c0:
        #     st.subheader("Licences")
        #     st.dataframe(df_meta['lic'].value_counts())
        # with c1:
        #     st.subheader("Countries")
        #     st.dataframe(df_meta['cnt'].value_counts())
        # with c2:
        #     st.subheader("Sampling rates")
        #     st.dataframe(df_meta['smp'].value_counts())


            