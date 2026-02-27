class NaiveSearch:
    @staticmethod
    def search(text, pattern):
        """
        Наивный алгоритм поиска подстроки
        Сложность: O(n*m), n - длина текста, m - длина шаблона
        """
        n = len(text)
        m = len(pattern)
        positions = [] #список для хранения позиций где найден шаблон

        for i in range(n - m + 1): #перебор стартовых позиций
            j = 0 #индекс для сравнения символов шаблона
            #пока символы совпадают и не достигнут конец шаблона
            while j < m and text[i + j] == pattern[j]:
                j += 1
            if j == m:
                positions.append(i) #если дошли до конца шаблона совпадение найдено и добавляем позицию в список

        return positions


class KMPSearch:
    @staticmethod
    def _compute_lps(pattern):
        """
        Вычисление префикс-функции

        """
        lps = [0] * len(pattern)  #инициализация массива префикс-функции
        length = 0  #длина предыдущего наибольшего префикса-суффикса
        i = 1  # индекс для прохода по шаблону

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                # если символы совпадают, увеличиваем длину
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # если не совпадают, но длина не нулевая, возвращаемся назад
                    length = lps[length - 1]
                else:
                    # если длина нулевая, просто записываем 0 и идем дальше
                    lps[i] = 0
                    i += 1
        return lps

    @staticmethod
    def search(text, pattern):
        """
        Алгоритм Кнута-Морриса-Пратта
        Сложность: O(n + m), где n - длина текста, m - длина шаблона

        """
        n = len(text)
        m = len(pattern)
        positions = []  # Список для хранения позиций совпадений

        lps = KMPSearch._compute_lps(pattern)  # Вычисляем префикс-функцию

        i = 0  #индекс для текста
        j = 0  # для шаблона

        while i < n:
            if pattern[j] == text[i]:
                # если символы совпадают, двигаемся дальше
                i += 1
                j += 1

                if j == m:
                    # если дошли до конца шаблона - нашли совпадение
                    positions.append(i - j)
                    # используем lps для сдвига шаблона
                    j = lps[j - 1]
            else:
                if j != 0:
                    # используем lps для перехода при несовпадении
                    j = lps[j - 1]
                else:
                    # если j=0, просто сдвигаемся по тексту
                    i += 1

        return positions


class BoyerMooreSearch:
    @staticmethod
    def _make_bad_char_table(pattern):
        """
        Создание таблицы плохих символов
        """
        table = {} #хранение последних позиций символов
        m = len(pattern)

        for i in range(m):
            table[pattern[i]] = i

        return table

    @staticmethod
    def _make_good_suffix_table(pattern):
        """
        Создание таблицы хороших суффиксов

          1. Нахождение границ для каждого суффикса
          2. Заполнение таблицы на основе найденных границ

        """
        m = len(pattern)
        table = [0] * (m + 1)  # Таблица хороших суффиксов
        border = [0] * (m + 1)  # Массив для хранения границ

        # Этап 1: Нахождение границ
        i = m  # Начинаем с конца шаблона
        j = m + 1  # Фиктивная позиция за шаблоном
        border[i] = j  # Граница для полного шаблона

        while i > 0:
            # ищем границу
            while j <= m and pattern[i - 1] != pattern[j - 1]:
                if table[j] == 0:
                    table[j] = j - i  #запоминаем сдвиг
                j = border[j]  #переходим к следующей границе
            i -= 1
            j -= 1
            border[i] = j  #запоминаем найденную границу

        # Этап 2: Заполнение таблицы
        j = border[0]  #начинаем с границы для всего шаблона
        for i in range(m + 1):
            if table[i] == 0:
                table[i] = j  #заполняем пропуски
            if i == j:
                j = border[j]  #переходим к следующей границе

        return table

    @staticmethod
    def search(text, pattern):
        """
        Алгоритм Бойера-Мура
        Сложность: O(n/m) в лучшем случае, O(n*m) в худшем
        """
        n = len(text)
        m = len(pattern)
        positions = []  # Список для хранения позиций совпадений

        # Создаем таблицы
        bad_char = BoyerMooreSearch._make_bad_char_table(pattern)
        good_suffix = BoyerMooreSearch._make_good_suffix_table(pattern)

        s = 0  # Текущий сдвиг шаблона относительно текста
        while s <= n - m:
            j = m - 1  # Начинаем сравнение с конца шаблона

            # Пока символы совпадают, идем назад по шаблону
            while j >= 0 and pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                # если дошли до начала шаблона - совпадение найдено
                positions.append(s)
                # сдвигаем шаблон по правилу хорошего суффикса
                s += good_suffix[0]
            else:
                # вычисляем сдвиг по обеим эвристикам
                bc_shift = j - bad_char.get(text[s + j], -1)  # Сдвиг по плохому символу
                gs_shift = good_suffix[j + 1]  # Сдвиг по хорошему суффиксу
                # выбираем максимальный сдвиг
                s += max(bc_shift, gs_shift)

        return positions


class RabinKarpSearch:
    @staticmethod
    def _hash(s, base=256, mod=101):
        """
        Вычисление хеша строки
        - Полиномиальный хеш

        """
        h = 0  # Инициализация хеша
        for ch in s:
            # Обновляем хеш для каждого символа
            h = (h * base + ord(ch)) % mod
        return h

    @staticmethod
    def _rehash(old_hash, old_char, new_char, m, base=256, mod=101):
        """
        Пересчет хеша при сдвиге окна

        """
        # Удаляем вклад старого символа и добавляем новый
        new_hash = (old_hash - ord(old_char) * pow(base, m - 1, mod)) % mod
        new_hash = (new_hash * base + ord(new_char)) % mod
        return new_hash

    @staticmethod
    def search(text, pattern):
        """
        Алгоритм Рабина-Карпа
        Сложность: O(n+m), O(n*m) в худшем случае

        """
        n = len(text)
        m = len(pattern)
        positions = []  # Список для хранения позиций совпадений

        base = 256  # Размер алфавита (ASCII)
        mod = 101   # Простое число для хеширования

        # Вычисляем хеш шаблона и первого окна текста
        pattern_hash = RabinKarpSearch._hash(pattern, base, mod)
        window_hash = RabinKarpSearch._hash(text[:m], base, mod)

        # Предварительно вычисляем base^(m-1) mod mod для быстрого rehash
        h_pow = pow(base, m - 1, mod)

        # Проходим по всем возможным позициям окна в тексте
        for i in range(n - m + 1):
            if pattern_hash == window_hash:
                # При совпадении хешей проверяем посимвольно
                if text[i:i + m] == pattern:
                    positions.append(i)

            if i < n - m:
                # Обновляем хеш для следующего окна
                window_hash = RabinKarpSearch._rehash(
                    window_hash, text[i], text[i + m], m, base, mod
                )

        return positions


if __name__ == "__main__":
    text = "ABSBBABCOA"
    pattern = "BA"

    print("Наивный алгоритм:", NaiveSearch.search(text, pattern))
    print("КМП алгоритм:", KMPSearch.search(text, pattern))
    print("Бойер-Мур алгоритм:", BoyerMooreSearch.search(text, pattern))
    print("Рабин-Карп алгоритм:", RabinKarpSearch.search(text, pattern))