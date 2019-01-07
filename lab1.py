from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn import datasets

StdSc = StandardScaler()
minMaxSc =  MinMaxScaler()
maxAbsSc = MaxAbsScaler()

y = [[0, 1], [0, 2], [1, 3], [0, 2], [2, 4]]

# StdSc = StdSc.fit(y)
minMaxSc = minMaxSc.fit(y)
maxAbsSc = maxAbsSc.fit(y)

print(StdSc.fit_transform(y))
print(minMaxSc.transform(y))
print(minMaxSc.transform(datasets.load_digits().data))

# print(datasets.load_iris())