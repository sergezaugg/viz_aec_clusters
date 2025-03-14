#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train, assess performance and feature importance
#--------------------

import os
import streamlit as st
import plotly.express as px
from streamlit import session_state as ss
import numpy as np
import pandas as pd
# from sklearn.cluster import DBSCAN
from sklearn.utils import shuffle
from utils import apply_dbscan_clustering, load_reduced_features

# initialize session state 
if 'aaa' not in ss:
    ss['aaa'] = 30
if 'bbb' not in ss:
    ss['bbb'] = 1


#--------------------------------
# streamlit frontend starts here 


impath = "spectrogram_images"

path_features = os.path.join("extracted_features/features_reduced_2.npz")


feat, filnam = load_reduced_features(path = path_features)
# feat.shape


df = apply_dbscan_clustering(x = feat, labels = filnam, eps = 0.18, min_samples = 10)

# df.shape


all_availabel_clusters = df['cluster_id'].value_counts().index

max_clust_size = 50
sel_2 = df['cluster_id'].value_counts() <= max_clust_size


# exclude some very large clusters 
selected_clusters = all_availabel_clusters[sel_2]
all_availabel_clusters.shape
selected_clusters.shape


selected_cluster_id = st.selectbox(label = "select a cluster id", options = selected_clusters )
# selected_cluster_id = 6

df_sel = df[df['cluster_id']==selected_cluster_id]
df_sel = df_sel.iloc[0:100]


selected_images_files = df_sel['file_name']
st.text(selected_images_files.shape)
# st.text(selected_images_files)



#  show images 
num_cols = 10
grid = st.columns(num_cols)
col = 0
for ii, im_filname in enumerate(selected_images_files):
    try:
        with grid[col]:
            with st.container(border=True):
                st.image(os.path.join(impath, im_filname), caption=im_filname[0:10])
        col += 1
        if ii % num_cols == (num_cols-1):
            col = 0
        print('OK')    
    except:
        print('shit')        



