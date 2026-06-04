# IMDb Top 250 Movie Scraper
A professional web scraping tool written in Python to automatically extract and compile details from the official IMDb Top rated movies chart.

## 🚀 Project Overview
This project uses browser automation to handle dynamically loaded elements on IMDb. It bypasses background layout structures, manages rendering delays, cleans raw data, and formats the output into a clean tabular layout.

## 🛠️ Technologies Used
* **Python** (Core Scripting)
* **Selenium WebDriver** (Web Automation & Content Loading)
* **WebDriver Manager** (Automated ChromeDriver Management)
* **Pandas** (Data Transformation & Structured CSV Generation)

## 📊 Extracted Features
The automation script cleanly scrapes:
1. **Ranking:** Position on the chart.
2. **Title:** Cleaned movie names.
3. **Rating:** Core audience score (e.g., 9.3, 9.2).

## 📁 Project Structure
* `webscrapper.py` - The core functional Python automation logic.
* `imdb_top_movies.csv` - The final extracted tabular dataset.
