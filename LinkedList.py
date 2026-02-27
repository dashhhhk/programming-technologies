class Node:
    """
    Класс, представляющий узел односвязного списка.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Класс, представляющий односвязный список.
    """
    def __init__(self):
        self.head = None
        self.size = 0  # Отслеживаем размер списка для повышения эффективности

    def create_list(self, data):
        """
        Создает список из переданных данных.  Заменяет текущий список.

        """
        self.head = None
        self.size = 0
        for item in data:
            self.insert_at_end(item)

    def print_list(self):
        """
        Выводит элементы списка на экран.

        """
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    def insert_at_end(self, data):
        """
        Вставляет новый элемент в конец списка.

        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1



    def delete_element(self, data):
        """
        Удаляет первый элемент с заданным значением из списка.

        """
        current = self.head
        previous = None
        while current:
            if current.data == data:
                break
            previous = current
            current = current.next

        if current is None:
            print("Элемент не найден.")
            return  # Элемент не найден

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        self.size -= 1

    def search_element(self, data):
        """
        Ищет элемент в списке и возвращает True, если элемент найден, иначе False.

        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def is_empty(self):
        """
        Проверяет, является ли список пустым.

        """
        return self.head is None

    def delete_list(self):
        """
        Удаляет все элементы из списка.

        """
        self.head = None
        self.size = 0

if __name__ == '__main__':
        linked_list = LinkedList()

        # Создание списка
        data = [1, 2, 3, 4, 5]
        linked_list.create_list(data)
        print("Список:")
        linked_list.print_list()

        # Вставка элемента в конец
        linked_list.insert_at_end(6)
        print("Список после вставки в конец:")
        linked_list.print_list()

        # Удаление элемента
        linked_list.delete_element(7)
        print("Список после удаления:")
        linked_list.print_list()

        # Поиск элемента
        search_result = linked_list.search_element(4)
        print("Результат поиска элемента 4:", search_result)

        search_result = linked_list.search_element(10)
        print("Результат поиска элемента 10:", search_result)

        # Проверка пустоты списка
        is_empty = linked_list.is_empty()
        print("Список пуст:", is_empty)

        # Удаление списка
        linked_list.delete_list()
        print("Список после удаления:")
        is_empty = linked_list.is_empty()
        print("Список пуст:", is_empty)