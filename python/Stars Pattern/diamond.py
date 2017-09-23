x=1
y=10

for i in range (1, y):
    if (i<6):
        print(" "*(y-i), "*"*(i*2-1))
    else:
        print(" "*(i), "*"*((y-i)*2-1))
