#----------------------
#
#
#----------------------

import numpy as np
import pandas as pd
import plotly.express as px
import os 
from sklearn.cluster import DBSCAN
from PIL import Image
from sklearn.utils import shuffle
from utils import apply_dbscan_clustering, load_reduced_features


impath = "spectrogram_images"

path_features = os.path.join("extracted_features/features_reduced.npz")

feat, filnam = load_reduced_features(path = path_features)

df = apply_dbscan_clustering(x = feat, labels = filnam, eps = 0.2, min_samples = 10)

df.shape

all_availabel_clusters = df['cluster_id'].unique()












