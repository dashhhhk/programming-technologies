import random
import time

def generate_random_array(length, min_val=0, max_val=100):
    """генерация массива случайных чисел."""
    return [random.randint(min_val, max_val) for _ in range(length)]

def timer(func, *args):

    start_time = time.perf_counter()  # Используем perf_counter для большей точности (милисекунды)
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time


def first(arr, value):
    """Находит индекс первого вхождения значения в массиве."""
    operations = 0
    for i in range(len(arr)):
        operations += 1
        operations += 1
        if arr[i] == value:
            return i, operations

    return -1, operations


def second(arr, value):
    """Подсчитывает количество вхождений значения в массиве."""
    count = 0
    operations = 0
    for i in range(len(arr)):
        operations += 1
        operations += 1
        if arr[i] == value:
            count += 1

    return count, operations


if __name__ == "__main__":
    array_length = 100
    random_array = generate_random_array(array_length)
    search_value = 42
    print(f"сгенерированный массив: {random_array}" )


    result, execution_time = timer(first, random_array, search_value)
    index, steps = result
    if index != -1:
        print(f"Первое вхождение {search_value} найдено по индексу: {index}")
    else:
        print(f"{search_value} не найдено в массиве.")
    print(f"Число операций (first): {steps}")
    print(f"Время выполнения (first): {execution_time:.5e} секунд")


    result, execution_time = timer(second, random_array, search_value)
    count, steps = result
    print(f"Количество вхождений {search_value}: {count}")
    print(f"Число операций (second): {steps}")
    print(f"Время выполнения (second): {execution_time:.5e} секунд")
