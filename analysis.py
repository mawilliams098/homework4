from numpy import *
import pandas as pd

import matplotlib.pyplot as plt

# read in csv
books = pd.read_csv("books_list.csv")

print("Average overall rating = ", round(mean(books['Rating']), 2))

# print(books.corr())
print(books.corr()['Price']['Rating'])

# find most expensive book
print(max(books['Price'])) # 59.99

print(min(books['Price'])) # 10

# average price of book that have rating 3
print("Average Price for 1 star book = ", round(mean(books[books['Rating'] == 1])['Price'], 2))
print("Average Price for 2 star book = ", round(mean(books[books['Rating'] == 2])['Price'], 2))
print("Average Price for 3 star book = ", round(mean(books[books['Rating'] == 3])['Price'], 2))
print("Average Price for 4 star book = ", round(mean(books[books['Rating'] == 4])['Price'], 2))
print("Average Price for 5 star book = ", round(mean(books[books['Rating'] == 5])['Price'], 2))

# bar chart 




# random sample of books with rating less than one
# lowest = books[books['Rating'] <= 1]

# x = books["Price"]
# num_bins = 10
# n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
# plt.show()

# hist(lowest,column="Price")
# lowest.hist(column="Price", bins=10)
# plt.show()

# plot scatter plot between book price and rating
# plt.plot(lowest['Rating'], lowest['Price'], 'ro')
# plt.xlabel("Book Price")
# plt.ylabel("Rating")
# plt.show()

