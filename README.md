# ETL Pipeline: Fashion Studio Products

A modular **Extract → Transform → Load** pipeline that scrapes product data from [Fashion Studio](https://fashion-studio.dicoding.dev/), cleans it with pandas and saves an analysis-ready CSV. Final project for Dicoding's *Belajar Fundamental Pemrosesan Data* class.

## Pipeline

| Step          | Module               | What it does                                                                                                                              |
| ------------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Extract**   | `utils/extract.py`   | Scrapes all 50 catalogue pages with Selenium (headless Chrome)                                                                            |
| **Transform** | `utils/transform.py` | Cleans prices (USD → IDR at Rp16,000), ratings, colour count, size and gender; removes "Unknown Product" rows and duplicates |
| **Load**      | `utils/load.py`      | Writes the result to `output/fashion_data.csv`                                                                                            |

Result: **867 clean product rows** with columns `Title, Price, Rating, Colors, Size, Gender`.

## Running it

```bash
pip install -r requirements.txt
python main.py
```

Requires Google Chrome installed (Selenium manages the driver).

## Tests

Unit tests for each stage with **pytest**:

```bash
python -m pytest tests
python -m pytest --cov=utils tests     # with coverage
```

## Tech stack

Python · Selenium · pandas · pytest · pytest-cov

## Author

**Fayza Azzahra** · [GitHub](https://github.com/ffyzhra) · [LinkedIn](https://www.linkedin.com/in/ffyzhra)
