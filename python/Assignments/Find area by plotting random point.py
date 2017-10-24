import matplotlib.pyplot as plt
import random


x_rand = []
y_rand = []
y_total = []

for i in range(4000) :
    x_rand.append(random.randint(0, 25))
    y_rand.append(random.randint(0, 600))

plt.plot(x_rand, y_rand, "o", color = "blue")

x = []
y = []

for i in range(0,26) :
    x.append(i)
    y.append(i ** 2 - 3 * i + 4)

plt.plot(x, y, "o", color = "red")


for q in range(len(x_rand)) :
    num = x.index(x_rand[q])

    if y_rand[q] < y[num]:
        y_total.append(y_rand[q])
    else:
        continue

print(len(y_total)/4000*25*600)

plt.axis([0, 25, 0, 600])
plt.show()
