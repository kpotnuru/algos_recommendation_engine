import pandas as pd
import numpy as np
from scipy.spatial.distance import hamming
from data_setup import load_books_data

data, books = load_books_data()

# input : isbn, get title and author for that isbn
def get_book_info(isbn):
    title = books.at[isbn, "title"]
    author = books.at[isbn, "author"]
    return title, author


# get user ratings for all records for provided user
# sort user ratings table for particular user in asc order on ratings column, get top n records
def fav_books(user, n):
    user_ratings = data[data["user"] == user]
    sorted_ratings = pd.DataFrame.sort_values(user_ratings, ['rating'], ascending=[0])[:n]
    sorted_ratings['title'] = sorted_ratings['isbn'].apply(get_book_info)
    return sorted_ratings


# calculate hamming distance between 2 users
def distance(user1, user2):
    try:
        user1_ratings = user_item_rating_matrix.transpose()[user1]
        user2_ratings = user_item_rating_matrix.transpose()[user2]
        distance = hamming(user1_ratings, user2_ratings)
    except:
        distance = np.NaN
    return distance


# find K nearest user
def nearest_neighbors(user, K=10):
    all_users = pd.DataFrame(user_item_rating_matrix.index)
    all_users = all_users[all_users.user != user]
    all_users['distance'] = all_users['user'].apply(lambda x: distance(user, x))
    k_nearest_users = all_users.sort_values(['distance'], ascending=True)['user'][:K]
    return k_nearest_users


def top_n(user, n=3):
    k_nearest_users = nearest_neighbors(user)
    nn_rating = user_item_rating_matrix[user_item_rating_matrix.index.isin(k_nearest_users)]
    avg_rating = nn_rating.apply(np.nanmean).dropna()
    books_already_read = user_item_rating_matrix.transpose()[user].dropna().index
    avg_rating = avg_rating[~avg_rating.index.isin(books_already_read)]  # nice trick, should use sometime
    top_n_isbns = avg_rating.sort_values(ascending=False).index[:n]
    return pd.Series(top_n_isbns).apply(get_book_info)


data = data[data["isbn"].isin(books.index)]
# group by isbn, give list of distinct isbn and count of user who rated the isbn
users_per_isbn = data.isbn.value_counts()

# group by user, give list of distinct user, the number of isbn the user has rated
isbn_per_user = data.user.value_counts()


# print(users_per_isbn.head())
# print(users_per_isbn.shape, isbn_per_user.shape)

data = data[data['isbn'].isin(users_per_isbn[users_per_isbn > 10].index)]

data = data[data['user'].isin(isbn_per_user[isbn_per_user > 10].index)]

user_item_rating_matrix = pd.pivot_table(data, values='rating', index=['user'], columns=['isbn'])

print("fav_books(204813, 10)")
print(fav_books(204813, 10))

print("top_n(204813, 10)")
print(top_n(204813, 10))
