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
