#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st
import os

c00, c01  = st.columns([0.9, 0.1])
with c00:
    with st.container(border=True) : 
       
        st.subheader("Screenshots of a few consistent clusters found with this tool")
        st.text("UMAP mapping depends on a random seed, thus these result cannot be exactly reproduced")

        st.divider()
        st.subheader("Screenshot 1")
        st.image(os.path.join('pics/Screenshot 2025-03-21 214654.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 2")
        st.image(os.path.join('pics/Screenshot 2025-03-21 214847.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 3")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215144.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 4")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215259.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 5")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215412.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 6")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215452.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 7")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215633.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 8")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215838.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 9")
        st.image(os.path.join('pics/Screenshot 2025-03-21 215931.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 10")
        st.image(os.path.join('pics/Screenshot 2025-03-21 220022.png'), use_container_width=True, caption = '')
        st.divider()





