import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os 
print("Files in current directory:", os.listdir())

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers and trends")

df = pd.read_csv("metadata.csv")

df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample Data")
st.write(filtered.head())

year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications Over Time")
st.pyplot(fig)
