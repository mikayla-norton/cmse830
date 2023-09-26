import streamlit as st
import pandas as pd
import time

if "file" not in st.session_state:
    st.session_state["file"] = "not done"

col1, col2 = st.columns([1,2])
col1.markdown("# Welcome to my app! ")
col1.markdown(" Here is some info on the app")

def change_file_state():
    st.session_state["file"] = "done"

upload_file = col2.file_uploader("Upload data", on_change=change_file_state)

progress = col2.progress(0)

#col2.progress(0)
if st.session_state["file"] == "done":
    for pct_complete in range(100):
        time.sleep(0.05)
        progress.progress(pct_complete+1)
    col2.success("Data loaded successfully!")

col1.metric(label="Temperature", value="58 °F", delta="1 °F")

with st.expander("Click to learn about the data source for my midterm project"):
    st.write("Here is more on the Emissions Dataset:")
    st.write("This dataset provides an in-depth look into the global CO2 emissions at the country-level, allowing for a better understanding of how much each country contributes to the global cumulative human impact on climate. It contains information on total emissions as well as from coal, oil, gas, cement production and flaring, and other sources. The data also provides a breakdown of per capita CO2 emission per country - showing which countries are leading in pollution levels and identifying potential areas where reduction efforts should be concentrated. This dataset is essential for anyone who wants to get informed about their own environmental footprint or conduct research on international development trends")