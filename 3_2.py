import time
import random

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: float) -> None:
        """Добавление элемента в конец очереди"""
        self.queue.append(item)

    def dequeue(self) -> float:
        """Удаление и возврат элемента из начала очереди"""
        if self.is_empty():
            raise IndexError("очередь пуста")
        return self.queue.pop(0)

    def peek(self) -> float:
        """Просмотр элемента в начале очереди без удаления"""
        if self.is_empty():
            raise IndexError("очередь пуста")
        return self.queue[0]

    def is_empty(self) -> bool:
        """Проверка, пуста ли очередь"""
        return len(self.queue) == 0

    def size(self) -> int:
        """Возвращает количество элементов в очереди"""
        return len(self.queue)

    def __str__(self) -> str:
        return str(self.queue)


class Node:
    def __init__(self, data: float):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None  # начало очереди
        self.rear = None  # конец очереди
        self._size = 0

    def enqueue(self, item: float) -> None:
        """Добавление элемента в конец очереди"""
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self) -> float:
        """Удаление и возврат элемента из начала очереди"""
        if self.is_empty():
            raise IndexError("очередь пуста")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return temp.data

    def peek(self) -> float:
        """Просмотр элемента в начале очереди без удаления"""
        if self.is_empty():
            raise IndexError("очередь пуста")
        return self.front.data

    def is_empty(self) -> bool:
        """Проверка, пуста ли очередь"""
        return self.front is None

    def size(self) -> int:
        """Возвращает количество элементов в очереди"""
        return self._size

    def __str__(self) -> str:
        """Вывод очереди в виде строки (для отладки)"""
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return " -> ".join(items) if items else "пусто"


if __name__ == "__main__":
    print("очередь на основе массива:")
    aq = ArrayQueue()
    aq.enqueue(1.5)
    aq.enqueue(2.7)
    aq.enqueue(3.1)
    print(f"очередь: {aq}")
    print(f"размер: {aq.size()}")
    print(f"первый элемент: {aq.peek()}")
    print(f"Dequeue: {aq.dequeue()}")
    print(f"Очередь после dequeue: {aq}")

    # Тестирование производительности для ArrayQueue
    start_time_array = time.time()
    test_array_queue = ArrayQueue()
    for _ in range(1000):
        random_float = round(random.uniform(1.0, 10.0), 2)
        test_array_queue.enqueue(random_float)
    while not test_array_queue.is_empty():
        test_array_queue.dequeue()
    time_array = time.time() - start_time_array
    print(f"Время выполнения: {time_array:.6f} сек")

    print("\nочередь на основе связного списка:")
    llq = LinkedListQueue()
    llq.enqueue(1.5)
    llq.enqueue(2.7)
    llq.enqueue(3.1)
    print(f"Очередь: {llq}")
    print(f"Размер: {llq.size()}")
    print(f"Первый элемент: {llq.peek()}")
    print(f"Dequeue: {llq.dequeue()}")
    print(f"Очередь после dequeue: {llq}")

    # Тестирование производительности для LinkedListQueue
    start_time_linked = time.time()
    test_linked_queue = LinkedListQueue()
    for _ in range(1000):
        random_float = round(random.uniform(1.0, 10.0), 2)
        test_linked_queue.enqueue(random_float)
    while not test_linked_queue.is_empty():
        test_linked_queue.dequeue()
    time_linked = time.time() - start_time_linked
    print(f"Время выполнения: {time_linked:.6f} сек")

    # Сравнение производительности
    print("\nСравнение производительности:")
    print(f"ArrayQueue: {time_array:.6f} сек")
    print(f"LinkedListQueue: {time_linked:.6f} сек")
    difference = abs(time_array - time_linked)
    if time_array < time_linked:
        print(f"ArrayQueue быстрее на {difference:.6f} сек")
    else:
        print(f"LinkedListQueue быстрее на {difference:.6f} сек")