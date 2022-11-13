# 22112202 정보통신공학과 이유준
# HomeWork2_5

import turtle
t = turtle.Turtle()
t.shape('turtle')
t.color("black")

n, length, x, y = map(int,input("꼭지점의 개수, 한 변의 길이, x축, y축을 입력하세요: ").split())
t.setpos(x, y)
t.write(x, y)

t.up(); t.goto(-length / 2, -length / 2); t.down()
for i in range(n):
    t.forward(length); t.left(360 / n); t.write(t.pos())
t.up(); t.goto(x, y); t.down()