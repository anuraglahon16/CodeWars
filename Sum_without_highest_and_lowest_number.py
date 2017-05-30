def sum_array(arr):
    if arr and len(arr)>1:
        return sum(arr)-max(arr)-min(arr)
    else:
        return 0
