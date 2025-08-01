def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)

#Selection Sort is a simple comparison-based sorting algorithm.
#It works by repeatedly finding the minimum (or maximum) element from the unsorted part of the array and moving it to the beginning.
