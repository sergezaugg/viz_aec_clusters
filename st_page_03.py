#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st

c00, c01  = st.columns([0.5, 0.2])
with c00:
    with st.container(border=True) : 
        st.subheader("Short methods")
        st.markdown(''' 
            The training set consists of 900 mp3 recording from Northern Europe that were downloaded from [xeno-canto](https://xeno-canto.org).
            The mp3s were down-sampled to 24'000 sps, then cut in 1.0 seconds pieces and transformed to spectrograms resulting in 6714 grey-scale images of 128 x 1152 pixels (freq x time).
            These images were used to train convolutional auto-encoders (CAE) under a de-noising regime with PyTorch.
            The encoder weights were saved to be used later for feature extraction.   
            The encoder does not apply full pooling in time, this allows to feed long-spectrograms and reduces impact of zero padding at the time-edges.                    
                    
            The test set (shown here) comes from 571 mp3 recordings from South-Western Europe taken from [xeno-canto](https://xeno-canto.org).
            The recordings were down-sampled to 24'000 sps, cut into shorter 0.2 seconds pieces, and transformed to spectrograms.
            This gave 60'560 grey-scale mini-images of 128 x 256 pixels (freq x time).
            These images were piped through the pre-trained encoder to obtain a feature matrix (60'463 rows x 256 columns) 
            The 256 columns correspond to the dim of the latent vector in the CAE, not the 256 time-pixels of the images ;-)
            The feature matrix can be interactively dim-reduced with [UMAP](https://umap-learn.readthedocs.io) to the final matrix, e.g. to 60'463 x 32. 
            The final matrix can be interactively processed with [DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html) and the mini-images can be plotted grouped by clusters.                               
            ''')
        
       


        


