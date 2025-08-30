# Откроем файл и считаем числа в список a
file = open("17__1z92x.txt")
numbers = [int(i) for i in file]

# Заведём переменные для счётчика и минимальной суммы
count = 0
min_sum = 10005000

# Переберём последовательные тройки
for i in range(len(numbers) - 2):
    # Проверим, что хотя бы одно число в тройке оканчивается на 7
    if ((numbers[i] % 10 == 7) or (numbers[i + 1] % 10 == 7) or (numbers[i + 2] % 10 == 7)):
        # Проверим, что сумма тройки кратна 6
        if (numbers[i] + numbers[i + 1] + numbers[i + 2]) % 6 == 0:
            # Тройка подошла -- увеличиваем счётчик
            count += 1
            # Обновляем минимальную сумму
            if numbers[i] + numbers[i + 1] + numbers[i + 2] < min_sum:
                min_sum = numbers[i] + numbers[i + 1] + numbers[i + 2]

# Выводим ответ
print(count, min_sum)
