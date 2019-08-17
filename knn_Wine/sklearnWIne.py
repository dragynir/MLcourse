import numpy as np 
import pandas
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale
data = pandas.read_csv('wine.data')

y = data.iloc[:, 0]
X = data.iloc[:, 1:]


X = scale(X)


max_sc = 0
opt_k = 1
for k in range(1, 51):

	clf = KNeighborsClassifier(n_neighbors=k)

	clf.fit(X, y)

	kf = KFold(n_splits=5, shuffle=True, random_state=42)

	scores = cross_val_score(clf, X, y, cv=kf)

	sc = np.mean(scores)
	print("score: {}, k: {}".format(sc, k))
	if sc > max_sc:
		max_sc = sc
		opt_k = k

print("Best score: {}, k: {}".format(round(max_sc, 2), opt_k))

#clf.predict([])



