#Zero Matrix

def zero_matrix(arr):
    cols = []
    rows = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                cols.append(j)
                rows.append(i)
    
    for i in rows:
        for j in range(len(arr[i])):
            arr[i][j] = 0
    
    for j in cols:
        for i in range(len(arr)):
            arr[i][j] = 0
    
    return arr

def print2d(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])
print2d(zero_matrix([[3,1,0], [1,3,3], [3,0,3]]))

