import streamlit as st
import numpy as np
import pandas as pd
import plost


"""
# 🍅 Plost

@st.cache
def get_datasets():
    N = 50
    rand = pd.DataFrame()
    rand['a'] = np.arange(N)
    rand['b'] = np.random.rand(N)
    rand['c'] = np.random.rand(N)

    return dict(
        rand=rand,
    )

datasets = get_datasets()


"### area_chart()"

with st.expander('Documentation'):
    st.write(plost.area_chart)
""

with st.echo():
    plost.area_chart(
        data=datasets['rand'],
        x='a',
        y=('b', 'c'),
    legend='left')

""

with st.echo():
    plost.area_chart(
        data=datasets['rand'],
        x='a',
        y=('b', 'c'),
        opacity=0.5,
        stack=False)

""

with st.echo():
    plost.area_chart(
        data=datasets['rand'],
        x='a',
        y=('b', 'c'),
        stack='normalize')
    
""
