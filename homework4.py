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
    title = row.h3.a["title"]
    single_book["Title"] = title
    print(single_book)

