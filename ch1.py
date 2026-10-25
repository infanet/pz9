# ЗАДАЧА 1. Group Anagrams
#
# Дан список строк words.
# Нужно сгруппировать слова, которые являются анаграммами друг друга.
#
# Анаграммы — слова, состоящие из одинаковых букв
# в одинаковом количестве, но в разном порядке.
#
# Пример:
#
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#
# Ответ:
# [
#     ["eat", "tea", "ate"],
#     ["tan", "nat"],
#     ["bat"]
# ]
#
# Порядок групп и слов внутри групп не важен.
#
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)

    for word in words:
        key = tuple(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# Проверка:
if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams(["abc", "bca", "cab", "foo", "ofo", "bar"]))
    print(group_anagrams(["a"]))
    print(group_anagrams([]))