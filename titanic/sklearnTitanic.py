import numpy as np 
import pandas
from sklearn.tree import DecisionTreeClassifier


#выбираем только нужные столбцы
data = pandas.read_csv("titanic.csv")[['Pclass', 'Sex', 'Fare', 'Age', 'Survived']].dropna()



def conv(d):
	if d == 'male':
		return 1
	return 0


X = data[['Pclass', 'Sex', 'Fare', 'Age']]
X['Sex'] = X['Sex'].apply(conv)

print(X)

y = data[['Survived']]



clf = DecisionTreeClassifier(random_state=241)

clf.fit(X, y)

importances = clf.feature_importances_
print(importances)


