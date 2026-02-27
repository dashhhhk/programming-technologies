import time
import random


class ArrayDeque:
    def __init__(self):
        self.deque = []

    def add_front(self, item: str) -> None:
        """добавление элемента в начало дека"""
        self.deque.insert(0, item)

    def add_rear(self, item: str) -> None:
        """Добавление элемента в конец дека"""
        self.deque.append(item)

    def remove_front(self) -> str:
        """Удаление и возврат элемента из начала дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.deque.pop(0)

    def remove_rear(self) -> str:
        """Удаление и возврат элемента из конца дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.deque.pop()

    def peek_front(self) -> str:
        """Просмотр элемента в начале дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.deque[0]

    def peek_rear(self) -> str:
        """Просмотр элемента в конце дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.deque[-1]

    def is_empty(self) -> bool:
        """Проверка, пуст ли дек"""
        return len(self.deque) == 0

    def size(self) -> int:
        """Возвращает количество элементов в деке"""
        return len(self.deque)

    def __str__(self) -> str:
        return str(self.deque)


class Node:
    def __init__(self, data: str):
        self.data = data
        self.next = None
        self.prev = None


class LinkedListDeque:
    def __init__(self):
        self.front = None  # начало дека
        self.rear = None  # конец дека
        self._size = 0

    def add_front(self, item: str) -> None:
        """Добавление элемента в начало дека"""
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self._size += 1

    def add_rear(self, item: str) -> None:
        """Добавление элемента в конец дека"""
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def remove_front(self) -> str:
        """Удаление и возврат элемента из начала дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        temp = self.front
        if self.front == self.rear:  # только один элемент
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self._size -= 1
        return temp.data

    def remove_rear(self) -> str:
        """Удаление и возврат элемента из конца дека"""
        if self.is_empty():
            raise IndexError("дек пуст")
        temp = self.rear
        if self.front == self.rear:  # только один элемент
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self._size -= 1
        return temp.data

    def peek_front(self) -> str:
        """Просмотр элемента в начале дека без удаления"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.front.data

    def peek_rear(self) -> str:
        """Просмотр элемента в конце дека без удаления"""
        if self.is_empty():
            raise IndexError("дек пуст")
        return self.rear.data

    def is_empty(self) -> bool:
        """Проверка, пуст ли дек"""
        return self.front is None

    def size(self) -> int:
        """Возвращает количество элементов в деке"""
        return self._size

    def __str__(self) -> str:
        """Вывод дека в виде строки (для отладки)"""
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return " <-> ".join(items) if items else "пустой"


def generate_random_string(length=5):
    """Генерация случайной строки фиксированной длины"""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for _ in range(length))


if __name__ == "__main__":
    print("дек на основе массива")
    ad = ArrayDeque()
    ad.add_front('a')
    ad.add_rear('b')
    ad.add_front('c')
    ad.add_rear('d')
    print(f"дек: {ad}")
    print(f"размер: {ad.size()}")
    print(f"первый элемент: {ad.peek_front()}")
    print(f"последний элемент: {ad.peek_rear()}")
    print(f"удаление первого элемента : {ad.remove_front()}")
    print(f"удаление последнего элемента: {ad.remove_rear()}")
    print(f"дек после удалений: {ad}")

    # Тестирование производительности для ArrayDeque
    start_time_array = time.time()
    test_array_deque = ArrayDeque()
    for _ in range(1000):
        # Чередуем добавление в начало и в конец
        random_str = generate_random_string()
        if random.random() > 0.5:
            test_array_deque.add_front(random_str)
        else:
            test_array_deque.add_rear(random_str)

    # Чередуем удаление из начала и из конца
    while not test_array_deque.is_empty():
        if random.random() > 0.5:
            test_array_deque.remove_front()
        else:
            test_array_deque.remove_rear()
    time_array = time.time() - start_time_array
    print(f"\nВремя выполнения: {time_array:.6f} сек")

    print("\nдек на основе связного списка")
    lld = LinkedListDeque()
    lld.add_front('a')
    lld.add_rear('b')
    lld.add_front('c')
    lld.add_rear('d')
    print(f"дек: {lld}")
    print(f"размер: {lld.size()}")
    print(f"первый элемент: {lld.peek_front()}")
    print(f"последний элемент: {lld.peek_rear()}")
    print(f"удаление первого элемента: {lld.remove_front()}")
    print(f"удаление последнего элемента: {lld.remove_rear()}")
    print(f"дек после удалений: {lld}")

    # Тестирование производительности для LinkedListDeque
    start_time_linked = time.time()
    test_linked_deque = LinkedListDeque()
    for _ in range(1000):
        # Чередуем добавление в начало и в конец
        random_str = generate_random_string()
        if random.random() > 0.5:
            test_linked_deque.add_front(random_str)
        else:
            test_linked_deque.add_rear(random_str)

    # Чередуем удаление из начала и из конца
    while not test_linked_deque.is_empty():
        if random.random() > 0.5:
            test_linked_deque.remove_front()
        else:
            test_linked_deque.remove_rear()
    time_linked = time.time() - start_time_linked
    print(f"\nВремя выполнения: {time_linked:.6f} сек")

    # Сравнение производительности
    print("\nСравнение производительности:")
    print(f"ArrayDeque: {time_array:.6f} сек")
    print(f"LinkedListDeque: {time_linked:.6f} сек")
    difference = abs(time_array - time_linked)
    if time_array < time_linked:
        print(f"ArrayDeque быстрее на {difference:.6f} сек")
    else:
        print(f"LinkedListDeque быстрее на {difference:.6f} сек")