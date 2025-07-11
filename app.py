import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Malaysia Economy Dashboard 🇲🇾")

# Dataset selector
dataset = st.selectbox("Choose dataset to explore:", ["CPI", "GDP", "Unemployment"])

# Load based on selection
if dataset == "CPI":
    df = pd.read_csv("CPI.csv")
elif dataset == "GDP":
    df = pd.read_csv("GDP.csv")
else:
    df = pd.read_csv("Unemployment.csv")

st.subheader(f"Preview of {dataset} data")
st.write(df.head())

# Optional filter - example: by year
if "Year" in df.columns:
    year = st.selectbox("Filter by Year", df["Year"].unique())
    filtered_df = df[df["Year"] == year]
else:
    filtered_df = df

# Plot
st.subheader(f"{dataset} Trend")
fig, ax = plt.subplots()
if "Month" in filtered_df.columns and "Value" in filtered_df.columns:
    ax.plot(filtered_df["Month"], filtered_df["Value"], marker='o')
    ax.set_xlabel("Month")
    ax.set_ylabel("Value")
    ax.set_title(f"{dataset} over Time")
    st.pyplot(fig)
else:
    st.write("Data does not have Month/Value columns for plotting.")
