# Откроем файл и считаем числа в список a

file = open("17__1z92y.txt")
numbers = [int(i) for i in file]

# Создадим счётчик и переменную для максимальной суммы
count = 0
max_sum = 0

# Перебираем пары соседних элементов
for i in range(len(numbers) - 1):
    # Проверяем, что хотя бы одно число из пары оканчивается на 2 в 5 сс
    if (numbers[i] % 5 == 2) or (numbers[i + 1] % 5 == 2):
        # Увеличиваем счётчик, если условие прошло
        count += 1
        # Обновляем максимальное число
        if numbers[i] + numbers[i + 1] > max_sum:
            max_sum = numbers[i] + numbers[i + 1]

# Выводим ответ
print(count, max_sum)  # 126 171120
