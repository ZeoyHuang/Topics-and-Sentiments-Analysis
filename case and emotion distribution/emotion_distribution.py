# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:04:23 2023

@author: Hzy
"""

import altair as alt
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('motion.csv')

# Histogram of the motion value according to the time
histogram = alt.Chart(df).mark_bar().encode(
    x='time:T',
    y='count():Q',  # Counting the number of records for the histogram
    color='location:N'  # N indicates nominal (categorical) data
)

# Scatterplot with different colored dots for different districts
scatterplot = alt.Chart(df).mark_circle().encode(
    x='time:T',
    y='motion value:Q',
    color='location:N'
)

# Save the charts to an HTML file
histogram.save('emotion_histogram.html')
scatterplot.save('emotion_scatterplot.html')