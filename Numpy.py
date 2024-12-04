'''
import numpy as np
ar = np.array([10,2,30,4])
arr = np.array([[10,20,3,40],[50,6,70,8]])
print(arr)
print (arr[0:2,0:2])
print(arr[1,1:3])
print(arr[1,1])
print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))
print(arr.dtype)

print(np.sort(ar))
print(np.sort(arr)) '''

import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_excel("D:/expense3.xlsx")
df = pd.DataFrame(data)
print(df)
plt.bar(df["Date"], df["Amount"])
plt.show()
