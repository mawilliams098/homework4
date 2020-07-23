"""
Homework: Python and Web Scraper

"""

import csv
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("books.html"), 'html.parser')

total_books = []

# find the main div that the books are on
table = soup.find('div', class_ = "col-sm-8 col-md-9")
div_above_table = table.section.div.find_next_sibling()
list_of_books = div_above_table.find('ol', class_="row")

for row in list_of_books.find_all('li'): 

    single_book = {}

    # scrape book title
    title = row.h3.a["title"]
    single_book["Title"] = title

    # scrape book price
    price_div = row.find('div', class_="product_price")
    price = price_div.find('p', class_="price_color").text
    single_book["Price"] = price

    # scrape availability
    availability = price_div.find('p', class_="instock availability").text
    single_book["Availability"] = availability.strip()

    # add single book instance to list of all books
    total_books.append(single_book)


filename = 'books_list.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['Title', 'Price', 'Availability']) 
    w.writeheader() 
    for book in total_books: 
        w.writerow(book) 

