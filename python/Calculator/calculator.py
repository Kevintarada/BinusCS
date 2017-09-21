import sys
import os
import random

def add (fNum, lNum):
    addNum = fNum + lNum
    return addNum
def sub (fNum, lNum):
    subNum = fNum - lNum
    return subNum
def mult (fNum, lNum):
    multNum = fNum * lNum
    return multNum
def div (fNum, lNum):
    divNum = fNum / lNum
    return divNum

numlist=[]
x=input("")
while (x!=""):
    if (x=="+"):
        lNum = numlist.pop()
        fNum = numlist.pop()
        y=add(fNum, lNum)
        numlist.append(int(y))
        print(y)
        x=input("")
    elif (x=="-"):
        lNum = numlist.pop()
        fNum = numlist.pop()
        y=sub(fNum, lNum)
        numlist.append(int(y))
        print(y)
        x=input("")
    elif (x=="*"):
        lNum = numlist.pop()
        fNum = numlist.pop()
        y= mult(fNum, lNum)
        numlist.append(int(y))
        print(y)
        x=input("")
    elif (x=="/"):
        lNum = numlist.pop()
        fNum = numlist.pop()
        y= div (fNum, lNum)
        numlist.append(int(y))
        print(y)
        x=input("")
    else:
        numlist.append(int(x))
        x=input("")
