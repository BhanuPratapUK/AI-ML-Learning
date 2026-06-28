import numpy as np
import pandas as pd
import xlrd

arr = np.array([10,23,23,46,57])
ser= pd.Series(arr)
a = ser.values
print(a)


my_dict= {
    "empid":[101, 102, 103, 104],
    "Name":["A", "B", "C", "D"]
}

df = pd.Series(my_dict)
print(df)