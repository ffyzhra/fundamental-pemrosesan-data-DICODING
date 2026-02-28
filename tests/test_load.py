import os
import pandas as pd
from utils.load import load_to_csv


def test_load_creates_csv(tmp_path):
    df = pd.DataFrame({
        "Title": ["Test Shirt"],
        "Price": [160000.0],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Men"]
    })

    file_path = tmp_path / "fashion.csv"
    load_to_csv(df, filename=str(file_path))

    assert os.path.exists(file_path)


def test_load_empty_dataframe(tmp_path):
    df = pd.DataFrame()
    file_path = tmp_path / "empty.csv"

    load_to_csv(df, filename=str(file_path))

    assert not os.path.exists(file_path)