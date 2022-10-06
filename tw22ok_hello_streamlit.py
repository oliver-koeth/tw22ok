from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.write("""
# Welcome to Streamlit!

This is a nice blend of markdown and Python
""")

if st.checkbox('Show result'):
    st.write(40+2)

