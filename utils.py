#--------------------             
# Author : Serge Zaugg
# Description : Utility functions used by main.py and stmain.py
#--------------------

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.cluster import DBSCAN


# @st.cache_data
@st.cache_resource
def load_meta_data(path):
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
    clu = DBSCAN(eps = eps, min_samples=min_samples, metric='euclidean', n_jobs = 4) 
    cluster_ids = clu.fit_predict(x)
    # pd.Series(cluster_ids).value_counts()[0:10]
    df = pd.DataFrame({
        'file_name' :labels,
        'cluster_id' :cluster_ids,
        })
    return(df)


@st.cache_data
def constrain_cluster_size(df_clusters, min_size, max_size):
    """
    """
    # select the cluster to display 
    sel_1 = df_clusters['cluster_id'].value_counts() >= min_size
    sel_2 = df_clusters['cluster_id'].value_counts() <= max_size
    sel_3 = np.logical_and(sel_1, sel_2)
    all_availabel_clusters = df_clusters['cluster_id'].value_counts().index
    selected_clusters = all_availabel_clusters[sel_3]
    return(selected_clusters)
