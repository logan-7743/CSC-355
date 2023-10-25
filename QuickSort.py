def median_of_three(arr, low, high):
    mid_ind = (low + high) // 2
    temp = [arr[high], arr[mid_ind], arr[low]]
    pe = sorted(temp)
    return pe[1]

def partin(arr, low, high):
    med = median_of_three(arr, low, high)
    i = low - 1
    # Find the index of the median in the subarray
    med_indx = low + arr[low:high+1].index(med)
    arr[high], arr[med_indx] = arr[med_indx], arr[high]
    
    for j in range(low, high):
        if arr[j] < med:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            # print(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def QuickSort(arr,low, high):
    if(high-low>=2): print(arr)
    if low<high:
        piv=partin(arr,low,high)
        QuickSort(arr,low,piv-1)
        QuickSort(arr,piv+1,high)
    return arr
arr = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
