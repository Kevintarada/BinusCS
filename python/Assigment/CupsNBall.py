def calculate(switching_pattern):
    cups=[1,0,0]
    # 1 is the ball
    for i in range (0, len(switching_pattern)):
        list_for_switch=[]
        if (switching_pattern[i]=="A"):
            list_for_switch.append(cups[0])
            cups[0]=cups[1]
            cups[1]=list_for_switch[0]
        elif (switching_pattern[i]=="B"):
            list_for_switch.append(cups[1])
            cups[1]=cups[2]
            cups[2]=list_for_switch[0]
        elif (switching_pattern[i]=="C"):
            list_for_switch.append(cups[0])
            cups[0]=cups[2]
            cups[2]=list_for_switch[0]
        else:
            print("(Patterns only consist of \"A\", \"B\", and \"C\")")
            main()
    print("(1=left | 2=middle | 3=right)")
    print("Cup number:", cups.index(1)+1)
def main():
    while True:
        switching_pattern=list(input("Pattern: ").upper())
        calculate(switching_pattern)
main()
