#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st

c00, c01  = st.columns([0.6, 0.4])
with c00:
    with st.container(border=True) : 
        st.header("Preliminary Discussion")

        st.text("<UNDER CONSTRUCTION>")

        st.markdown(''' 
                          
        * **Challenge**
            * Training and test images are unselected: the audio files were sequentially cut into pieces, many only contain nuisance sounds and background noise.
                    
        * **Current limitations**
            * Many clusters have an edge bias, i.e. sounds are located all at one side of clip. 
            * This is probably due to zero padding during test set prediction of the 128*128 clips.  
            * DBSCAN parameter are very sensitive: small change induce large differences in the quality of clustering.
                    
        * **Promising behavior**
            * Some visually consistent patterns coming from different mp3 recordings are clustered together. 
            * Worked for certain narrow-band sounds and also short broad-band sounds.
                
                                
        ''')
       


        


