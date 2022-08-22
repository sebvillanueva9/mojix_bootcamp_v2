import streamlit as st
import pandas as pd

st.title('Stock / Inventory Discrepancy')

st.header('Databases')

st.subheader('Expected database')
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
st.dataframe(df_expected)

st.subheader('Counted database')
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)
st.dataframe(df_counted)

st.markdown("---")

st.header('Plotting')

st.subheader('Expected products')
df1 = df_expected['Retail_Product_Level1Name'].value_counts()
st.bar_chart(df1)

st.subheader('Counted (Without duplicates) products')
st.write('The duplicates were removed in order to present the plot.')
df_counted_r = df_counted.drop_duplicates("RFID")
df2 = df_counted_r['Retail_Product_Level1Name'].value_counts()
st.bar_chart(df2)

st.write('The counted products case has one more bar that corresponds to "LAR-TEXTIL", suggesting that there is a difference between the products in each case.')

st.markdown("<h3 style='text-align: center;'>. . .</h3>", unsafe_allow_html=True)
st.caption('by Sebastián Villanueva')
