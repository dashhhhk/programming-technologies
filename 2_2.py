import random
from LinkedList import LinkedList
def generate_random_list(length, min_val=0, max_val=100):
    """
    Генерирует псевдо-случайный список заданной длины, используя класс LinkedList.

    """
    linked_list = LinkedList()
    random_data = [random.randint(min_val, max_val) for _ in range(length)]
    linked_list.create_list(random_data)
    return linked_list

if __name__ == '__main__':
    random_list = generate_random_list(10, 1, 20)

    print("Случайный список:")
    random_list.print_list()


