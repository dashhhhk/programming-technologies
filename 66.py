import random
import time


class AVLNode:
    """Класс узла AVL-дерева"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Высота узла, изначально 1 для нового узла


class AVLTree:
    """Класс AVL-дерева"""

    def __init__(self):
        self.root = None

    def height(self, node):
        """Возвращает высоту узла (обрабатывает случай None)"""
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        """Обновляет высоту узла на основе высот его поддеревьев"""
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        """Вычисляет баланс-фактор узла (разница высот поддеревьев)"""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        """Правый поворот вокруг узла y"""
        x = y.left
        T2 = x.right

        # Выполняем поворот
        x.right = y
        y.left = T2

        # Обновляем высоты
        self.update_height(y)
        self.update_height(x)

        return x  # Новый корень поддерева

    def rotate_left(self, x):
        """Левый поворот вокруг узла x"""
        y = x.right
        T2 = y.left

        # Выполняем поворот
        y.left = x
        x.right = T2

        # Обновляем высоты
        self.update_height(x)
        self.update_height(y)

        return y  # Новый корень поддерева

    def insert(self, node, key):
        """Рекурсивная вставка ключа в поддерево с корнем node"""
        # 1. Обычная вставка в BST
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        # 2. Обновляем высоту текущего узла
        self.update_height(node)

        # 3. Проверяем баланс и балансируем при необходимости
        balance = self.balance_factor(node)

        # Левый-левый случай
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Правый-правый случай
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Левый-правый случай
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Правый-левый случай
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node  # Возвращаем неизмененный узел, если баланс в порядке

    def insert_key(self, key):
        """Публичный метод для вставки ключа"""
        self.root = self.insert(self.root, key)

    def find_min(self, node):
        """Находит узел с минимальным ключом в поддереве"""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, key):
        """Рекурсивное удаление ключа из поддерева с корнем node"""
        # 1. Обычное удаление из BST
        if node is None:
            return node

        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            # Узел с одним или без детей
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Узел с двумя детьми: получаем преемника (минимальный в правом поддереве)
            temp = self.find_min(node.right)
            node.key = temp.key
            node.right = self.delete(node.right, temp.key)

        # Если дерево стало пустым после удаления
        if node is None:
            return node

        # 2. Обновляем высоту текущего узла
        self.update_height(node)

        # 3. Проверяем баланс и балансируем при необходимости
        balance = self.balance_factor(node)

        # Левый-левый случай
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)

        # Левый-правый случай
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Правый-правый случай
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)

        # Правый-левый случай
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete_key(self, key):
        """Публичный метод для удаления ключа"""
        self.root = self.delete(self.root, key)

    def search(self, node, key):
        """Поиск ключа в поддереве с корнем node"""
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)

    def search_key(self, key):
        """Публичный метод для поиска ключа"""
        return self.search(self.root, key)

    def generate_random_tree(self, num_elements, min_val=1, max_val=100):
        """Генерирует дерево со случайными элементами"""
        elements = random.sample(range(min_val, max_val + 1), num_elements)
        for elem in elements:
            self.insert_key(elem)
        return elements


# Демонстрация работы AVL-дерева
if __name__ == "__main__":
    avl = AVLTree()

    # 1. Генерируем дерево со случайными элементами
    print("Генерация дерева со случайными элементами...")
    elements = avl.generate_random_tree(20, 1, 100)
    print("Сгенерированные элементы:", elements)

    print("\nЦентрированный обход дерева (отсортированные элементы):")
    avl.inorder_traversal(avl.root)
    print("\n")

    # 2. Выбираем случайный элемент для поиска
    search_key = random.choice(elements)
    print(f"Поиск элемента {search_key} в дереве...")

    # 3. Измеряем время поиска
    start_time = time.perf_counter()
    found = avl.search_key(search_key)
    end_time = time.perf_counter()

    if found:
        print(f"Элемент {search_key} найден в дереве.")
    else:
        print(f"Элемент {search_key} не найден в дереве.")

    print(f"Время поиска: {(end_time - start_time) * 1000:.6f} миллисекунд")

    # 4. Демонстрация удаления
    delete_key = random.choice(elements)
    print(f"\nУдаление элемента {delete_key} из дерева...")
    avl.delete_key(delete_key)

    print()