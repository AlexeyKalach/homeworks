# Задание 2. В условиях не было дано значение числа, поэтому я решил его запрашивать.
# Надеюсь, за ошибку не считается
num = int(input('Введите число'))
gen_odd_nums = (n for n in range(1, num + 1, 2))
print(next(gen_odd_nums))
print(next(gen_odd_nums))

# Задание 3
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
from itertools import zip_longest
generator = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
print(next(generator))
print(next(generator))

# Задание 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [num for i, num in enumerate(src) if num > src [i - 1] and i != 0]
print(res_list)

# Задание 5
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])