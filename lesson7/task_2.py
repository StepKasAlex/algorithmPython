"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random


def sorting(list_):
    if len(list_) > 1:
        middle = len(list_) // 2
        left = list_[:middle]
        right = list_[middle:]

        sorting(left)
        sorting(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_[k] = left[i]
                i = i + 1
            else:
                list_[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            list_[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            list_[k] = right[j]
            j = j + 1
            k = k + 1


nums = 15
list_ = [random.random()*50 for i in range(nums)]

print(f"{list_}")
sorting(list_)
print(f"{list_}")
