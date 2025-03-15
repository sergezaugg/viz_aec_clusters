#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train, assess performance and feature importance
#--------------------

import os
import streamlit as st
from streamlit import session_state as ss
import numpy as np
# import pandas as pd
from utils import apply_dbscan_clustering, load_reduced_features, load_meta_data, constrain_cluster_size

# initialize session state 
if 'dbscan_params' not in ss:
    ss['dbscan_params'] = {
        'eps' : 0.20,
        'min_samples' : 10,
        'aaa' : 666,
        }
     
if 'plot_par' not in ss:
    ss['plot_par'] = {
        'min_clu_size' : 10,
        'max_clu_size' : 200,
        }

# define paths 
impath = "spectrogram_images"
path_features = os.path.join("extracted_features/features_reduced_4.npz")
path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")

#--------------------------------
# computational block 
df_meta = load_meta_data(path = path_meta_data)
# df_meta.shape
feat, filnam = load_reduced_features(path = path_features)
# feat.shape
df = apply_dbscan_clustering(x = feat, labels = filnam, eps = ss['dbscan_params']["eps"], min_samples = ss['dbscan_params']["min_samples"])
# df.shape
selected_clusters = constrain_cluster_size(df_clusters = df, min_size = ss['plot_par']["min_clu_size"], max_size = ss['plot_par']["max_clu_size"])



#--------------------------------
# streamlit interactive frontend starts here 

a00, a01 = st.columns([0.56, 0.4])

# select DBSCAN params 
with a00:
    with st.form("my_form_1"):
        c00, c01, c02 = st.columns([0.4, 0.4, 0.2])
        with c00:
            ss['dbscan_params']["eps"]         = st.slider(label = "DBSCAN eps", min_value=0.05, max_value=3.0, value=ss['dbscan_params']["eps"], step=0.01,)
        with c01:
            ss['dbscan_params']["min_samples"] = st.slider(label = "DBSCAN min_samples", min_value=5, max_value=100, value=ss['dbscan_params']["min_samples"], step=1,)
        with c02:
            submitted_1 = st.form_submit_button("Submit")
        if submitted_1:
            st.rerun()

# select size of clusters to be displayed
with a01:
    with st.form("my_form_2"):
        c10, c11, c12 = st.columns([0.4, 0.15, 0.30])
        with c10:
            ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"] = st.slider(
                label = "Range of cluster size to plot", min_value=1, max_value=300, 
                value=(10, 200), step=1,)
        with c11:
            submitted_2 = st.form_submit_button("Submit")
        with c12: 
            with st.container(border=True) : 
                st.text('Nb clusters selected:')
                st.text(len(selected_clusters))
        if submitted_2:
            st.rerun()



if len(selected_clusters) <= 1:
    st.text("Not enough clusters: Try to reduce 'Eps' or 'Range of cluster size' ")
else:
    with st.container(border=True) : 
        selected_cluster_id = st.segmented_control(label = "Select a cluster ID (sorted smallest to largests)", options = selected_clusters )

    # selected_cluster_id = 6
    df_sel = df[df['cluster_id']==selected_cluster_id]
    selected_images_files = df_sel['file_name']
    #  show images 
    num_cols = 10
    grid = st.columns(num_cols)
    col = 0
    for ii, im_filname in enumerate(selected_images_files):
        try:
            with grid[col]:
                with st.container(border=True):
                    st.image(os.path.join(impath, im_filname)) # , caption=im_filname[0:10])
            col += 1
            if ii % num_cols == (num_cols-1):
                col = 0
            print('OK')    
        except:
            print('shit')   

with st.expander("Origin files of sounds"):
    if len(selected_images_files) > 0:
        all_files_in_cluster = selected_images_files.str.split('_segm_', expand=True).iloc[:,0]
        files_counts = all_files_in_cluster.value_counts().reset_index()

        nb_file_in_cluster   = len(all_files_in_cluster)
        nb_pieces_in_cluster = len(files_counts)
        st.text([nb_file_in_cluster, nb_pieces_in_cluster])

        files_counts.columns = ["File name", "Count"]
        st.dataframe(data = files_counts, hide_index=True, width = 1000, height = 500, column_order=("Count", "File name")) 


               




