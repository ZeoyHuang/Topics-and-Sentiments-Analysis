# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:03:26 2023

@author: Hzy
"""

import altair as alt
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('case.csv')

# Create a line chart
chart = alt.Chart(df).mark_line().encode(
    x='Date:T',  # T indicates temporal (time-based) data
    y='Number of New Confirmed Cases:Q'  # Q indicates a quantitative field
)

# Save the chart to an HTML file
chart.save('case_increase.html')