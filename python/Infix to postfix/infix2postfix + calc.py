math_txt=open('math_expression.txt', 'r')
# just change the file / you may change the text in math_expression.txt instead
# i use split so ' ' is needed after every character except the last....
infix=(math_txt.read()).split()
postfix=[]
operator=[]
def add (fNum, sNum):
    addNum = fNum + sNum
    return addNum
def subt (fNum, sNum):
    subNum = fNum - sNum
    return subNum
def mult (fNum, sNum):
    multNum = fNum * sNum
    return multNum
def div (fNum, sNum):
    divNum = fNum / sNum
    return divNum

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

def calculate(postfix):
    numlist=[]
    for i in range (0, len(postfix)):
        try :
            x=int(postfix[i])
            numlist.append(x)
        except:
            if ((postfix[i]=="+") or (postfix[i]=="-") or (postfix[i]=="*") or (postfix[i]=="/")):
                count=len(numlist)
                if (count>=2):
                    if (postfix[i]=="+"):
                        sNum = numlist.pop()
                        fNum = numlist.pop()
                        y=add(fNum, sNum)
                        numlist.append(y)
                    elif (postfix[i]=="-"):
                        sNum = numlist.pop()
                        fNum = numlist.pop()
                        y=subt(fNum, sNum)
                        numlist.append(y)
                    elif (postfix[i]=="*"):
                        sNum = numlist.pop()
                        fNum = numlist.pop()
                        y=mult (fNum, sNum)
                        numlist.append(y)
                    elif (postfix[i]=="/"):
                        sNum = numlist.pop()
                        fNum = numlist.pop()
                        y=div(fNum, sNum)
                        numlist.append(y)
    return float(numlist[0])

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
    print("Infix: ", end="")
    print(' '.join(infix))
    print("Postfix: ",end="")
    print(' '.join(postfix))
    print("Result: ", end="")
    print(calculate(postfix))
main()
