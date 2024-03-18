import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Визначення функцій для тестування
def test_merge_sort(arr):
    merge_sort(arr)

def test_insertion_sort(arr):
    insertion_sort(arr)

def test_timsort(arr):
    sorted(arr)

# Генерація тестових даних
sizes = [100, 1000, 10000]
test_data = {size: [random.randint(0, 100000) for _ in range(size)] for size in sizes}

# Заміри часу виконання
results = {}
for size in sizes:
    results[size] = {}
    arr = test_data[size].copy()
    results[size]['Merge Sort'] = timeit.timeit(lambda: test_merge_sort(arr.copy()), number=1)
    arr = test_data[size].copy()
    results[size]['Insertion Sort'] = timeit.timeit(lambda: test_insertion_sort(arr.copy()), number=1)
    arr = test_data[size].copy()
    results[size]['Timsort'] = timeit.timeit(lambda: test_timsort(arr.copy()), number=1)

print(results)
