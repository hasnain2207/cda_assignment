# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:58:33 2023

@author: Hasnain
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
st.set_page_config(layout="wide")

file1 = r'C:\Users\Lenovo\Desktop\Class 1 Python\Assignments\3rd Assignment\archive (1)\athlete_events.csv'
df1 = pd.read_csv(file1)

file2 = r'C:\Users\Lenovo\Desktop\Class 1 Python\Assignments\3rd Assignment\archive (1)\noc_regions.csv'
df2 = pd.read_csv(file2)
data = pd.merge(df1, df2)

data.isna().any()

data.info()
#df = data.drop(['notes'],axis=1)

total_participations = data['ID'].count()
gold_medals = data[data['Medal'] == 'Gold']
h = data['Medal'](gold_medals.count())

st.metric(label="Total Participations", value=total_participations)


curr_count = 100
inc_count = 10

curr_medals = 50
inc_medals = -4

country_count = 14
inc_count = 5
st.header('Olympic History Dashboard')
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric('Number of Olympians', curr_count, inc_count)
col2.metric('Participating Countries', country_count, inc_count)
col3.metric('Gold Medals', curr_medals, inc_medals)
col4.metric('Silver Medals', curr_medals, inc_medals)
col5.metric('Bronze Medals', curr_medals, inc_medals)
