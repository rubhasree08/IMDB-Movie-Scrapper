from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Open Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

# IMDb Top 250 Page
driver.get("https://www.imdb.com/chart/top/")

# Wait for page load
time.sleep(5)

movies = []

try:
    movie_items = driver.find_elements(
        By.CSS_SELECTOR,
        "li.ipc-metadata-list-summary-item"
    )

    for movie in movie_items:

        try:
            title = movie.find_element(
                By.TAG_NAME,
                "h3"
            ).text

            rating = movie.find_element(
                By.CSS_SELECTOR,
                "span.ipc-rating-star--rating"
            ).text

            movies.append({
                "Title": title,
                "Rating": rating
            })

        except:
            continue

except Exception as e:
    print("Error:", e)

# Create DataFrame
df = pd.DataFrame(movies)

print(df.head())
print("Total Movies:", len(df))

# Save CSV
df.to_csv(
    "imdb_top_movies.csv",
    index=False,
    encoding="utf-8-sig"
)

print("CSV Saved Successfully!")

driver.quit()