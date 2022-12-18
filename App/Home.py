import streamlit as st
import streamlit.components.v1 as com
import numpy as np
import pandas as pd

st.set_page_config(page_title = "BIOMOLECULE PREDICTION SYSTEM", page_icon = "🌍", layout = "wide", initial_sidebar_state = "collapsed", menu_items = None)


htmlFile = open("Pages/home copy.html", 'r', encoding = 'utf-8')
source_code = htmlFile.read()
com.html(source_code, height = 1000 )