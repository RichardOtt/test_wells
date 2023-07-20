import streamlit as st
import pandas as pd
import altair as alt
from database import get_wells
from charts import map_wells

st.set_page_config("Wells for geothermal energy")

st.title("Abandonded Wells")
st.text("An interactive map of abandoned wells that can be used for geothermal energy")

st.sidebar.title("Select well parameters")
# must all be same type - all int, all float, etc in a given box
depth = st.sidebar.number_input("Minimum depth (m)", min_value=0, value=500)
# default format only prints two decimal digits, but it _is_ taking the smaller values
gradient = st.sidebar.number_input("Minimum thermal gradient (°C/m)", min_value=0.0, value=0.05, step=0.001, format='%0.4f')

# Get wells data, placeholder
wells = get_wells(depth, gradient)
well_df = pd.DataFrame(wells, columns=['latitude', 'longitude', 'depth', 'gradient']).dropna()

chart = map_wells(well_df)

st.altair_chart(chart)