import streamlit as st
import numpy as np
import pandas as pd
import plost

st.set_page_config(page_title='Plost', page_icon=':tomato:')

"""
# Fynd


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

"---"

"### bar_chart()"

with st.expander('Documentation'):
    st.write(plost.bar_chart)
""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value='q2')

""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value='q2',
        direction='horizontal')

""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value=['q2', 'q3'],
    )

""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value=['q2', 'q3'],
        stack='normalize')

""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value=['q2', 'q3'],
        group=True)
""

with st.echo():
    plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value=['q2', 'q3'],
        group='value',
        color='company',
        legend=None,
    )

"---"

"### pie_chart()"

with st.expander('Documentation'):
    st.write(plost.pie_chart)
""

with st.echo():
    plost.pie_chart(
        data=datasets['stocks'],
        theta='q2',
        color='company')

"---"

"### donut_chart()"

with st.expander('Documentation'):
    st.write(plost.donut_chart)
""

with st.echo():
    plost.donut_chart(
        data=datasets['stocks'],
        theta='q2',
        color='company')

"---"

"### scatter_chart()"

with st.expander('Documentation'):
    st.write(plost.scatter_chart)
""

with st.echo():
    plost.scatter_chart(
        data=datasets['randn'],
        x='a',
        y='b',
        size='c',
        opacity='b',
        height=500)

""

with st.echo():
    plost.scatter_chart(
        data=datasets['randn'],
        x='a',
        y=['b', 'c'],
        size='d',
        height=500)

"---"

"### event_chart()"

with st.expander('Documentation'):
    st.write(plost.event_chart)
""

with st.echo():
    plost.event_chart(
        data=datasets['events'],
        x='time_delta_s',
        y='servers')

""

with st.echo():
    plost.event_chart(
        data=datasets['events'],
        x='time_delta_s',
        y='servers',
        color='servers',
        legend=None)

"""
---
## Histograms
"""

"### hist()"

with st.expander('Documentation'):
    st.write(plost.hist)
""

with st.echo():
    plost.hist(
        data=datasets['randn'],
        x='a',
        aggregate='count')

""

with st.echo():
    plost.hist(
        data=datasets['seattle_weather'],
        x='date',
        y='temp_max',
        aggregate='median')

"---"

"### time_hist()"

with st.expander('Documentation'):
    st.write(plost.time_hist)
""

with st.echo():
    plost.time_hist(
        data=datasets['seattle_weather'],
        date='date',
        x_unit='week',
        y_unit='day',
        color='temp_max',
        aggregate='median',
        legend=None,
    )

"---"

"### xy_hist()"

with st.expander('Documentation'):
    st.write(plost.xy_hist)
""

with st.echo():
    plost.xy_hist(
        data=datasets['randn'],
        x='a',
        y='b',
    )

"---"

with st.echo():
    plost.xy_hist(
        data=datasets['randn'],
        x='a',
        y='b',
        x_bin=dict(maxbins=20),
        y_bin=dict(maxbins=20),
        height=400,
    )

"---"

"""
Woah, double histogram :rainbow:
"""

"### scatter_hist()"

with st.expander('Documentation'):
    st.write(plost.scatter_hist)
""

with st.echo():
    plost.scatter_hist(
        data=datasets['randn'],
        x='a',
        y='b',
        size='c',
        color='c',
        opacity=0.5,
        aggregate='count',
        width=500,
        height=500)

"""
---
# Advanced features
## Vega-Lite encoding dicts
You can use [Vega-Lite encoding dicts](https://vega.github.io/vega-lite/docs/encoding.html) for
the `x`, `y`, `color`, `size`, and `opacity` arguments to do all sorts of fun things. For example,
the chart below is computing the mean of the `y` values, grouped by month.
"""

with st.echo():
    plost.area_chart(
        data=datasets['seattle_weather'],
        x=dict(field='date', timeUnit='month'),
        y=dict(field='temp_max', aggregate='mean'),
        color='weather',
    )

"""
Plost also supports [Altair-style
shorthands](https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types), like
"column_name:T" for temporal.
"""

"""
---
## Annotations
Use `x_annot` and `y_annot` to add vertical or horizontal lines with annotations:
"""

with st.echo():
    plost.area_chart(
        data=datasets['rand'],
        x='a',
        y=('b', 'c'),
        x_annot={
            12: "This is when things became random",
            33: "Actually they were always random. Back to normal now.",
        },
    )


"""
---
## Minimaps
You can add a minimap to many of the charts above my simply passing `pan_zoom='minimap'`.
"""

with st.echo():
    plost.line_chart(
        data=datasets['sp500'],
        x='date',
        y='price',
        width=500,
        pan_zoom='minimap')

"---"

with st.echo():
    plost.area_chart(
        data=datasets['sp500'],
        x='date',
        y='price',
        width=500,
        pan_zoom='minimap')

"---"

with st.echo():
    plost.scatter_chart(
        data=datasets['randn'],
        x='a',
        y='b',
        size='c',
        opacity='b',
        width=500,
        height=500,
        pan_zoom='minimap')

"---"

with st.echo():
    plost.bar_chart(
        data=datasets['pageviews'],
        bar='pagenum',
        value='pageviews',
        width=500,
        pan_zoom='minimap')

"---"

with st.echo():
    plost.bar_chart(
        data=datasets['pageviews'],
        bar='pagenum',
        value='pageviews',
        direction='horizontal',
        width=500,
        height=500,
        pan_zoom='minimap')

""
""
""
""
"🍅"
