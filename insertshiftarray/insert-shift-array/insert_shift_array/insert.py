def insertShiftArray(arr,n):     
    length = int(len(arr)/2)     
    arr += [n]      
    for i in range(len(arr),length+1,-1):         
        x=arr[i-1]         
        arr[i-1]=arr[i-2]         
        arr[i-2]=x     
    return arr
