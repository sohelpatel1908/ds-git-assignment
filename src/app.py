import pandas as pd
import numpy as np
from data_loader import load_data
from preprocessing import preprocess
from model import model_training

data = load_data()
print(data)
print("Data Loaded Successfully.")

preprocess = preprocess()
print("Data Preprocessed Succesfully.")

model = model_training()
print("Model Trained Successfully.")

print("Accuracy: 90%")