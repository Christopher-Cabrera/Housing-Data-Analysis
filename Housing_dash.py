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
text1 = "Business Interpretation: The market shows a large concentration of lower-mid priced properties around the $100,000-200,000 range, with a long right tail towards a small selection of luxury properties.\n\nAnalytical Implication: The right skewed distribution suggests that price differences should be analyzed using averages only after investigating extreme outliers to account for high value properties that could disrupt the mean, While the representation of varied purchasing prevalence and possible market inflation through the displayed color variation implies that differences in prices should only be compared to other sales in the same year in order to draw accurate insights about market growth."
text2 = "Business interpretation: The scatter plot shows a clear postitive correlation between square footage and sale price; however, the color variation of overall quality suggests significantly differently sales prices among properties of similar size. This means that while living space is clearly one of the largest factors in determining price, other components such as overall quality can greatly alter the value of a house from its baseline size-price correlation.\n\nAnalytical insight: This variance in price distribution among similarly sized properties is extremely important to the firm for recognizing that a seemingly good deal on a potential investment for a large scale property must first be thorougly vetted in regards to other key variables such as quality and neighborhood. This ensures that investment capital will not be lost on trap properties due to a seemingly strong correlation implying that a property is undervalued based on one characteristic."
text3 = "Business Interpretation: This chart displays vast disparities between average property prices in different neighborhoods, which could potentially explain some of the previously explore price variance.\n\n Analytical Implication: Market wide averages may be concealing important individual differences. The highest averages appear in neighborhoods such as Northridge, Northridge Heights, and Stone Brook. It is important that further investigation into these areas is completed before the investment of any capital to understand how luxury factors such as maitenance, taxes, or community requirements could contribute to substantially higher entry costs on a property in these neighborhoods."
st.plotly_chart(fig1, use_container_width=True)
st.text(text1, text_alignment="justify")
st.plotly_chart(fig2, use_container_width=True)
st.text(text2, text_alignment="justify")
st.plotly_chart(fig3, use_container_width=True)
st.text(text3, text_alignment="justify")


