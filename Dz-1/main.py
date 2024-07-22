# Пузырьковая сортировка (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Флаг для отслеживания, произошли ли обмены в текущем проходе
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Обмен элементов
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не произошло ни одного обмена, массив уже отсортирован
        if not swapped:
            break
    return arr


# Быстрая сортировка (Quick Sort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Выбор опорного элемента
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        # Рекурсивная сортировка левой и правой частей
        return quick_sort(left) + middle + quick_sort(right)


# Сортировка выбором (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Поиск минимального элемента в несортированной части массива
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Обмен найденного минимального элемента с первым элементом несортированной части
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Сортировка вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Сдвиг элементов массива, которые больше текущего элемента, вправо
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Сортировка слиянием (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Разделение массива на две половины
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    # Слияние двух половин
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Добавление оставшихся элементов
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Пример использования всех сортировок
if __name__ == "__main__":
    arr = [64, 34, -7, 25, 0, 12, 22, 11, 90, -11, 0, -5, 89, 34, 99, -7, 0]

    print("Original array:", arr)

    print("Bubble Sorted array:", bubble_sort(arr.copy()))
    print("Quick Sorted array:", quick_sort(arr.copy()))
    print("Selection Sorted array:", selection_sort(arr.copy()))
    print("Insertion Sorted array:", insertion_sort(arr.copy()))
    print("Merge Sorted array:", merge_sort(arr.copy()))

# Original array: [64, 34, -7, 25, 0, 12, 22, 11, 90, -11, 0, -5, 89, 34, 99, -7, 0]
# Bubble Sorted array: [-11, -7, -7, -5, 0, 0, 0, 11, 12, 22, 25, 34, 34, 64, 89, 90, 99]
# Quick Sorted array: [-11, -7, -7, -5, 0, 0, 0, 11, 12, 22, 25, 34, 34, 64, 89, 90, 99]
# Selection Sorted array: [-11, -7, -7, -5, 0, 0, 0, 11, 12, 22, 25, 34, 34, 64, 89, 90, 99]
# Insertion Sorted array: [-11, -7, -7, -5, 0, 0, 0, 11, 12, 22, 25, 34, 34, 64, 89, 90, 99]
# Merge Sorted array: [-11, -7, -7, -5, 0, 0, 0, 11, 12, 22, 25, 34, 34, 64, 89, 90, 99]
