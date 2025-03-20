#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st

c00, c01  = st.columns([0.8, 0.1])
with c00:
    with st.container(border=True) : 
        st.markdown('''20250316: First deployment, clips are square 128 x 128, Dim reduction via UMAP precomputed and fixed to 32 dims''')
        st.markdown('''20250320: Test clips now have 128 freq x 256 time bins, feature extracted for center time bins only only (Padding with real data instead of zeros)''')
        st.markdown('''20250320: Dim reduction via UMAP integrated into the dashboard, slow but fun (and interesting)''')

        






    

        

        


