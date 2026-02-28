from utils.extract import scrape_page
from utils.transform import transform
from utils.load import load_to_csv


def main():
    print("Starting ETL process...")

    data = scrape_page()
    print(f"Data extracted: {len(data)}")

    df = transform(data)
    print(f"Data transformed: {len(df)}")

    print(df.info())

    load_to_csv(df)

    print("ETL selesai!")


if __name__ == "__main__":
    main()