import streamlit as st
import pandas as pd
import plotly.express as px
from processing import load_all_products  # Make sure this returns a DataFrame

# Load all products
df = load_all_products()

st.set_page_config(page_title="Quick Commerce Price Comparison", layout="wide")
st.title("Quick Commerce Bread Price Comparison")

# Price Comparison Table
st.header("Price Comparison Table")
price_table = df.pivot_table(
    index=['product_name', 'brand'],
    columns='platform',
    values='price_rupees'
).reset_index()
st.dataframe(price_table)

# Average Price per Brand per Platform
st.header("Average Price per Brand per Platform")
avg_price = df.groupby(['platform', 'brand'])['price_rupees'].mean().reset_index()
fig_avg_price = px.bar(
    avg_price,
    x='brand',
    y='price_rupees',
    color='platform',
    barmode='group',
    title='Average Price per Brand per Platform'
)
st.plotly_chart(fig_avg_price, use_container_width=True)

# Number of Products per Brand per Platform
st.header("Number of Products per Brand per Platform")
prod_count = df.groupby(['platform', 'brand']).size().reset_index(name='count')
fig_prod_count = px.bar(
    prod_count,
    x='brand',
    y='count',
    color='platform',
    barmode='group',
    title='Number of Products per Brand per Platform'
)
st.plotly_chart(fig_prod_count, use_container_width=True)

# Best Deals Count per Platform
st.header("Best Deals Count per Platform")
best_deals = df.loc[df.groupby('product_name')['price_rupees'].idxmin()]
best_deals_count = best_deals['platform'].value_counts().reset_index()
best_deals_count.columns = ['platform', 'best_deals_count']
fig_best_deals = px.bar(
    best_deals_count,
    x='platform',
    y='best_deals_count',
    color='platform',
    title='Number of Best Deals per Platform'
)
st.plotly_chart(fig_best_deals, use_container_width=True)

# Price Distribution per Platform
st.header("Price Distribution per Platform")
fig_price_dist = px.box(
    df,
    x='platform',
    y='price_rupees',
    color='platform',
    title='Price Distribution per Platform'
)
st.plotly_chart(fig_price_dist, use_container_width=True)

# Products Count per Platform
st.header("Products Count per Platform")
prod_per_platform = df['platform'].value_counts().reset_index()
prod_per_platform.columns = ['platform', 'product_count']
fig_prod_platform = px.bar(
    prod_per_platform,
    x='platform',
    y='product_count',
    color='platform',
    title='Total Number of Products per Platform'
)
st.plotly_chart(fig_prod_platform, use_container_width=True)
