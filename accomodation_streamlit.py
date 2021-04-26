import streamlit as st
import pandas as pd
import plotly.express as px
import datetime


st.write("""
# Impact of Covid-19 on Japanese Economy
""")



acco = pd.read_csv("accomodation_processed.tsv", sep="\t",  parse_dates=True)
expenditure = pd.read_csv("expenditure.tsv", sep="\t")
vessel = pd.read_csv("vessels_melt.tsv", sep="\t")

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



df_acco = acco[acco["location"].isin(locations_chosen)]

if not df_acco.empty:
    fig = px.line(df_acco, x="time", y = "accomodations", color = "location", title = "Accomadation in Japan from 2007-2020")
    st.plotly_chart(fig, use_container_width=True)



### expenditure

cities_chosen = []

city_expander = st.beta_expander("Cities:")

with city_expander:
    "Select Cities"
    cities_chosen = st.multiselect('City', sorted(expenditure["city"].unique()), default=sorted(expenditure["city"].unique())[0])

variable_chosen = ""

variable_chosen = st.selectbox('Variables', sorted(expenditure["variable"].unique()))

df_expenditure = expenditure[(expenditure["city"].isin(cities_chosen)) & (expenditure["variable"] == variable_chosen)].sort_values("year")

st.write(variable_chosen)

if not df_expenditure.empty:
    #for v in variable_chosen:
    
    fig = px.line(df_expenditure, x="year", y = "value", color = "city", title = variable_chosen + " per household per month")
    fig.update_yaxes(title_text="Spending (Yen)")
    st.plotly_chart(fig, use_container_width=True)


### vessels

countries_chosen = []

country_expander = st.beta_expander("Countries:")

with country_expander:
    "Select Countries"
    countries_chosen = st.multiselect('Countries', sorted(vessel["country"].unique()), default=sorted(vessel["country"].unique())[0])

variable_chosen_2 = ""

variable_chosen_2 = st.selectbox('Variables', sorted(vessel["variable"].unique()))

df_vessel = vessel[(vessel["country"].isin(countries_chosen)) & (vessel["variable"] == variable_chosen_2)].sort_values("time")

st.write(variable_chosen_2)

if not df_vessel.empty:
    #for v in variable_chosen:
    
    fig = px.line(df_vessel, x="time", y = "value", color = "country", title = variable_chosen)
    #fig.update_yaxes(title_text="Spending (Yen)")
    st.plotly_chart(fig, use_container_width=True)