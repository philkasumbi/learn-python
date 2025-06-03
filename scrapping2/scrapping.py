import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

books = soup.find_all("article",class_="product_pod")



    
with open("scrapped.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title","Price","Availability","Rating"])

    for book in books:
        price = book.find("p",class_="price_color").get_text()
        title = book.h3.a["title"]
        availability = book.find("p",class_="instock availability").get_text()
        # rating = book.find("p",class_="star-rating")["class"][1]
        rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
        }

        rating_word = book.find("p", class_="star-rating")["class"][1]
        rating = rating_map.get(rating_word, 0)  # default to 0 if not found
        

        writer.writerow([title,price,availability,rating])

    print("DONE!")    
       