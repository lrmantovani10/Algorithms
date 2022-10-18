## Quicksort
def quicksort(arr, low, high):
    if low >= high:
        return 
    pivot = arr[high]
    i = low
    j = high - 1
    
    while i < j:
        while arr[j] >= pivot and j >= low:
            j -= 1 
        while arr[i] <= pivot and i < high:
            i += 1 
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[high], arr[i] = arr[i], arr[high]
    quicksort(arr, low, i - 1)
    quicksort(arr, i + 1, high)

array = [2, 8, 9, 20, 11]
quicksort(array, 0, 4)
print(array)

array1 = [10, 10,10]
quicksort(array1, 0, 2)
print(array1)
