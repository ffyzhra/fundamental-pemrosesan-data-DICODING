import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://fashion-studio.dicoding.dev"


def scrape_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    all_data = []

    try:
        for page in range(1, 51):
            
            url = BASE_URL if page == 1 else f"{BASE_URL}/page{page}"
            print(f"Scraping page {page}: {url}")

            driver.get(url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CLASS_NAME, "collection-card")
                )
            )

            products = driver.find_elements(By.CLASS_NAME, "collection-card")
            print(f"Products found: {len(products)}")

            for prod in products:
                try:
                    title = prod.find_element(By.TAG_NAME, "h3").text.strip()
                    price = prod.find_element(By.CLASS_NAME, "price").text.strip()

                    rating = colors = size = gender = None
                    details = prod.find_elements(By.TAG_NAME, "p")

                    for d in details:
                        text = d.text.strip()
                        if "/" in text:
                            rating = text
                        elif "Color" in text:
                            colors = text
                        elif "Size" in text:
                            size = text
                        elif "Gender" in text:
                            gender = text

                    all_data.append({
                        "Title": title,
                        "Price": price,
                        "Rating": rating,
                        "Colors": colors,
                        "Size": size,
                        "Gender": gender
                    })

                except Exception:
                    continue

            time.sleep(1)

    finally:
        driver.quit()

    print(f"Total data scraped: {len(all_data)}")
    return all_data