def Merge(arr, left_array, left_count, right_array, right_count):
    i, j, k = 0, 0, 0
    while i < left_count and j < right_count:
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
            k += 1
        else:
            arr[k] = right_array[j]
            j += 1
            k += 1
    while i < left_count:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < right_count:
        arr[k] = right_array[j]
        j += 1
        k += 1

def MergeSort(arr, n):
    # Base condition to stop recursion when array can't be divided further
    if n < 2:
        return
    
    # find middle index
    mid = n//2

    # Dividing array at mid
    L = arr[:mid]
    R = arr[mid:]

    # Recursively divide the left sub array till it can't be divided
    MergeSort(L, mid)

    # Recursively divide the right sub array till it can't be divided
    MergeSort(R, n-mid)

    # Merging L and R into A as sorted list.
    Merge(arr, L, mid, R, n-mid)


if __name__ == "__main__":
    arr = [9, 4, 7, 6, 3, 1, 5, 5]
    n = len(arr)

    MergeSort(arr, n)

    print("After Sorting Array: ")
    print(arr)
