import random
import time


class AVLNode:
    def __init__(self, key):
        self.key = key      # Значение узла
        self.left = None    # Левый потомок
        self.right = None   # Правый потомок
        self.height = 1     # Высота поддерева (начальное значение = 1)


class AVLTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if not self.root:
            self.root = AVLNode(key)
        else:
            if not node:
                return AVLNode(key)
            elif key < node.key:
                node.left = self._insert(node.left, key)
            else:
                node.right = self._insert(node.right, key)

            node.height = 1 + max(self._get_height(node.left),
                                  self._get_height(node.right))

            balance = self._get_balance(node)

            if balance > 1 and key < node.left.key:
                return self._right_rotate(node)

            if balance < -1 and key > node.right.key:
                return self._left_rotate(node)

            if balance > 1 and key > node.left.key:
                node.left = self._left_rotate(node.left)
                return self._right_rotate(node)

            if balance < -1 and key < node.right.key:
                node.right = self._right_rotate(node.right)
                return self._left_rotate(node)

            return node


    def _delete(self, node, key):
        if not node:
            return node

        elif key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


    def _search(self, node, key):
        if node is None:
            return False
        elif key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left),
                           self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                           self._get_height(y.right))

        return y


def generate_random_tree(size):
    avl = AVLTree()
    elements = random.sample(range(1, 1000000), size)
    print(f"\nГенерация дерева из {size} элементов")
    for elem in elements:
        avl._insert(avl.root, elem)
    return avl, elements


def measure_search(avl, search_elem):
    print(f"\nПоиск элемента: {search_elem}")
    start_time = time.perf_counter()
    found = avl._search(avl.root,search_elem)
    end_time = time.perf_counter()

    print(f"Результат: {'найден' if found else 'не найден'}")
    print(f"Время поиска: {(end_time - start_time):.8f} сек")
    return end_time - start_time


if __name__ == "__main__":
    size = 10
    avl, elements = generate_random_tree(size)

    # Поиск существующего элемента
    existing_elem = random.choice(elements)
    measure_search(avl, existing_elem)

    # Поиск несуществующего элемента
    non_existent = max(elements) + 1
    measure_search(avl, non_existent)

    # Вставка нового элемента
    new_elem = max(elements) + 2
    print(f"\nВставка элемента: {new_elem}")

    avl._insert(avl.root, new_elem)
    measure_search(avl, new_elem)



    # Удаление существующего элемента
    elem_to_delete = random.choice(elements)
    print(f"\nУдаление элемента: {elem_to_delete}")

    deleted = avl._delete(avl.root, elem_to_delete)

    print(f"Результат: {'удален' if deleted else 'не найден'}")

