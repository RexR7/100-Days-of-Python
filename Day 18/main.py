# import colorgram
# colors = colorgram.extract("aryan.jpg", 225)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
color_list = [(133, 164, 202), (225, 150, 101), (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72), (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157), (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158), (18, 83, 105), (175, 200, 188), (35, 150, 209), (65, 66, 56), (103, 140, 129), (164, 200, 214), (130, 129, 122)]

slow_turtle = Turtle()
slow_turtle.speed("fastest")
slow_turtle.hideturtle()
slow_turtle.teleport(-250, -200)

def move_straight():
    for _ in range(10):
        choice = random.choice(color_list)
        slow_turtle.dot(20, choice)
        slow_turtle.penup()
        slow_turtle.forward(50)
def move_up_1():
    choice = random.choice(color_list)
    slow_turtle.dot(20, choice)
    slow_turtle.left(90)
    slow_turtle.penup()
    slow_turtle.forward(50)
    slow_turtle.left(90)
def move_up_2():
    choice = random.choice(color_list)
    slow_turtle.dot(20, choice)
    slow_turtle.right(90)
    slow_turtle.penup()
    slow_turtle.forward(50)
    slow_turtle.right(90)

for _ in range(5):
    move_straight()
    move_up_1()
    move_straight()
    move_up_2()















screen = Screen()
screen.exitonclick()
