import random
import string
import time
#from suffix_prefix import find_matching_pair_dict, find_matching_pair_bruteforce


# Генерация случайных слов
import random
import string

def generate_words(word_count: int, avg_words_length: int) -> list[str]:
    words_list: list = []
    # Добавляем русские символы к латинским
    alphabet = string.ascii_lowercase + 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
    for _ in range(word_count):
        length = random.randint(avg_words_length - 2, avg_words_length + 2)  # Разбег длины диапазона
        word: str = ''.join(random.choices(alphabet, k=length))  # Составление слов из смешанных букв
        words_list.append(word)  # Конечный список слов
    return words_list


if __name__ == '__main__':
    # Пример использования
    random_words = generate_words(5, 7)
    print(random_words)

    # Тестирование
    num_words = 500  # Количество слов
    avg_length = 10  # Средняя длина слова

    # Генерируем тестовые данные
    words = generate_words(num_words, avg_length)
    print(words)

    """
    Следующий текст только после выполнения писать,
    либо только в ознакомительных целях
    """

    # Тестируем брутфорс
    start = time.time()
    result_brute = find_matching_pair_bruteforce(words)
    end = time.time()
    print(f"Брутфорс: {result_brute}, Время: {end - start:.4f} секунд")

    # Тестируем словарь
    start = time.time()
    result_dict = find_matching_pair_dict(words)
    end = time.time()
    print(f"Словарь: {result_dict}, Время: {end - start:.4f} секунд")
