math_txt=open('C:\Binus CS\math_expression.txt', 'r')
infix=(math_txt.read()).split()
print(infix)
postfix=[]
operator=[]

def precedence(x):
    if x=="+" or x=="-" :
        return 1
    elif x=="*" or x=="/":
        return 2
    elif x=="(":
        return 0

def type(i):
    if i=="+" or i=="-" or i=="*" or i=="/":
        return "operator"
    elif i=="(" or i==")":
        return "parenthesis"
    elif i==" ":
        return "empty"
    else:
        return "operand"
def main():
    for i in range(0, len(infix)):
        type_of_thing=type(infix[i])
        if type_of_thing=="operand":
            postfix.append(infix[i])
        elif type_of_thing=="operator":
            while len(operator)!=0 and precedence(infix[i]) <= precedence(operator[-1]) :
                postfix.append(operator.pop())
            operator.append(infix[i])
        elif type_of_thing=="parenthesis":
            if infix[i]=="(":
                operator.append(infix[i])
            elif infix[i]==")":
                while operator[-1]!="(":
                    the_pop=operator.pop()
                    postfix.append(the_pop)
                operator.pop()
        while i==len(infix)-1 and len(operator)!=0:
            the_pop=operator.pop()
            postfix.append(the_pop)
    print(postfix)
    print(''.join(postfix))
    print(operator)
main()
