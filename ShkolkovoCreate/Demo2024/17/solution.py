# Открываем файл
file = open("17_2024.txt")

# Считываем числа из файла
numbers = [int(s) for s in file]

# Находим максимальное число, оканчивающееся на 13
max_div13 = max(x for x in numbers if x % 100 == 13)

# Вводим счётчик подходящик троек и переменную для максимальной суммы
count = 0
max_sum = 0

# Проходимся по тройкам
for i in range(len(numbers) - 2):
    # Срезом берём текущую тройку
    triplet = numbers[i:i+3]
    # Находим сумму тройки
    triplet_sum = sum(triplet)
    # Считаем, сколько трёхзначных чисел в тройке
    count_three_digits = sum(100 <= x <= 999 for x in triplet)

    # Проверяем, что два трёхзначных чисел
    # и сумма тройки не больше максимального числа, кратного 13
    if count_three_digits == 2 and triplet_sum <= max_div13:
        # Увеличиваем счётчик
        count += 1
        # Обновляем максимальную сумму
        max_sum = max(max_sum, triplet_sum)

# Выводим ответ
print(count, max_sum)  # 959 97471
