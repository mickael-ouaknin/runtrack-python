def my_sort(arr):
    n = len(arr)
    total_swaps = 0

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total_swaps += 1
        
        print(f"After {i+1} iterations, total swaps: {total_swaps}")
    
    print(f"Total swaps: {total_swaps}")
    
    return arr
arr = [22, 11, 25, 64, 34, 90, 12]

sorted_arr = my_sort(arr)

print(f"Sorted array: {sorted_arr}")