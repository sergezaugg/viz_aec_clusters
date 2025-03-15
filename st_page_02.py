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


# define paths 
impath = "spectrogram_images"
path_features = os.path.join("extracted_features/features_reduced_2.npz")
path_meta_data = os.path.join("metadata/downloaded_data_meta.pkl")

df_meta = load_meta_data(path = path_meta_data)

st.divider()

st.dataframe(df_meta)

st.dataframe(df_meta['lic'].value_counts())
