import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

base_url = "https://books.toscrape.com/"
current_url = base_url

with open("scrapped.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Availability", "Rating"])

    while current_url:
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            price = book.find("p", class_="price_color").get_text()
            title = book.h3.a["title"]
            availability = book.find("p", class_="instock availability").get_text(strip=True)

            rating_map = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }

            rating_word = book.find("p", class_="star-rating")["class"][1]
            rating = rating_map.get(rating_word, 0)

            writer.writerow([title, price, availability, rating])

        print("Scraped:", current_url)

        next_btn = soup.find("li", class_="next")
        if next_btn:
            next_page_url = next_btn.a["href"]
            current_url = urljoin(current_url, next_page_url)
        else:
            print("No next page found. Scraping complete.")
            current_url = None
