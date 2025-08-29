from turtle import *

# Увеличиваем размер экрана, чтобы картинка влезла
screensize(2000, 2000)

# Ускорение отрисовки
tracer(0)
# Поворот влево, чтобы Черепаха смотрел вдоль оси ординат
left(90)

# Масштаб
scale = 30

# Повтори 9
for _ in range(9):
    # Впедёд 22
    forward(22 * scale)
    # Направо 90
    right(90)
    # Вперёд 6
    forward(6 * scale)
    # Направо 90
    right(90)

# Поднять хвост
up()
# Вперёд 1
forward(1 * scale)
# Направо 90
right(90)
# Вперёд 5
forward(5 * scale)
# Налево 90
left(90)
# Опустить хвост
down()

# Повтори 9
for _ in range(9):
    # Вперёд 53
    forward(53 * scale)
    # Направо 90
    right(90)
    # Вперёд 75
    forward(75 * scale)
    # Направо 90
    right(90)


# Поднимаем хвост, чтобы нарисовать точки
up()
# Рисуем точки с координатами от -30 до 30
for x in range(-30, 30):
    for y in range(-30, 30):
        # Перемещаем Черепаху в точку (x, y)
        goto(x * scale, y * scale)
        # Зелёная точка
        dot(5, "green")


# Отрисовать рисунок
update()

input()
getscreen().getcanvas().postscript(file="figure.eps")
print("saved")

# Конец программы, чтобы рисунок сразу не закрылся
done()
