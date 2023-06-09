import streamlit as st
import numpy as np
import pandas as pd
import plost


@st.cache
def get_datasets():
    N = 3600
    M = 3000
    rand = pd.DataFrame()
    rand['a'] = np.arange(N)
    rand['b'] = np.random.rand(M)
    

    return dict(
        rand=rand,
    )

datasets = get_datasets()


"### Fynd"

#with st.expander('Documentation'):
#    st.write(plost.area_chart)
""

with st.echo():
    plost.area_chart(
        data=datasets['rand'],
        x='a',
        y='b',
    legend='left')

""
