from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import tw22ok_calc
import tw22ok_util

gpx_file = None

st.write("""
# Welcome to Streamlit!

Please select a GPX file to be loaded
""")

gpx_file = st.file_uploader(label="Upload a GPX file",type=['gpx'])

if gpx_file is not None:
    gpx_data = tw22ok_calc.load_reference_data(gpx_file)

    gpx_chart_base = alt.Chart(gpx_data).encode(
        x=alt.X(
            field="distance_sum", type="quantitative", 
            axis=alt.Axis(labels=False,grid=False,title=None,ticks=False,domainOpacity=0)
            ),
    )

    gpx_chart_elevation = gpx_chart_base.mark_area(opacity=0.5, color="grey").encode(
        y=alt.Y(
            field="elevation", type="quantitative", 
            axis=alt.Axis(labels=False,grid=False,title=None,ticks=False,domainOpacity=0),
            scale=alt.Scale(
                domain=[gpx_data["elevation"].min().values[0], 
                gpx_data["elevation"].max().values[0]])
            ),
    )

    gpx_chart_pace = gpx_chart_base.mark_line(opacity=0.7, color='grey').encode(
        y=alt.Y(
            field="pace_segment", type="quantitative", 
            axis=alt.Axis(labels=False,grid=False,title=None,ticks=False,domainOpacity=0),
            #scale=alt.Scale(domain=[0, gpx_data["pace_segment"].max().values[0]])
            ),
    )

    c = alt.layer(gpx_chart_elevation, gpx_chart_pace).resolve_scale(
        y = 'independent'
    ).configure_view(
        strokeOpacity=0
    )

    st.altair_chart(c, use_container_width=True)
else:
    st.write("No file selected")