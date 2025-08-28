from turtle import *

# Ускорение отрисовки
tracer(0)
# Поворот влево, чтобы Черепаха смотрел вдоль оси ординат
left(90)

# Масштаб
scale = 20

# Повтори 2
for _ in range(2):
    # Вперёд 8
    forward(8 * scale)
    # Направо 90
    right(90)
    # Вперёд 18
    forward(18 * scale)
    # Направо 90
    right(90)

# Поднять хвост
up()

# Вперёд 4
forward(4 * scale)
# Направо 90
right(90)
# Вперёд 10
forward(10 * scale)
# Налево 90
left(90)

# Опустить хвост
down()

# Повтори 2
for _ in range(2):
    # Вперёд 17
    forward(17 * scale)
    # Направо 90
    right(90)
    # Вперёд 7
    forward(7 * scale)
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
