#Rotate matrix 90 degrees in place

#Time Complexity = O(n^2)
#Space complexity = O(n^2) given the array
def rotate90(arr):
    for layer in range(0, len(arr)//2):
        first = layer
        last = len(arr)-1-layer

        for i in range(first, last):
            offset = i-first
            top = arr[first][i]

            arr[first][i] = arr[last-offset][first]

            arr[last-offset][first] = arr[last][last-offset]

            arr[last][last-offset] = arr[i][last]

            arr[i][last] = top

    return arr


def print2d(arr):
    for i in range(len(arr)):
        s = ""
        for j in range(len(arr[0])):
            s += str(arr[i][j]) + " "
        
        print(s)

arr = [[0,1,2],[3,4,5],[6,7,8]]
print2d(arr)
print("")
print2d(rotate90(arr))