"""
Homework: Python and Web Scraper
Andre Zazzera (alz9cb), Annie Williams (maw3as)
"""

import csv
import requests
from bs4 import BeautifulSoup


total_books = []
for i in range(1,51):
    URL = 'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    #print(soup.prettify())
    
    table = soup.find('div', class_ = 'col-sm-8 col-md-9')
    #print(table.section)
    
    div_above_table = table.section.div.find_next_sibling()
    list_of_books = div_above_table.find('ol', class_='row')
    

    
    for row in list_of_books.find_all('li'):
        
        # scrape book titles
        single_book = {}
        title = row.h3.a['title']
        single_book['Title'] = title
        
        # scrape book price
        price_div = row.find('div', class_="product_price")
        price = price_div.find('p', class_="price_color").text
        single_book["Price"] = float(price[1:])
        
        # scrape availability
        availability = price_div.find('p', class_="instock availability").text
        single_book["Availability"] = availability.strip()
        
        # scrape star rating
        rating_div = row.p['class']
        if rating_div[1] == 'One':
            rating_div[1] = 1
        elif rating_div[1] == 'Two':
            rating_div[1] = 2
        elif rating_div[1] == 'Three':
            rating_div[1] = 3
        elif rating_div[1] == 'Four':
            rating_div[1] = 4
        else:
            rating_div[1] = 5
        single_book['Rating'] = rating_div[1]
        
        # scrape catalogue reference
        ref = row.h3.a['href']
        single_book['Link'] = 'http://books.toscrape.com/'+ref
        
        # add single book instance to list of all books
        total_books.append(single_book)
    

    
filename = 'books_list.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['Title', 'Price', 'Availability', 'Rating', 'Link']) 
    w.writeheader() 
    for book in total_books: 
        w.writerow(book)
    
#%%
# sort total_books list        
total_books_sorted = sorted(total_books, key = lambda i: i['Title'])




# binary search for a book title
def binarySearchbooks(item_list, title):
    start = 0
    end = len(item_list)
    found = False
    info = []
    while(start <= end and not found):
        mid = (start + end) // 2
        if item_list[mid]['Title'] == title:
            found = True
            info = item_list[mid]
        else:
            if item_list[mid]['Title'] > title:
                end = mid - 1
            else:
                start = mid + 1
    return found, info # returns boolean, book info from the list

    


print(binarySearchbooks(total_books_sorted, "A Spy's Devotion (The Regency Spies of London #1)"))
