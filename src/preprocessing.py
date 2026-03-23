# from src.data_loader import load_data
from data_loader import load_data

def preprocess():
    print("Data Preprocessing Completed...")
    df = load_data()
    # data = df.capitalize()
    return df