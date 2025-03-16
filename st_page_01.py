#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train, assess performance and feature importance
#--------------------

import os
import streamlit as st
from streamlit import session_state as ss
import numpy as np
from utils import apply_dbscan_clustering, load_reduced_features, load_meta_data, constrain_cluster_size

# initialize session state 
if 'dbscan_params' not in ss:
    ss['dbscan_params'] = {
        'eps' : 0.30,
        'min_samples' : 10,
        }
     
if 'plot_par' not in ss:
    ss['plot_par'] = {
        'min_clu_size' : 10,
        'max_clu_size' : 100,
        }

# define paths 
impath = "spectrogram_images"
path_features = os.path.join("extracted_features/featuresreduced.npz")
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
            ss['dbscan_params']["min_samples"] = st.slider(label = "DBSCAN min_samples", min_value=2, max_value=100, value=ss['dbscan_params']["min_samples"], step=1,)
        with c02:
            submitted_1 = st.form_submit_button("Trigger DBSCAN computation")
        if submitted_1:
            st.rerun()

# select size of clusters to be displayed
with a01:
    with st.form("my_form_2"):
        c10, c11, c12 = st.columns([0.4, 0.15, 0.30])
        with c10:
            ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"] = st.slider(
                label = "Range of cluster size to plot", 
                min_value=1, max_value=200, 
                value = (ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"]) ,# (10, 200), 
                step = 1,)
        with c11:
            submitted_2 = st.form_submit_button("Submit")
        with c12: 
            with st.container(border=True) : 
                st.text('Nb clusters: ' + str(len(selected_clusters)))
        if submitted_2:
            st.rerun()
            



if len(selected_clusters) <= 1:
    st.text("Not enough clusters: Try to change 'eps' or 'min_sample' or 'Range of cluster size' ")
else:
    selected_cluster_id = st.segmented_control(label = "Select a cluster ID (sorted smallest to largests)", options = selected_clusters )
    df_sel = df[df['cluster_id']==selected_cluster_id]
    selected_images_files = df_sel['file_name']
    # sort to have clips from same image next by each other 
    selected_images_files = selected_images_files.sort_values(ascending=True)
    if len(selected_images_files) > 0:

        # get list of XC id alone (same order as selected_images_files)
        all_files_in_cluster = ('XC' + selected_images_files.str.extract(r'_XC(.{,6})'))
        files_counts = all_files_in_cluster.value_counts().reset_index()

        # add info 
        with st.container(border=True) : 
            x00, x01 = st.columns([0.56, 0.4])    
            with x00:
                nb_file_in_cluster   = len(files_counts )
                nb_pieces_in_cluster = len(selected_images_files)
                st.text(  'Cluster content: ' + str(nb_pieces_in_cluster) + ' clips from ' + str(nb_file_in_cluster) + ' separate mp3 files'   ) 
            with x01:
                with st.expander("Detail table (click to expand)"):
                    files_counts.columns = ["File name", "Count"]
                    st.dataframe(data = files_counts, hide_index=True, width = 300, column_order=("Count", "File name")) 
                    
        # show images 
        with st.container(border=True) : 
            num_cols = 10
            grid = st.columns(num_cols)
            col = 0
            for ii, im_filname in enumerate(selected_images_files):
                try:
                    with grid[col]:
                        with st.container(border=True):
                            st.image(os.path.join(impath, im_filname), use_container_width=True, caption= 'From  ' + all_files_in_cluster.iloc[ii].values)
                    col += 1
                    if ii % num_cols == (num_cols-1):
                        col = 0
                    print('OK')    
                except:
                    print('shit')   

        

      


               




