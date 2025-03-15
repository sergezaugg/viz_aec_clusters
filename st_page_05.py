#--------------------             
# Author : Serge Zaugg
# Description : some info 
#--------------------

import streamlit as st

c00, c01  = st.columns([0.6, 0.4])
with c00:
    with st.container(border=True) : 
        st.header("References")
        
        st.markdown('''In a previous collaboration, I learned hands-on that reducing dimensionality before unsupervised clustering helps a lot.''')

        st.page_link("https://doi.org/10.1109/EFTF61992.2024.10722402", label=":red[D. Husmann; S. Zaugg; J. Morel : Detection and Analysis of Anthropogenic Patterns in a Phase-Stabilized Optical Fiber Network]")


        st.markdown('''A few interesting papers that inspired me''')
        
        st.page_link("https://doi.org/10.1016/j.aiig.2021.12.002", label=":red[Q. Kong et al. : Deep convolutional autoencoders as generic feature extractors in seismological applications]")

        st.page_link("https://doi.org/10.1371/journal.pone.0283396", label=":red[P. Best, S. Paris, H. Glotin, R. Marxer : Deep audio embeddings for vocalisation clustering]")

        st.page_link("https://doi.org/10.3389/frsen.2024.1429227", label=":red[A. Noble et al. : Unsupervised clustering reveals acoustic diversity and niche differentiation in pulsed calls from a coral reef ecosystem]")




    

        

        


