import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Add custom CSS for the pointer cursor


# Sample data (replace with your dataset)
df = pd.DataFrame({
    'Disease Name': ['Disease A', 'Disease B', 'Disease C'],
    'Population Affected': [1000, 2000, 1500],
    'Average Treatment Cost (USD)': [500, 800, 650],
    'Mortality Rate (%)': [5, 10, 7]
})

# Dropdown menu
chart_option = st.selectbox("Select a chart to display:", [
    "Bar Chart: Population Affected",
    "Box Plot: Treatment Cost",
    "Histogram: Mortality Rate"
])

# Display the selected chart
if chart_option == "Bar Chart: Population Affected":
    st.subheader("Bar Chart: Population Affected")
    fig, ax = plt.subplots()
    df.groupby('Disease Name')['Population Affected'].sum().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title("Total Population Affected by Disease")
    ax.set_xlabel("Disease Name")
    ax.set_ylabel("Population Affected")
    st.pyplot(fig)

elif chart_option == "Box Plot: Treatment Cost":
    st.subheader("Box Plot: Treatment Cost")
    fig, ax = plt.subplots()
    sns.boxplot(x='Disease Name', y='Average Treatment Cost (USD)', data=df, ax=ax, palette='Set2')
    ax.set_title("Comparison of Treatment Costs by Disease")
    st.pyplot(fig)

elif chart_option == "Histogram: Mortality Rate":
    st.subheader("Histogram: Mortality Rate")
    fig, ax = plt.subplots()
    ax.hist(df['Mortality Rate (%)'], bins=5, color='orange', edgecolor='black', alpha=0.7)
    ax.set_title("Distribution of Mortality Rate")
    ax.set_xlabel("Mortality Rate (%)")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
