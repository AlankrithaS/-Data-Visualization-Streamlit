import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import json

# Load GeoJSON data
india_states = json.load(open("states_india.geojson", "r"))

# Create state ID map
state_id_map = {}
for feature in india_states["features"]:
    feature["id"] = feature["properties"]["state_code"]
    state_id_map[feature["properties"]["st_nm"]] = feature["id"]

# Read the original CSV file into a DataFrame
df = pd.read_csv("data/india_census.csv")
# Display original DataFrame head
st.write('Original DataFrame (before preprocessing):')
st.write(df.head())


# Data preprocessing
df["Density"] = df["Density[a]"].apply(lambda x: int(x.split("/")[0].replace(",", "")))
df["id"] = df["State or union territory"].apply(lambda x: state_id_map.get(x, None))  # Using .get() to handle missing values
df["DensityScale"] = np.log10(df["Density"])
df["SexRatioScale"] = df["Sex ratio"] - 1000

# Read the original CSV file into a DataFrame
new_df = pd.read_csv("data/new_india_census.csv")

# # Display preprocessed DataFrame head
# st.write('Preprocessed DataFrame (after preprocessing):')
# st.write(new_df.head())

# Display preprocessed DataFrame head
st.write('Preprocessed DataFrame (after preprocessing):')

# Dropdown for selecting number of rows to display
num_rows = st.select_slider('Select number of rows to display:', options=[3, 5, 10, 20], value=3)

# Display selected number of rows
st.write(new_df.head(num_rows))

# Streamlit app
st.title('India Census Data Visualization')

# Dropdown for selecting column option
selected_column_option = st.selectbox('Select column option:', ['Sex ratio', 'DensityScale'])

# Dropdown for selecting color theme
color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
selected_color_theme = st.selectbox('Select a color theme', color_theme_list)

# Create choropleth map
fig = px.choropleth(
    df,
    locations="id",
    geojson=india_states,
    color=selected_column_option,  # Using selected column for visualization
    hover_name="State or union territory",
    hover_data=[selected_column_option, "DensityScale" if selected_column_option == "Sex ratio" else "Sex ratio"],
    color_continuous_scale=selected_color_theme,
    color_continuous_midpoint=0,
)
fig.update_geos(fitbounds="locations", visible=False)

# Add title to the map based on selected column
fig.update_layout(title=f'India Census Data Visualization: {selected_column_option}')

# Show choropleth map
st.plotly_chart(fig)
