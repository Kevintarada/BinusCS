num=[0,1]
x=int(input("Fibonacci= "))
for i in range(1,x+1):
    x=num.pop()
    y=num.pop()
    print(y)
    z=x+y
    num.append(x)
    num.append(z)

