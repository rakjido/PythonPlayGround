from sklearn import preprocessing

import numpy as np
import pandas as pd 

dt = np.arange(1,100).reshape(3,33).T
print(dt)

# 이진화 (binaryization) preprocessing
dt_bin = preprocessing.Binarizer(threshold=42.4).transform(dt)
print(dt_bin)

# 정규화 (Normalize)
dt_normal = preprocessing.Normalizer().transform(dt)
print(dt_normal)

# 범주화 (group by sum)
large_counts = [30000, 200, 8907, 1000789, 2, 80, 678, 9876, 1111, 32, 44, 2222, 345, 2, 45, 78]

a = np.floor(np.log10(large_counts))
s_a = pd.Series(a)
print(s_a)
cat_s_a = s_a.value_counts()
print(cat_s_a)

print(pd.qcut(large_counts, 10))

# label데이터를 숫자로 변환
labels = ["red", "black", "green"]
numbers = preprocessing.LabelEncoder().fit(labels).transform(labels)
print(numbers)

# 범주형 데이터를 dummy로 변환 : 범주형 데이터를 linear regression등에 사용할 경우
cats = np.array(['a','b','c','b','c','a'])
dummies = pd.get_dummies(cats)
print(dummies)