## Merge Sort

the function (Merge_sort) takes in arr as input and then return the same arr in sorted order by dividing that arr and using recursion with that to give the disered result  which is a the same array sorted.


```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```


## Trace



`Sample Array: [8,4,23,42,16,15]`


**Pass 1**


![alt](./merge1.jpg)



first the array is splitted into half with the same sizes , These two parts are sorted by recursive calls to give us 2 arrays 

1- [8 ,4,23]

2- [42 ,16 ,15]

**Pass 2**

![alt](./merge2.jpg)


then we recursivlly calls the function with first half nd then the secound half which will divide the the 2 arrays into 4 arrays

1- [8]

2- [4,23]

3- [42]

4- [16 ,15]



**Pass 3** 


![alt](./merge3.jpg)


We keep dividing it until the subpart of the list consists of only one element


**Pass 4**

![alt](./merge4.jpg)

we will combine the two elements in the given sorted way 


**Pass 5**


![alt](./merge5.jpg)


we will combine the 4 lists of elements and convert them into a list of tow elements after sorting


**Pass 6**


![alt](./merge6.jpg)

then we get the final result which is a full sorted array of the original array



## Efficency

### Time: O(n)

The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.

### Space: O(n)

No additional space is being created. This array is being sorted in place…keeping the space at constant O(n).
