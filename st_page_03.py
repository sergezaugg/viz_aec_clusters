#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st

c00, c01  = st.columns([0.6, 0.4])
with c00:
    with st.container(border=True) : 
        st.header("Methods in a nutshell")

        st.text("<UNDER CONSTRUCTION>")

        st.markdown('''     

            The training set consists of 900 mp3 recording from Northern Europe that were downloaded from xeno-canto.
            The mp3s were down-sampled to 24'000 sps, then cut in 1.0 seconds pieces and transformed to spectrograms resulting in 6714 long grey-scale images of 128 x 1152 pixels (freq x time).
            These images were used to train convolutional auto-encoders under a de-noising regime with PyTorch.
            The encoder weights were saved to be used later for feature extraction.              
                    
            The test set (shown here) comes from 571 mp3 recordings from South-Western Europe taken from xeno-canto.
            The mp3s down-sampled to 24'000 sps, then were cut in shorter 0.2 seconds pieces and transformed to spectrograms, which gave 60'560 grey-scale mini-images of 128 x 128 pixels (freq x time).
            These images were piped through the pre-trained encoder to obtain a feature matrix (60'560 rows x 15xx columns) 
            The feature matrix was dim-reduced with UMAP to the final matrix (60'560 x 32). 
            In this dashboard, the final matrix can be interactively processed with DBSCAN and the square mini-images can be plotted grouped by clusters.        
                                
            ''')
        st.subheader("Links")
        st.page_link("https://umap-learn.readthedocs.io", label="UMAP")
        st.page_link("https://pytorch.org", label="PyTorch")
        st.page_link("https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html", label="DBSCAN")


        


