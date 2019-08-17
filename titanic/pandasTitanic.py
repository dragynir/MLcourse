import numpy as np 
import pandas

f = open("5.txt", "w")


data = pandas.read_csv("titanic.csv", index_col='PassengerId')

#1

#s = data['Sex']
#m_count = s[s == 'male'].shape[0]
#em_count = s.shape[0] - m_count

#f.write("{} {}".format(m_count, fem_count))

#2
#s = data['Survived']


#print(s.value_counts())
#survived = int(s.value_counts()[1])
#f.write(str(round(survived / s.shape[0] * 100, 2)))

#3
#pclass = data['Pclass']
#first_c = pclass.value_counts()[1]  
#f.write(str(round(first_c / pclass.shape[0] * 100, 2)))

#4
#age = data['Age']
#age = age.dropna()
#mean = round(np.mean(age), 2)
#median = round(np.median(age), 2)
#f.write("{} {}".format(mean, median))


#5
'''s = data['SibSp']
p = data['Parch']

b = np.column_stack((s, p))
print(type(data))
c = pandas.core.frame.DataFrame(b).corr(method='pearson')
f.write('0.414838')'''


'''n = s.shape[0]


sum_s = np.sum(s)
sum_p = np.sum(p)
sum_s_sq = np.sum(s ** 2)
sum_p_sq = np.sum(p ** 2)


u = n * np.sum(s * p)  - (sum_s * sum_p)

d = ((n * sum_s_sq - (sum_s) ** 2) * (n  * sum_p_sq  - sum_p ** 2))

f.write(str(int(round(u / d, 2))))'''



'''def extractName(s):
	s = s.split(',')[1]
	if s.find("Mrs") != -1 and s.find('(') != -1:
		s = s[s.find('(') + 1:s.find(')')].split()[0]
	else:
		s = s.split()[1]
	return s

d = data[data['Sex'] == 'female']['Name'].values
f.write(data[data['Sex'] == 'female']['Name'].to_csv())

d = pandas.core.series.Series(map(extractName, d))

print(d.value_counts())'''

