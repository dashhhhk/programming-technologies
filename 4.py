import random

def counting_sort(arr):
    """Сортировка подсчётом (Counting Sort)"""
    length = max(arr) + 1  # кол-во ячеек для счетчиков
    counters = [0] * length  # инициализируем список счетчик
    res = [] * length  # результат
    #считаем кол-во вхождений і в список а
    for i in arr:
        counters[i] += 1
    # запись отсортированного списка
    for i in range(length):  # i встречается counters[i] раз
        res += [i] * counters[i]
    return res


def insertion_sort(arr):
    """Сортировка вставками (Insertion Sort)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr):
    """Сортировка Шелла (Shell Sort)"""
    n = len(arr)
    gap = n // 2  # начальный интервал

    while gap > 0:
        for i in range(gap, n):  # проход по подмассивам
            temp = arr[i]  # текущий элемент для вставки
            j = i
            #сдвигаем элементы, пока не найдем место для temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp  # вставляем temp на правильное место
        gap //= 2  # уменьшаем интервал
    return arr

def selection_sort(arr):
    """Сортировка выбором (Selection Sort)"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def heap_sort(arr):
    """Пирамидальная сортировка (Heap Sort)"""

    def heapify(arr, n, i):
        largest = i  # текущий узел (родитель)
        left = 2 * i + 1  # левый потомок
        right = 2 * i + 2  # правый потомок
        #если левый потомок существует и больше родителя
        if left < n and arr[left] > arr[largest]:
            largest = left
        #если правый потомок существует и больше текущего largest
        if right < n and arr[right] > arr[largest]:
            largest = right
        #если largest изменился, меняем местами и рекурсивно heapify
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def bubble_sort(arr):
    """Сортировка пузырьком (Bubble Sort)"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """Быстрая сортировка (Quick Sort)"""
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        l_arr = [n for n in arr if n < q]
        e_arr = [n for n in arr if n == q]
        b_arr = [n for n in arr if n > q]
        return quick_sort(l_arr) + e_arr + quick_sort(b_arr)

def merge_sort(arr):
    """Сортировка слиянием (Merge Sort)"""

    def merge(left, right):
        result = []  # итоговый отсортированный массив
        i = j = 0  # указатели для left и right

        # пка есть элементы в обоих массивах
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])  # берем меньший элемент из left
                i += 1
            else:
                result.append(right[j])  # берем меньший элемент из right
                j += 1

        #добавляем оставшиеся элементы (если left или right закончился раньше)
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", arr)

    print("Сортировка подсчётом:", counting_sort(arr.copy()))
    print("Сортировка вставками:", insertion_sort(arr.copy()))
    print("Сортировка Шелла:", shell_sort(arr.copy()))
    print("Сортировка выбором:", selection_sort(arr.copy()))
    print("Пирамидальная сортировка:", heap_sort(arr.copy()))
    print("Сортировка пузырьком:", bubble_sort(arr.copy()))
    print("Быстрая сортировка:", quick_sort(arr.copy()))
    print("Сортировка слиянием:", merge_sort(arr.copy()))