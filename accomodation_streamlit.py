import streamlit as st
import pandas as pd
import plotly.express as px
import datetime


st.write("""
# Impact of Covid-19 on Japanese Economy
""")



acco = pd.read_csv("accomodation_processed.tsv", sep="\t",  parse_dates=True)

#acco["time"] = pd.to_datetime(acco["time"]).apply(lambda x: x.strftime('%Y-%m')) 
acco["time"] = pd.to_datetime(acco["time"])
#st.write(acco["time"].min().split("-")[0])

#col1, col2 = st.beta_columns((2, 10))


locations_chosen = ["Japan"]

location_expander = st.beta_expander("Options:")

with location_expander:
    "Select Prefecture(s)"
    locations_chosen = st.multiselect('Prefecture', sorted(acco["location"].unique()), default=sorted(acco["location"].unique())[0])
#acco_time_slice = st.sidebar.slider("Time", min_value=int(acco["time"].min().split("-")[0]), max_value=int(acco["time"].max().split("-")[0]), value=None, step=None, format=None)



df = acco[acco["location"].isin(locations_chosen)]



if not df.empty:
    fig = px.line(df, x="time", y = "accomodations", color = "location", title = "Accomadation in Japan from 2007-2020")
    st.plotly_chart(fig, use_container_width=True)
