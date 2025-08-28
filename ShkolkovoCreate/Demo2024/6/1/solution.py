from turtle import *

# Ускорение отрисовки
tracer(0)
# Поворот влево, чтобы Черепаха смотрел вдоль оси ординат
left(90)

# Масштаб
scale = 40

# Повтори 7
for _ in range(7):
    # Вперёд 10
    forward(10 * scale)
    # Направо 10
    right(120)


# Поднимаем хвост, чтобы нарисовать точки
up()
# Рисуем точки с координатами от -20 до 20
for x in range(-20, 20):
    for y in range(-20, 20):
        # Перемещаем Черепаху в точку (x, y)
        goto(x * scale, y * scale)
        # Зелёная точка
        dot(5, "green")


# Отрисовать рисунок
update()
# Конец программы, чтобы рисунок сразу не закрылся
getscreen().getcanvas().postscript(file="figure.eps")
done()
