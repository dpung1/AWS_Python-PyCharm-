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

# npArray1 = np.array(numArray1)
# npArray2 = np.array(numArray2)
#
# npArray3 = npArray1 + npArray2
#
# print(npArray3)