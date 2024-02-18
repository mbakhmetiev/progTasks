#/usr/bin/python

'''
    https://pythonist.ru/sortirovka-sliyaniem-dlya-teh-kto-ne-hochet-prosto-ispolzovat-sort/?ysclid=lsrgijuzke871637860
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    # i, j = 0, 0

    # Merge two sorted arrays
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

arr = [12, 4, 5, 6, 1, 22, 0, 1]
print("Original array: ", arr)
sorted_arr = merge_sort(arr)
print("Sorted array: ", sorted_arr)
