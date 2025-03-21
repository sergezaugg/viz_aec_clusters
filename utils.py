#--------------------             
# Author : Serge Zaugg
# Description : Utility functions used by other scripts
#--------------------

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import time
import umap.umap_ as umap

@st.cache_resource
def load_meta_data(path):
    """
    """
    df_meta = pd.read_pickle(path)
    return(df_meta)


@st.cache_data
def load_reduced_features(path):
    """
    """
    data = np.load(file = path)
    feat = data['feat']
    filnam = data['imfiles']
    return(feat, filnam)


@st.cache_data
def apply_dbscan_clustering(x , labels, eps = 0.2, min_samples = 10):
    """
    """
    dbscan_start_time = time.time()
    # DBSCAN
    clu = DBSCAN(eps = eps, min_samples=min_samples, metric='euclidean', n_jobs = 8) 
    cluster_ids = clu.fit_predict(x)
    # pd.Series(cluster_ids).value_counts()[0:10]
    df = pd.DataFrame({
        'file_name' :labels,
        'cluster_id' :cluster_ids,
        })
    # get timing
    dbscan_end_time = time.time()
    dbscan_exec_time = np.round(dbscan_end_time - dbscan_start_time, 1)
    return(df, dbscan_exec_time)


@st.cache_data
def constrain_cluster_size(df_clusters, min_size, max_size):
    """
    """
    # select the cluster to display 
    list_by_clu_size = df_clusters['cluster_id'].value_counts(sort=True, ascending=True)
    sel_1 = list_by_clu_size >= min_size
    sel_2 = list_by_clu_size <= max_size
    sel_3 = np.logical_and(sel_1, sel_2)
    all_availabel_clusters = list_by_clu_size.index
    selected_clusters = all_availabel_clusters[sel_3]
    return(selected_clusters)


@st.cache_data
def reduce_dim_and_standardize(X, n_neighbors = 10, n_dims_red = 32):
    """
    """
    umap_start_time = time.time()
    # umap 
    reducer = umap.UMAP(
        n_neighbors = n_neighbors, 
        n_components = n_dims_red, 
        metric = 'euclidean',
        n_jobs = -1
        )
    # reducer.fit(X[0:25000])
    # X_trans = reducer.transform(X)
    X_trans = reducer.fit_transform(X)
    # standardize
    scaler = StandardScaler()
    scaler.fit(X_trans)
    X_scaled = scaler.transform(X_trans)
    # get timing
    umap_end_time = time.time()
    umap_exec_time = np.round(umap_end_time - umap_start_time, 1)
    return(X_scaled, umap_exec_time)


