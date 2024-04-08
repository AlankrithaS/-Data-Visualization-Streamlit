import os
import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import os
import pickle
from pathlib import Path
import pandas as pd


def load_file(path: str) -> pd.DataFrame:
    with open(path, "rb") as f:
        dataset = pickle.load(f)
        return dataset


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    all_datasets = [load_file(file) for file in Path("data/data1").iterdir()]
    df = pd.concat(all_datasets)
    return df

# here data frame is split into daily pickled pandas data frames
# So we have two methods to first read a data and another to stack all of the daily files into one consolidated file


st.write("# Chat with Credit Card Fraud Dataset 🦙")

df = load_data("./data")

with st.expander("🔎 Dataframe Preview"):
    st.write(df.tail(3))

query = st.text_area("🗣️ Chat with Dataframe")
container = st.container()
