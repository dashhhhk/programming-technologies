import time
import random

class ArrayStack:
    def __init__(self, capacity):
        """
        Инициализация стека с заданной емкостью
        """
        self.capacity = capacity          # максимальная емкость стека
        self.stack = [None] * capacity    # массив для хранения элементов
        self.top = -1                     # индекс вершины стека (-1 означает пустой стек)

    def push(self, item):
        """
        Добавление элемента в стек
        """
        if self.is_full():
            raise Exception("стек переполнен")
        self.top += 1
        self.stack[self.top] = float(item)  # вещественное число для добавления

    def pop(self):
        """
        Удаление и возврат верхнего элемента стека
        """
        if self.is_empty():
            raise Exception("стек пуст")
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        """
        Просмотр верхнего элемента без его удаления
        """
        if self.is_empty():
            raise Exception("стек пуст")
        return self.stack[self.top]

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return self.top == -1

    def is_full(self):
        """Проверка, заполнен ли стек"""
        return self.top == self.capacity - 1

    def size(self):
        """Текущий размер стека"""
        return self.top + 1

    def __str__(self):
        """Строковое представление стека"""
        if self.is_empty():
            return "[]"
        return str(self.stack[:self.top + 1])

class Node:
    """Узел связного списка"""
    def __init__(self, data):
        self.data = float(data) # хранение вещественного числа
        self.next = None  # ссылка на следующий узел

class LinkedListStack:
    """Реализация стека на основе связного списка"""
    def __init__(self):
        self.top_node = None  # вершина стека (последний добавленный элемент)
        self._size = 0  # текущий размер стека

    def push(self, item):
        """
        Добавление элемента в стек
        """
        new_node = Node(item)  # новый узел, item: вещественное число для добавления
        new_node.next = self.top_node  # новый узел ссылается на текущую вершину
        self.top_node = new_node  # обновляем вершину стека
        self._size += 1

    def pop(self):
        """
        Удаление и возврат верхнего элемента стека
        """
        if self.is_empty():
            raise Exception("стек пуст")
        item = self.top_node.data  # сохраняем данные вершины
        self.top_node = self.top_node.next  # перемещаем вершину на следующий узел
        self._size -= 1
        return item

    def peek(self):
        """
        Просмотр верхнего элемента без его удаления
        """
        if self.is_empty():
            raise Exception("стек пуст")
        return self.top_node.data

    def is_empty(self):
        """Проверка, пуст ли стек"""
        return self.top_node is None

    def size(self):
        """Текущий размер стека"""
        return self._size

    def __str__(self):
        """Строковое представление стека"""
        elements = []
        current = self.top_node
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return "[" + ", ".join(reversed(elements)) + "]" if elements else "[]"

if __name__ == "__main__":
    print("\nстек на основе массива")
    # создание стека из 5 элементов
    stack = ArrayStack(5)

    # элементы
    stack.push(3.14)
    stack.push(2.71)
    stack.push(1.41)

    # Тестирование производительности
    start_time_array = time.time()
    test_stack = ArrayStack(1000)  # создаем новый стек для теста
    for _ in range(1000):
        random_float = round(random.uniform(1.0, 10.0), 2)
        test_stack.push(random_float)
    while not test_stack.is_empty():
        test_stack.pop()
    time_array = time.time() - start_time_array

    print(f"  Время выполнения: {time_array:.6f} сек")

    print(f"стек: {stack}")
    print(f"верхний элемент: {stack.peek()}")

    print(f"удаление элемента: {stack.pop()}")
    print(f"удаление элемента: {stack.pop()}")
    print(f"стек: {stack}")

    # Проверка состояния
    print(f"стек пуст: {stack.is_empty()}")  # False
    print(f"размер стека: {stack.size()}")      # 1

    print("\nстек на основе связного списка")
    # стек
    stack = LinkedListStack()

    # элементы
    stack.push(3.14)
    stack.push(2.71)
    stack.push(1.41)

    # Тестирование производительности
    start_time_linked = time.time()
    test_linked_stack = LinkedListStack()
    for _ in range(1000):
        random_float = round(random.uniform(1.0, 10.0), 2)
        test_linked_stack.push(random_float)
    while not test_linked_stack.is_empty():
        test_linked_stack.pop()
    time_linked = time.time() - start_time_linked

    print(f"  Время выполнения: {time_linked:.6f} сек")

    print(f"стек: {stack}")
    print(f"верхний элемент: {stack.peek()}")

    print(f"удаление элемента: {stack.pop()}")
    print(f"удаление элемента: {stack.pop()}")
    print(f"стек: {stack}")

    # Проверка состояния
    print(f"стек пуст: {stack.is_empty()}")  # False
    print(f"размер стека: {stack.size()}")  # 1

    # Сравнение производительности
    print("\nСравнение производительности:")
    print(f"ArrayDeque: {time_array:.6f} сек")
    print(f"LinkedListDeque: {time_linked:.6f} сек")
    difference = abs(time_array - time_linked)
    if time_array < time_linked:
        print(f"ArrayDeque быстрее на {difference:.6f} сек")
    else:
        print(f"LinkedListDeque быстрее на {difference:.6f} сек")