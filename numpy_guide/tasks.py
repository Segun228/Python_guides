import numpy as np
from math import sqrt
a = np.zeros(10, dtype="int32")

b = np.ones((3, 3))

c = np.zeros((5, 5))
for i in range(5):
    c[i, i] = i + 1

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[:, 1])
print(arr[0:2, 1:3])
first = np.copy(arr[0])
arr[0] = arr[2]
arr[2] = first
print(arr)

data = np.random.randint(0, 100, size=(5, 5))

average = np.mean(data)
median = np.median(data)
max = np.max(data)
stand = np.std(data)
variation = np.var(data)

arr = np.arange(12)
arr.resize(4, 4)

dif = np.random.randint(1, 1000, 100).reshape(-1, 100)
print(dif[dif > 50])

dif = np.where(dif % 2 == 0, np.sqrt(dif), dif)
print(dif)
