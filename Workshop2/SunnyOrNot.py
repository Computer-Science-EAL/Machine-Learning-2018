from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import tree
import numpy as np

#1 = sunny, 2 = overcast, 3 = rainy
#1 = grass, 2 = gravel

#1 = yes, 0 = no

#observations
X_train = np.array([[1,2], [2,1], [3,1], [1,2], [1,2], [2,1], [3,1], [3,1], [1,2], [3,1], [1,1], [2,1], [2,1], [3,1], [3,2], [3,2], [3,1]]) #samples
Y_train = np.array([0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0]) #classes

gaussian = GaussianNB()
gaussian.fit(X_train, Y_train)
Y_pred = gaussian.predict([[1,2]])
print(Y_pred)
