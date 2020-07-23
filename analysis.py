from numpy import *
import pandas as pd

import matplotlib.pyplot as plt

# read in csv
books = pd.read_csv("books_list.csv")

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

