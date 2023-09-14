import pandas as pd
import numpy as np

##################[ Series ]##################
print("##################[ Series ]##################")
a = pd.Series({"a": 1, "b": 2, "c": 3})
print(a)
print(a.index.values)

# a = np.arange(1, 5)
a = np.array([1, 2, 3, 4])
b = pd.Series(a)
print(b)
print(b.index.values)

##################[ DataFrame ]##################
print("##################[ DataFrame ]##################")
a = {"a":[1 , 2, 3, 0], "b":[4, 5, 6, 0], "c":[7, 8, 9, 0], "d":[10, 11, 12, 0]}
b = pd.Series(a)
c = pd.DataFrame(a, index=a.keys())
print(b)
print(c)

print(c.index.values)
print(c.columns)

print("----------[ index, columns ]----------")
a = pd.DataFrame({"a":(1, 2, 3), "b":1, "c":3})
print(a)
print("----------[ 위: 변경 전, 아래: 변경 후 ]----------")
# index, columns 이름 바꾸기
a.index = ["x", "y", "z"]
a.columns = ["i", "j", "k"]
print(a)

print("----------[ loc, iloc ]----------")
# loc = location
# iloc = index_location
print(a.loc[a["j"] == 1])
print(a.iloc[2])

print("----------[ describe ]----------")
a = {"a":[1 , 2, 3], "b":[4, 5, 6], "c":[7, 8, 9], "d":[10, 11, 12]}
b = pd.DataFrame(a)
print(b.describe())

print("----------[ sum : 열의 합 ]----------")
print(b.sum())
print("----------[ sum(axis=?) : 각 해당(?) Index의 합 ]----------")
print(b.sum(axis=1))
print("----------[ min : 최소 값 ]----------")
print(b.min())
print("----------[ min : 최대 값 ]----------")
print(b.max())
print("----------[ mean : 평균 ]----------")
print(b.mean())
print("----------[ 표준편차, 분산 ]----------")
print(b.std(), b.var()) # 표준편차, 분산
