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
from utils import apply_dbscan_clustering, load_reduced_features, load_meta_data

# initialize session state 
if 'dbscan_params' not in ss:
    ss['dbscan_params'] = {
        'eps' : 0.18,
        'min_samples' : 10,
        'aaa' : 666,
        }
     

if 'plot_par' not in ss:
    ss['plot_par'] = {
        'min_clu_size' : 1,
        'max_clu_size' : 200,
        }



#--------------------------------
# streamlit frontend starts here 


impath = "spectrogram_images"

path_features = os.path.join("extracted_features/features_reduced_2.npz")

path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")




df_meta = load_meta_data(path = path_meta_data)
# df_meta.shape

feat, filnam = load_reduced_features(path = path_features)
# feat.shape

df = apply_dbscan_clustering(x = feat, labels = filnam, eps = ss['dbscan_params']["eps"], min_samples = ss['dbscan_params']["min_samples"])
# df.shape


# select DBSCAN params 
with st.form("my_form"):
   
    ss['dbscan_params']["eps"]         = st.slider(label = "DBSCAN eps", min_value=0.05, max_value=3.0, value=ss['dbscan_params']["eps"], step=0.05,)
    ss['dbscan_params']["min_samples"] = st.slider(label = "DBSCAN min_samples", min_value=1, max_value=100, value=ss['dbscan_params']["min_samples"], step=1,)

    submitted = st.form_submit_button("Submit new DBSCAN params")
    if submitted:
        st.rerun()


ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"] = st.slider(
    label = "max cluster size plotted", 
    min_value=1, 
    max_value=1000, 
    value=(ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"]), 
    step=1)


# select the cluster to display 
sel_1 = df['cluster_id'].value_counts() >= ss['plot_par']["min_clu_size"]
sel_2 = df['cluster_id'].value_counts() <= ss['plot_par']["max_clu_size"]
sel_3 = np.logical_and(sel_1, sel_2)


all_availabel_clusters = df['cluster_id'].value_counts().index
# exclude some very large clusters 
selected_clusters = all_availabel_clusters[sel_3]


st.text(len(all_availabel_clusters))
st.text(len(selected_clusters))


if len(selected_clusters) <= 1:
    st.text("Not enough clusters: Eps is probably too high, try to reduce it ")
else:
    selected_cluster_id = st.select_slider(label = "select a cluster id", options = selected_clusters )
    # selected_cluster_id = 6
    df_sel = df[df['cluster_id']==selected_cluster_id]
    # df_sel = df_sel.iloc[0:100]
    selected_images_files = df_sel['file_name']
    # st.text(selected_images_files.shape)
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



