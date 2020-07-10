# Introductory Algorithms for Recommendation Systems

Discusses some basic algorithms for Recommendation Systems (usecases for selling more on ecommerce or video streaming sites)
- Content-Based Filtering (no code in the repo)
- Collaborative Filtering 
  -  Nearest Neighbors model
  -  Latent Factor Analysis Model - based on Principal Component Analysis
  -  Both models answer the questions like what are the top N books recommended for the reader on a booksite, 
    what top 10 movies viewer would like to watch on Netflix, Amazon Prime etc.
- Association Rules Learning (Apriori Algorithm) 
  - recommends buyer complementary or associated products one can cross-sell,upsell,substitute etc. For example, you can suggest customer a piece of Cake that goes well along with coffee in the bakery etc.

### Perquisites
This project is developed using PyCharm CE IDE and tested on Python 3.7 (64 bit). 

You can install prequisites libraries using requirements.txt. I exported requirements.txt for ease of installation. These libraries are configured on my machine. All are not needed to run the program.

From your project repository folder run this command:

`pip install -r requirements.txt` (Python 2), or `pip3 install -r requirements.txt `(Python 3)

### Book Crossing Dataset - 
Link - http://www2.informatik.uni-freiburg.de/~cziegler/BX/

1. `collaborative_filter.py ` -  run the python script to observe how Nearest K- Neighbors model works
2. `latent_factor.py` run this script to execute implementation of Latent Factor model 

### Bakery Dataset
Link - http://wiki.csc.calpoly.edu/datasets/wiki/ExtendedBakery75K

`apriori_association_rule.py` has code to implement aprior algorithm that calculates support, confidence, lift, item combination rules to recommend complementary products

### Disclaimer 
This is not my original code but part of https://app.pluralsight.com/library/courses/algorithms-recommendation-systems.
I just had fun rewriting it (learning by doing) and picking up some python skills/tricks along the way. I suggest this course to anyone who is new to recommendations system and got pluralsight account. 
Instructor has done a good job.

