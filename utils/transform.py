import pandas as pd
import re


def transform(data):
    print("=== TRANSFORM ===")

    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data)

    df = df[df["Title"].notna()]
    df = df[df["Title"].str.strip() != ""]
    df = df[df["Title"] != "Unknown Product"]

    def clean_price(x):
        if not x:
            return None
        num = re.sub(r"[^\d.]", "", str(x))
        num = re.sub(r"\.(?=.*\.)", "", num)
        return float(num) * 16000 if num else None

    def clean_rating(x):
        if not x:
            return None
        nums = re.findall(r"\d+\.?\d*", str(x))
        return float(nums[0]) if nums else None

    def clean_colors(x):
        if not x:
            return None
        nums = re.findall(r"\d+", str(x))
        return int(nums[0]) if nums else None

    df["Price"] = df["Price"].apply(clean_price)
    df["Rating"] = df["Rating"].apply(clean_rating)
    df["Colors"] = df["Colors"].apply(clean_colors)

    def clean_size(x):
        if isinstance(x, str):
            return x.replace("Size:", "").strip()
        return None

    def clean_gender(x):
        if isinstance(x, str):
            return x.replace("Gender:", "").strip()
        return None

    df["Size"] = df["Size"].apply(clean_size)
    df["Gender"] = df["Gender"].apply(clean_gender)

    df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
    df = df[df["Price"].notna()]
    df = df[df["Price"] > 0]

    df = df.drop_duplicates()
    df = df[["Title", "Price", "Rating", "Colors", "Size", "Gender"]]

    print("Rows after transform:", len(df))
    return df