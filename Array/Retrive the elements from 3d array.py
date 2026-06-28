from numpy import *
arr = array([
              [ 
                  [13,15,17,19], 
                  [1,2,3,4] 
              ],
              [ 
                  [5,6,7,8],
                  [9,10,11,12]
              ]
               ])


for i in range(len(arr)):# ---> Number of the elements in the array
    print("-------------> I ",arr[i])
    for j in range(len(arr[i])):# ----> Number of the
        print("------------->  JJ ",arr[i][j])
        for k in range(len(arr[i][j])):
            print(arr[i][j][k],end=" ")
    print()
