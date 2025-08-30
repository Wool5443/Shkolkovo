# Откроем файл и считаем числа в список
file = open("17__1z92u.txt")
numbers = [int(i) for i in file]

# Для подсчёта среднего нужно найти количество и сумму чисел, кратных 4
count_4 = 0
sum_4 = 0
# Пройдёмся по всем числам
for i in range(len(numbers)):
    # Если число кратно 4, посчитаем его в количество и в сумму
    if numbers[i] % 4 == 0:
        count_4 += 1
        sum_4 += numbers[i]
# Найдём среднее арифметическое
average = sum_4 / count_4

# Введём переменные для максимальной суммы и количества пар
max_sum = 0
count_pairs = 0
# Пройдёмся по парам
for i in range(len(numbers) - 1):
    # Проверим, что хотя бы одно число в паре больше среднего
    if (numbers[i] > average) or (numbers[i + 1] > average):
        # Увеличим счётчик
        count_pairs += 1
        # Обновим максимальную сумму
        if numbers[i] + numbers[i + 1] > max_sum:
            max_sum = numbers[i] + numbers[i + 1]

# Выведем ответ
print(count_pairs, max_sum)
