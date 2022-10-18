def merge_sort(arr):

    # Get middle element in array
    middle = int(len(arr)/2)

    # Base case -- to avoid infinite recursion
    if middle == 0:
        return
        
    # Find two array halves
    first_half = arr[:middle]
    second_half = arr[middle:]

    # Recursively call merge sort for both halves
    merge_sort(first_half)
    merge_sort(second_half)

    # First array index
    i = 0
    # Second array index
    j = 0
    # Third array index
    k = 0

    # Comparing both arrays and updating the resulting one
    while i < len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            arr[k] = first_half[i]
            i += 1
        else:
            arr[k] = second_half[j]
            j += 1
        k += 1

    # Adding leftover elements from the left array
    while i < len(first_half):
        arr[k] = first_half[i]
        i += 1
        k += 1

    # Adding leftover elements from the right array
    while j < len(second_half):
        arr[k] = second_half[j]
        j += 1
        k += 1


arr1 = [56, 12, 10, 8]
merge_sort(arr1)
print(arr1)

arr2 = [7, 5, 3]
merge_sort(arr2)
print(arr2)

arr3 = [19, 18, 6, 3]
merge_sort(arr3)
print(arr3)