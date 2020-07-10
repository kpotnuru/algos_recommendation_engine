import pandas as pd

dataFile = 'BX-CSV-Dump/BX-Book-Ratings.csv'
bookFile = 'BX-CSV-Dump/BX-Books.csv'

itempath = 'Bakery-CSV-Dump/EB-build-goods.sql'
receiptspath = 'Bakery-CSV-Dump/75000-out2.csv'


def load_books_data():
    data = pd.read_csv(dataFile, sep=";", header=0, names=['user', 'isbn', 'rating'], encoding='unicode_escape')
    books = pd.read_csv(bookFile, sep=';', header=0, error_bad_lines=False,
                        usecols=[0, 1, 2], index_col=0, names=['isbn', "title", "author"], encoding='unicode_escape')
    return data, books


'''
Load Bakery Data:
 1) Open/Read the receipts csv file, clean it and get list of receipts. 
 each receipt line has basket with items ids, return list of baskets.
 e.g ['11', '21']
 
 2) Open/Read items sql file, clean it, return list of items. 
 each item has id, description, price, category etc.
 e.g ['0', "'Chocolate'", "'Cake'", '8.95', "'Food'"]
    
'''


def load_bakery_data():
    with open(receiptspath, "r") as receiptsfile:
        receiptsdata = receiptsfile.read().split('\n')
        baskets = [line.split(",")[1:] for line in receiptsdata[0:-1]]
    with open(itempath, "r") as itemsfile:
        lines = itemsfile.read().split('\n')
        items = [line.split("(")[1][0:-2].split(",") for line in lines[0:-1]]
    return baskets, items



