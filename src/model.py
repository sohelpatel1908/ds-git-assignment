# from src.preprocessing import preprocess
from preprocessing import preprocess
from data_loader import load_data


def model_training():
    data = preprocess()
    print("Model Successfully Trained!")