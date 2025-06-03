import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

base_url = "https://quotes.toscrape.com"
current_url = base_url



with open("scrapped.csv",'w',newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote","Author","Tags"])

    while current_url:
        response = requests.get(current_url)

        soup = BeautifulSoup(response.text,"html.parser")

        quotes = soup.find_all("div",class_="quote")

        for quote in quotes:
            text = quote.find("span",class_="text").get_text()
            author = quote.find("small",class_="author").get_text()
            tag_elements = quote.find("div", class_="tags").find_all("a", class_="tag")
            tags = [tag.text for tag in tag_elements]
            tag_string = ", ".join(tags)

            writer.writerow([text,author,tag_string])

        print(f"scrapped {current_url}")

        

        next_btn =soup.find("li",class_="next")

        if next_btn:
            next_btn_url = next_btn.a["href"]
            current_url = urljoin(current_url,next_btn_url)
          
        else:
            print("No next page found. Scraping complete.")
            current_url = None
            


