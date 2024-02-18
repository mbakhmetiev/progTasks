#/usr/bin/python

'''
    Быстрая сортировка
    -> 1-е повтороение рекурсии
        -  arr  = [10, 5, 2]
        -  pivot = 10
        -  less_than_pivot = [5, 2]
        -  greater_than_pivot = []
        -  return quicksort([5 ,2]) + [10] + quicksort([])
    -> 2-е повтороение рекурсии
        -  arr  = [5, 2]
        -  pivot = 5
        -  less_than_pivot = [2]
        -  greater_than_pivot = []
        -  return quicksort([2]) + [5] + quicksort([]) # Важно! здесь помимо
           вызова рекурсии, добавляется спсиок[10]
    -> 3-е повтороение рекурсии
        -  arr  = [2]
        -  return [2] # Сработал базовый случай рекурсии
    Итоговый список: [2] + [5] + [10] = [2, 5, 10]
'''

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [i for i in arr[1:] if i <= pivot]
        grater_than_pivot = [i for i in arr[1:] if i > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(grater_than_pivot)

arr = [12, 4, 5, 6, 7, 3, 1, 15]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
