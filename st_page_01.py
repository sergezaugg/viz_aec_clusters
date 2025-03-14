#--------------------             
# Author : Serge Zaugg
# Description : Create datasets, train, assess performance and feature importance
#--------------------


import os
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
# from utils import make_dataset, fit_rf_get_metrics, reshape_df, make_scatter_plot
from streamlit import session_state as ss



# initialize session state 
if 'rfo_n_trees' not in ss:
    ss['rfo_n_trees'] = 30
if 'max_features' not in ss:
    ss['max_features'] = 1


#--------------------------------
# streamlit frontend starts here 


impath = "C:/xc_real_projects/da_examples/2"

grid = st.columns(15)
col = 0

for im_filname in os.listdir(impath)[0:8]:
    with grid[col]:
        st.image(os.path.join(impath, im_filname), caption='aaaaa')
    col += 1


