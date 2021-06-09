def selectionSort(arr):
    for j in range(len(arr)):
        min=j
        for i in range(j, len(arr)):
            if arr[i]<arr[min]:
                min=i
        arr[j],arr[min]=arr[min],arr[j]
    return arr

print(selectionSort([8,5,2,6,9,3,1,4,7]))