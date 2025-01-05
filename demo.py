import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y)

# Display the plot in Streamlit
st.pyplot(fig)
