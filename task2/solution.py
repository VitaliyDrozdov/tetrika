from time import perf_counter
import csv
import os
from collections import defaultdict
import wikipediaapi

RUSSIAN_ALPHABET = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")


def get_animals_count():
    user_agent = "TestName/1.0 (https://test.com; test-email@test.com)"
    wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="ru")
    counter = defaultdict(int)

    root_page = wiki_wiki.page("Категория:Животные_по_алфавиту")

    if root_page.exists():
        for subcat in root_page.categorymembers.values():
            if subcat.namespace != wikipediaapi.Namespace.MAIN:
                continue
            letter = subcat.title[0].upper()
            if letter not in RUSSIAN_ALPHABET:
                continue
            counter[letter] += 1
    else:
        print("Корневая категория не найдена.")
        return counter
    return counter


def to_csv(counter):
    path = os.path.join(os.getcwd(), "beasts.csv")
    with open(path, "w", encoding="utf-8") as file_write:
        writer = csv.writer(file_write)
        for letter in RUSSIAN_ALPHABET:
            writer.writerow([letter, counter.get(letter, 0)])


if __name__ == "__main__":
    start = perf_counter()
    counter = get_animals_count()
    to_csv(counter)
    print(f"end_time: {perf_counter() - start}")
