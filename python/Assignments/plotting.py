import matplotlib.pyplot as plt
from math import *
import numpy


total = int(input("Number of Projectile Motions: "))

for i in range (total):
    speed = int(input("Velocity: "))
    angle = int(input("Angle: "))

    g = 9.8

    y_speed = int(sin(radians(angle))*speed)
    x_speed = int(cos(radians(angle))*speed)
    time = int((0+y_speed/g)*2)

    x_plot = []
    y_plot = []

    for t in numpy.arange(0,time +1 ,0.01):
        height = (y_speed*t)-(g*(t**2)*0.5)
        if height >= 0:
            x_plot.append(x_speed*t)
            y_plot.append(height)

    plt.plot(x_plot, y_plot)

plt.title("Projectile Motions")
plt.xlabel("Distance")
plt.ylabel("Height")

plt.show()
