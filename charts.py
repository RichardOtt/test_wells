import altair as alt
from vega_datasets import data

def map_wells(well_df):
    states = alt.topo_feature(data.us_10m.url, feature='states')

    # US states background
    background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).properties(
        width=500,
        height=300
    ).project('albersUsa')

    well_points = (alt.Chart(well_df)
    .mark_circle().encode(
        longitude='longitude:Q',
        latitude='latitude:Q',
        color=alt.Color('gradient:Q', scale=alt.Scale(scheme='yelloworangered')),
        tooltip=[alt.Tooltip('depth:Q', title='Depth (m)'), 
                 alt.Tooltip('gradient:Q', title='Gradient (C/m)', format='0.2f')]
    ).properties(
        title='Well locations'
    ))
    chart = background + well_points
    
    return chart