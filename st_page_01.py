#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train, assess performance and feature importance
#--------------------

import os
import streamlit as st
from streamlit import session_state as ss
import numpy as np
from utils import apply_dbscan_clustering, load_reduced_features, load_meta_data, constrain_cluster_size, reduce_dim_and_standardize


# initialize session state 
if 'dbscan_params' not in ss:
    ss['dbscan_params'] = {
        'eps' : 0.30,
        'min_samples' : 10,
        }

if 'umap_params' not in ss:
    ss['umap_params'] = {
        'n_dims_red' : 32,
        'n_neighbors' : 10,
        }

if 'plot_par' not in ss:
    ss['plot_par'] = {
        'min_clu_size' : 10,
        'max_clu_size' : 100,
        }
    
if 'init_message' not in ss:
    st.text('On startup UMAP is computed, this can take a minute or two ')
    ss['init_message'] = "available"



# define paths 
impath = "spectrogram_images"
path_features = os.path.join("extracted_features/features_semi_reduced.npz")
path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")


#--------------------------------
# computational block 
df_meta              = load_meta_data(path = path_meta_data)
feat_semi, filnam    = load_reduced_features(path = path_features)
feat, umap_exec_time = reduce_dim_and_standardize(X = feat_semi, n_neighbors = ss['umap_params']["n_neighbors"], n_dims_red = ss['umap_params']["n_dims_red"] )
df, dbscan_exec_time = apply_dbscan_clustering(x = feat, labels = filnam, eps = ss['dbscan_params']["eps"], min_samples = ss['dbscan_params']["min_samples"])
selected_clusters    = constrain_cluster_size(df_clusters = df, min_size = ss['plot_par']["min_clu_size"], max_size = ss['plot_par']["max_clu_size"])


#--------------------------------
# streamlit interactive frontend starts here 

a99, a00, a01 = st.columns([0.3, 0.3, 0.2])

# select UMAP params 
with a99:
    with st.form("my_form_0"):
        c00, c02 = st.columns([0.4, 0.2])
        with c00:
            # ss['umap_params']["n_dims_red"]  =        st.slider(label = "UMAP target dim",  min_value=2, max_value=128,  value = ss['umap_params']["n_dims_red"],  step=2,)
            ss['umap_params']["n_dims_red"]  = st.select_slider(label = "UMAP target dim", options=[2,4,8,16,32,64,128], value = ss['umap_params']["n_dims_red"],)
            ss['umap_params']["n_neighbors"] = st.slider(label = "UMAP n_neighbors", min_value=2, max_value=100, value=ss['umap_params']["n_neighbors"], step=1,)
        with c02:
            submitted_0 = st.form_submit_button("Trigger UMAP", type = "primary")
            st.text('This can take a few minutes on first run for any set of params')
            st.text('Exec ' + str(umap_exec_time) + ' sec')
        if submitted_0:
            st.rerun()

# select DBSCAN params 
with a00:
    with st.form("my_form_1"):
        c00, c02 = st.columns([0.4, 0.2])
        with c00:
            ss['dbscan_params']["eps"]         = st.slider(label = "DBSCAN eps", min_value=0.05, max_value=3.0, value=ss['dbscan_params']["eps"], step=0.01,)
            ss['dbscan_params']["min_samples"] = st.slider(label = "DBSCAN min_samples", min_value=2, max_value=100, value=ss['dbscan_params']["min_samples"], step=1,)
        with c02:
            submitted_1 = st.form_submit_button("Trigger DBSCAN", type = "primary")
            st.text('This can take several seconds on first run for any set of params')
            st.text('Exec ' + str(dbscan_exec_time) + ' sec')
        if submitted_1:
            st.rerun()

# select size of clusters to be displayed
with a01:
    with st.form("my_form_2"):
        c10, c11 = st.columns([0.4, 0.20])
        with c10:
            ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"] = st.slider(
                label = "Range of cluster size to plot", 
                min_value=1, max_value=200, 
                value = (ss['plot_par']["min_clu_size"], ss['plot_par']["max_clu_size"]) ,# (10, 200), 
                step = 1,)
            # aaa = st.slider(label = "aaaa", min_value=2, max_value=100, value=5, step=1, disabled = True)
            st.text('Nb clusters: ' + str(len(selected_clusters)))
            # st.text('')
            st.subheader('')
        with c11:
            submitted_2 = st.form_submit_button("Submit", type = "primary")
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

        

      


               




