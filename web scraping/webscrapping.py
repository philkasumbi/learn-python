"""
webscrapping - pulling data from websites
there are people who use web scrapping for market research,price monitoring,academic research,automate repetitive tasks,sentiment analysis 
requests -a popular HTTP library that allows you to send HTTP requests easily (e.g., GET, POST).
beautifulsoup4 -a library used to parse HTML and XML documents, often used for web scraping.
used to turn a raw html into searchable object 
https://quotes.toscrape.com/
"""
import requests
from bs4 import BeautifulSoup
import csv




def scrape(pages):
    headers = {"User-agents":"Mozilla/5.0"}

    for i in range(5):
        url = f"https://quotes.toscrape.com/page/{i}/"

        # fetch and parse
        response = requests.get(url,headers=headers)

        soup = BeautifulSoup(response.text,"html.parser")

        

        quotes = soup.find_all("div",class_="quote")

        # open CSV
        with open("scrapped.csv","w",newline="",encoding="utf-8") as file:
            Writer = csv.writer(file)
            Writer.writerow(["quote","author","tag"])

        # extract and write rows
            for quote in quotes:
                text = quote.find("span",class_="text").get_text()
                author = quote.find("small",class_="author").get_text()
                tag = [t.get_text() for t in quote.find_all("a",class_="tag")]
                Writer.writerow([text,author,tag])
    print("DONE!")

scrape(5)