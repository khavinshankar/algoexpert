# time = O(nlogn) and space = O(n)
def mergeSort(arr):
    if len(arr) == 1: return arr

    mergeSortHelper(arr, 0, len(arr)-1, arr[:])
    return arr

def mergeSortHelper(main_arr, start, end, auxiliary_arr):
    if start == end: return

    mid = (start + end) // 2
    mergeSortHelper(auxiliary_arr, start, mid, main_arr)
    mergeSortHelper(auxiliary_arr, mid+1, end, main_arr)

    i = start
    j = mid+1
    k = start
    while i <= mid and j <= end:
        if auxiliary_arr[i] < auxiliary_arr[j]:
            main_arr[k] = auxiliary_arr[i]
            i += 1; k += 1
        else:
            main_arr[k] = auxiliary_arr[j]
            j += 1; k += 1
        
    while i <= mid:
        main_arr[k] = auxiliary_arr[i]
        i += 1; k += 1
    
    while j <= end:
        main_arr[k] = auxiliary_arr[j]
        j += 1; k += 1