import os


def load_to_csv(df, filename="fashion_data.csv"):
    if df.empty:
        return

    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)
    df.to_csv(path, index=False)