import pandas as pd
from scipy.sparse import coo_matrix
from data_setup import load_books_data
import numpy as np
from numpy.linalg import norm

# setup the data
data, books = load_books_data()
data['user'] = data['user'].astype("category")
data['isbn'] = data['isbn'].astype("category")

# Construct rating matrix
# R is a special matrix. It is (user, isbn, rating) data matrix with all null rating values removed
# R = coo_matrix((data['rating'].astype(float), (data['user'].cat.codes.copy, data['isbn'].cat.codes.copy)))

R = coo_matrix((data['rating'].astype(float), (data['user'].cat.codes.copy(), data['isbn'].cat.codes.copy())))

M, N = R.shape
K = 3  # latent factors

# initialize factor matrices P and Q
P = np.random.rand(M, K)  # P = users x factors matrix initialized with random values
Q = np.random.rand(K, N)  # Q = factors x books matrix initialized with random values


# Calculate error e
def error(R, P, Q, lamda=0.02):
    ratings = R.data
    rows = R.row
    cols = R.col
    e = 0
    for ui in range(len(ratings)):
        rui = ratings[ui]
        u = rows[ui]
        i = cols[ui]
        if rui > 0:
            e = e + pow(rui - np.dot(P[u, :], Q[:, i]), 2) + \
                lamda * (pow(norm(P[u, :]), 2) + pow(norm(Q[:, i]), 2))
    return e


# Stochastic Gradient Descent to least RMSE and (P,Q) value.
def SGD(R, K, lamda=0.02, steps=10, gamma=0.001, margin=0.05):
    M, N = R.shape
    P = np.random.rand(M, K)
    Q = np.random.rand(K, N)
    init_rmse = rmse = np.sqrt(error(R, P, Q, lamda) / len(R.data))
    print('Initial RMSE : {rmse}'.format(rmse=rmse))
    for steps in range(steps):
        for ui in range(len(R.data)):
            rui = R.data[ui]
            u = R.row[ui]
            i = R.col[ui]
            if rui > 0:
                eui = rui - np.dot(P[u, :], Q[:, i])
                P[u, :] = P[u, :] + gamma * 2 * (eui * Q[:, i] - lamda * P[u, :])
                Q[:, i] = Q[:, i] + gamma * 2 * (eui * P[u, :] - lamda * Q[:, i])
        rmse = np.sqrt(error(R, P, Q, lamda) / len(R.data))
        print('Step: {step}, RMSE : {rmse}'.format(step=steps, rmse=rmse))
        if rmse < margin:
            break
    print('Final RMSE : {rmse}'.format(rmse=rmse))
    print('RMSE reduced by {reduction} %'.format(reduction=round((1 - rmse / init_rmse) * 100, 2)))
    return P, Q


P, Q = SGD(R, K=2, lamda=0.01, steps=100, gamma=0.0005, margin=0.05)
