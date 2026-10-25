# ЗАДАЧА 2. Subarray Sum Equals K
#
# Дан массив целых чисел nums и число k.
#
# Нужно найти количество непрерывных подмассивов,
# сумма элементов которых равна k.
#
# Пример:
#
# nums = [1, 1, 1]
# k = 2
#
# Ответ:
# 2
#
# Подходящие подмассивы:
# [1, 1] — первые два элемента
# [1, 1] — последние два элемента
#
# Ещё пример:
#
# nums = [1, 2, 3]
# k = 3
#
# Ответ:
# 2
#
# Подходят:
# [1, 2]
# [3]
#
# Желательно решить быстрее, чем O(n^2).
#


from collections import defaultdict


def subarray_sum(nums, k):
    prefix_count = defaultdict(int)
    prefix_count[0] = 1

    prefix_sum = 0
    result = 0

    for num in nums:
        prefix_sum += num

        # сколько раз встречалась сумма (prefix_sum - k)?
        result += prefix_count[prefix_sum - k]

        prefix_count[prefix_sum] += 1

    return result

# Проверка:
if __name__ == '__main__':
    print(subarray_sum([1, 1, 1], 2))          # 2
    print(subarray_sum([1, 2, 3], 3))          # 2
    print(subarray_sum([1, -1, 0], 0))         # 3