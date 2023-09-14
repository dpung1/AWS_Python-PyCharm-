# 넘파이(Numpy)
# 고성능(대량) 수치 계산을 위한 라이브러리
# 벡터, 행렬 연산

import numpy as np

numArray1 = [1, 2, 3, 4, 5]
numArray2 = [6, 7, 8, 9, 10]

numArray3 = []
for i in range(len(numArray1)):
    numArray3.append(numArray1[i] + numArray2[i])

print(numArray3)

npArray1 = np.array(numArray1)
npArray2 = np.array(numArray2)
npArray3 = npArray1 * npArray2

print(npArray1)
print(npArray2)
print(npArray3)

npDoubleArray1 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
npDoubleArray2 = np.array([[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]])

print(npDoubleArray1)
print(npDoubleArray2)
print(npDoubleArray1 + npDoubleArray2)

print(npArray1.shape)
print(npDoubleArray1.shape)

# Numpy의 배열 생성
npArray4 = np.arange(1, 11)
print(npArray4)

# Numpy의 배열 모든 값을 0으로 생성
npArray5 = np.zeros(10)
print(npArray5)
npArray6 = np.zeros_like(npDoubleArray1)
print(npArray6)

# Numpy의 배열 모든 값을 1로 생성
npArray7 = np.ones(10)
print(npArray7)
npArray8 = np.ones_like(npDoubleArray1)
print(npArray8)

# Numpy의 배열 모든 값을 원하는 값으로 생성 ((배열의 갯수(행 , 열)), 배열의 값)
npArray9 = np.full((5, 3), 5)
print(npArray9)
print(npArray9 * 2)



