import sys
import os
import random

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

numlist=[]
x=(input(""))
while (x!=""):
    if (x.isdigit()==True):
        numlist.append(int(x))
        x=(input(""))
    elif ((x=="+") or (x=="-") or (x=="*") or (x=="/")):
        count=len(numlist)
        if (count>=2):
            if (x=="+"):
                sNum = numlist.pop()
                fNum = numlist.pop()
                y=add(fNum, sNum)
                numlist.append(y)
                print(y)
                x=(input(""))
            elif (x=="-"):
                sNum = numlist.pop()
                fNum = numlist.pop()
                y=subt(fNum, sNum)
                numlist.append(y)
                print(y)
                x=(input(""))
            elif (x=="*"):
                sNum = numlist.pop()
                fNum = numlist.pop()
                y=mult (fNum, sNum)
                numlist.append(y)
                print(y)
                x=(input(""))
            elif (x=="/"):
                sNum = numlist.pop()
                fNum = numlist.pop()
                y=div(fNum, sNum)
                numlist.append(y)
                print(y)
        else:
            print("Input more number!")
            x=(input(""))
    else:
        print("Please input a number!")
        x=(input(""))
