import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from plotly.figure_factory import create_table
from wordcloud import WordCloud

# Initialize Plotly in Streamlit
st.set_option('deprecation.showPyplotGlobalUse', False)

# Title
st.title("COVID-19 Data Analysis and Visualization")

# Loading datasets
@st.cache_data
def load_data():
    dataset1 = pd.read_csv("covid.csv")
    dataset2 = pd.read_csv("covid_grouped.csv")
    dataset3 = pd.read_csv("coviddeath.csv")
    return dataset1, dataset2, dataset3

dataset1, dataset2, dataset3 = load_data()

# Display datasets info
st.header("Dataset Information")
st.write("### Dataset1: COVID-19 Overall Data")
st.write(dataset1.head())
st.write("Shape:", dataset1.shape)
st.write("Size:", dataset1.size)
st.write("Info:")
st.write(dataset1.info())

st.write("### Dataset2: COVID-19 Grouped Data")
st.write(dataset2.head())
st.write("Shape:", dataset2.shape)
st.write("Size:", dataset2.size)
st.write("Info:")
st.write(dataset2.info())

st.write("### Dataset3: COVID-19 Death Data")
st.write(dataset3.head())
st.write("Shape:", dataset3.shape)
st.write("Size:", dataset3.size)
st.write("Info:")
st.write(dataset3.info())

# Drop unnecessary columns from dataset1
dataset1 = dataset1.drop(['NewCases', 'NewDeaths', 'NewRecovered'], axis=1)

# Sample data
st.header("Sample Data")
st.write(dataset1.sample(5))

# Table Visualization
st.header("Table Visualization")
colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
table = create_table(dataset1.head(15), colorscale=colorscale)
st.plotly_chart(table)

# Bar charts
st.header("Bar Charts")
fig1 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalCases', height=500, hover_data=['Country/Region', 'Continent'])
st.plotly_chart(fig1)
fig2 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalDeaths', height=500, hover_data=['Country/Region', 'Continent'])
st.plotly_chart(fig2)
fig3 = px.bar(dataset1.head(15), x='Country/Region', y='TotalCases', color='TotalTests', height=500, hover_data=['Country/Region', 'Continent'])
st.plotly_chart(fig3)
fig4 = px.bar(dataset1.head(15), x='TotalTests', y='Country/Region', color='TotalTests', orientation='h', height=500, hover_data=['Country/Region', 'Continent'])
st.plotly_chart(fig4)
fig5 = px.bar(dataset1.head(15), x='TotalTests', y='Continent', color='TotalTests', orientation='h', height=500, hover_data=['Country/Region', 'Continent'])
st.plotly_chart(fig5)

# Scatter plots
st.header("Scatter Plots")
fig6 = px.scatter(dataset1, x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80)
st.plotly_chart(fig6)
fig7 = px.scatter(dataset1.head(57), x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True)
st.plotly_chart(fig7)
fig8 = px.scatter(dataset1.head(54), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80)
st.plotly_chart(fig8)
fig9 = px.scatter(dataset1.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True)
st.plotly_chart(fig9)
fig10 = px.scatter(dataset1.head(100), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80)
st.plotly_chart(fig10)
fig11 = px.scatter(dataset1.head(30), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, log_y=True)
st.plotly_chart(fig11)
fig12 = px.scatter(dataset1.head(10), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80)
st.plotly_chart(fig12)
fig13 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='Tests/1M pop', size_max=80)
st.plotly_chart(fig13)
fig14 = px.scatter(dataset1.head(30), x='Country/Region', y='Tests/1M pop', hover_data=['Country/Region', 'Continent'], color='Tests/1M pop', size='Tests/1M pop', size_max=80)
st.plotly_chart(fig14)
fig15 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80)
st.plotly_chart(fig15)
fig16 = px.scatter(dataset1.head(30), x='TotalCases', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_x=True, log_y=True)
st.plotly_chart(fig16)

# Choropleth maps
st.header("Choropleth Maps")
fig17 = px.choropleth(dataset2, locations='iso_alpha', color='Confirmed', hover_name='Country/Region', color_continuous_scale='Blues', animation_frame='Date')
st.plotly_chart(fig17)
fig18 = px.choropleth(dataset2, locations='iso_alpha', color='Deaths', hover_name='Country/Region', color_continuous_scale='Viridis', animation_frame='Date')
st.plotly_chart(fig18)
fig19 = px.choropleth(dataset2, locations='iso_alpha', color='Recovered', hover_name='Country/Region', color_continuous_scale='RdYlGn', projection='natural earth', animation_frame='Date')
st.plotly_chart(fig19)

# Bar charts for WHO region
fig20 = px.bar(dataset2, x="WHO Region", y="Confirmed", color="WHO Region", animation_frame="Date", hover_name="Country/Region")
st.plotly_chart(fig20)

# US Data Visualizations
st.header("US Data Visualizations")
df_US = dataset2.loc[dataset2["Country/Region"] == "US"]
fig21 = px.bar(df_US, x="Date", y="Confirmed", color="Confirmed", height=400)
st.plotly_chart(fig21)
fig22 = px.bar(df_US, x="Date", y="Recovered", color="Recovered", height=400)
st.plotly_chart(fig22)
fig23 = px.line(df_US, x="Date", y="Recovered", height=400)
st.plotly_chart(fig23)
fig24 = px.line(df_US, x="Date", y="Deaths", height=400)
st.plotly_chart(fig24)
fig25 = px.line(df_US, x="Date", y="Confirmed", height=400)
st.plotly_chart(fig25)
fig26 = px.line(df_US, x="Date", y="New cases", height=400)
st.plotly_chart(fig26)
fig27 = px.bar(df_US, x="Date", y="New cases", height=400)
st.plotly_chart(fig27)
fig28 = px.scatter(df_US, x="Confirmed", y="Deaths", height=400)
st.plotly_chart(fig28)

# WordCloud visualizations
st.header("WordCloud Visualization")
sentences = ' '.join(dataset3["Condition"].tolist())
plt.figure(figsize=(10, 10))
plt.imshow(WordCloud().generate(sentences), interpolation='bilinear')
plt.axis('off')
st.pyplot()

column_to_string = ' '.join(dataset3["Condition Group"].tolist())
plt.figure(figsize=(10, 10))
plt.imshow(WordCloud().generate(column_to_string), interpolation='bilinear')
plt.axis('off')
st.pyplot()
