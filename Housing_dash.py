#Load dependencies
import pandas as pd 
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "iframe"
import numpy as np
import streamlit as st

#load CSV FILE
df = pd.read_csv("AmesHousing (1).csv")
print (df.head())
print(df.info())

# Price Distribution Analysis
fig1 = px.histogram(df, x="SalePrice", color="Yr Sold", hover_name="SalePrice", title="Ames Housing Sales")

#Size/Price Correlation 
fig2 = px.scatter(df, x="Gr Liv Area", y="SalePrice", color="Overall Qual", hover_data="Neighborhood", title="Correlation Between Square Footage/Overall Quality and Selling Price")

#Geographic Price Patterns
avg_price = df.groupby("Neighborhood", as_index=False)["SalePrice"].mean()
fig3 = px.bar(avg_price, x="Neighborhood", y= "SalePrice",hover_name="SalePrice", title= "Average Sale Price by Neighborhood")
#Display
st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)


