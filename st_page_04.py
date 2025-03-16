#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st
import os

c00, c01  = st.columns([0.9, 0.1])
with c00:
    with st.container(border=True) : 
        st.header("Short discussion")

        st.markdown('''                 
        * Audio files were sequentially cut into pieces, this is challenging because many contain only nuisance sounds or background noise.
        * Many clusters have an edge bias, i.e. sounds are located all at one side of clip. 
        * This is probably due to zero padding during test set prediction of the 128*128 clips.  
        * Some visually consistent patterns coming from different mp3 recordings are clustered together.             
        * Worked for certain narrow-band sounds and also short broad-band sounds.    
        * Some interesting clusters are shown below and many more can be generated interactively.                              
        ''')

        st.divider()
        st.subheader("Screenshot 1")
        st.image(os.path.join('pics\Screenshot11.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 2")
        st.image(os.path.join('pics\Screenshot16.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 3")
        st.image(os.path.join('pics\Screenshot21.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 4")
        st.image(os.path.join('pics\Screenshot23.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 5")
        st.image(os.path.join('pics\Screenshot24.png'), use_container_width=True, caption = '')
        st.divider()
        st.subheader("Screenshot 6")
        st.image(os.path.join('pics\Screenshot25.png'), use_container_width=True, caption = '')

        


