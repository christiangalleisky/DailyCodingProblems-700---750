
def peak(array):
    n = len(array)
    start, end = 0, n - 1

    while start + 1 <= end:
        mid = start + (end - start) // 2

        if array[mid - 1] < array[mid] > array[mid + 1]:
            return array[mid]
        elif array[mid] < array[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    return array[start]
    
    
    
lst = [1,4,6,5,4,5,4,2]
print(peak(lst))
