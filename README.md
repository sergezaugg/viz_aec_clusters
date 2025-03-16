# CLUSTERING UNSELECTED BIO-ACOUSTIC RECORDINGS

**SUMMARY:**
* :construction:  Still under development :construction:
* Spectrogram clusters were obtained via auto-encoders, dimensionality reduction and unsupervised clustering.
* This page currently only features the last step, clustering with DBSCAN.   
* Once ready, this tool could automatically create pre-labelled dataset.
* This could speed-up the annotation of datasets to train supervised models.      

**DEPENDENCIES:**
* Developed under Python 3.12.8
* First make a venv, then:
* pip install -r requirements.txt
* pip install umap-learn

**USAGE:**
* Clone the repo
* go to the repo's root dir
* To start the Streamlit dashboard do ```streamlit run stmain.py```

**DATA LICENSE:**
* Please find details in ./license_xc_data/xeno_canto_files_list.csv






