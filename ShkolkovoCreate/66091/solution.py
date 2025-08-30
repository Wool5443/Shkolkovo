# Откроем файл и считаем числа в список
file = open("17__1z92t.txt")
numbers = [int(i) for i in file]

# Создадим переменные для счётчика и минимальной суммы
count = 0
max_sum = 10005000

# Переменная для максимального числа, кратного 8
mx = 0
# Пройдёмся по всем числам
for i in range(len(numbers)):
    # Обновляем максимальное число
    if (numbers[i] > mx) and (numbers[i] % 8 == 0):
        mx = numbers[i]

# Пройдёмся по парам
for i in range(len(numbers) - 1):
    # Проверяем, что хотя бы одно число в паре больше mx
    if (numbers[i] > mx) or (numbers[i + 1] > mx):
        # Увеличиваем счётчик
        count += 1
        # Обновляем минимальную сумму
        if numbers[i] + numbers[i + 1] < max_sum:
            max_sum = numbers[i] + numbers[i + 1]

# Выведем ответ
print(count, max_sum)
