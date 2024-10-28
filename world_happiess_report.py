import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv("world_happiness_report.csv")  # Replace with your actual dataset filename
    return data

# Set up Streamlit app
st.title("World Happiness Report Analysis with Interactive Maps")
st.write("Explore global happiness metrics by country and region with interactive maps.")

# Load data
data = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
year = st.sidebar.selectbox("Select Year", sorted(data['Year'].unique(), reverse=True))
region = st.sidebar.multiselect("Select Region", data['Region'].unique())
country = st.sidebar.multiselect("Select Country", data['Country'].unique())

# Filter data based on sidebar selections
filtered_data = data[data['Year'] == year]
if region:
    filtered_data = filtered_data[filtered_data['Region'].isin(region)]
if country:
    filtered_data = filtered_data[filtered_data['Country'].isin(country)]

# 1. Choropleth Map: Global Happiness Score by Country
st.subheader("Global Happiness Score by Country")
fig_choropleth = px.choropleth(
    filtered_data,
    locations="Country",
    locationmode="country names",
    color="Happiness Score",
    hover_name="Country",
    title=f"Global Happiness Score for {year}",
    color_continuous_scale="Viridis",
    projection="natural earth"
)
fig_choropleth.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")
st.plotly_chart(fig_choropleth, use_container_width=True)

# 2. Bubble Map: Happiness Score with GDP per Capita
st.subheader("Bubble Map of Happiness Scores and GDP per Capita")
fig_bubble_map = px.scatter_geo(
    filtered_data,
    locations="Country",
    locationmode="country names",
    size="GDP per capita",
    color="Happiness Score",
    hover_name="Country",
    title=f"Happiness Score and GDP per Capita for {year}",
    size_max=30,
    color_continuous_scale="Plasma",
    projection="natural earth"
)
fig_bubble_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")
st.plotly_chart(fig_bubble_map, use_container_width=True)

# 3. Animated Choropleth Map: Happiness Score Over Time
st.subheader("Animated Map: Happiness Score Over Years")
fig_animated_map = px.choropleth(
    data,
    locations="Country",
    locationmode="country names",
    color="Happiness Score",
    hover_name="Country",
    animation_frame="Year",
    color_continuous_scale="YlGnBu",
    projection="natural earth",
    title="Happiness Score Over Time by Country"
)
fig_animated_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")
st.plotly_chart(fig_animated_map, use_container_width=True)

# 4. Map with Filtered Regions Only (if regions selected)
if region:
    st.subheader("Filtered Map: Happiness Scores for Selected Regions")
    fig_filtered_map = px.choropleth(
        filtered_data,
        locations="Country",
        locationmode="country names",
        color="Happiness Score",
        hover_name="Country",
        color_continuous_scale="sunsetdark",
        title=f"Happiness Score for Selected Regions in {year}"
    )
    fig_filtered_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="lightgray")
    st.plotly_chart(fig_filtered_map, use_container_width=True)

# Display raw data
st.subheader("Raw Data")
st.write(filtered_data)
