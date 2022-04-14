def reverseArray(arr):
    for i in range(int(len(arr)/2)):
        n = arr[i]
        arr[i]=arr[len(arr) - i - 1]
        arr[len(arr) - i - 1]=n
    return arr

arr=[1, 2, 3, 4, 5]
print(reverseArray(arr))