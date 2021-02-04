import streamlit as st 
import pandas as pd
import plotly.express as px

def load_data():
    """ Function for loading data"""
    df = pd.read_csv('../data/5tystock.csv')

    numeric_df = df.select_dtypes(['float', 'int'])
    numeric_cols = numeric_df.columns