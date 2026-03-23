import pandas as pd
import numpy as np

def load_data():
    df = pd.read_csv("D:\\CreateBot Labs Internship\\Day 2\\GitHub Assignment\\ds-git-assignment\\data\\dummy_dataset.csv")
    print("Data Loaded Succesfully...")
    return df

# data = load_data()
# print(data)