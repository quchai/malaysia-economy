import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🇲🇾 Malaysia National Government Debt (RM Billion)")

df = pd.read_csv("debt_malaysia_rm.csv")

st.subheader("Raw Data")
st.write(df)

fig, ax1 = plt.subplots()
ax1.plot(df["Year"], df["Debt_RMbn"], color="blue", marker='o', label="Debt (RM bn)")
ax1.set_xlabel("Year")
ax1.set_ylabel("Debt (RM bn)", color="blue")

ax2 = ax1.twinx()
ax2.plot(df["Year"], df["Debt_pct_GDP"], color="red", marker='x', label="% of GDP")
ax2.set_ylabel("% of GDP", color="red")

fig.tight_layout()
st.pyplot(fig)
