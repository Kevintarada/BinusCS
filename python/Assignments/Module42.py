def input_numbers():
    number_inputed=[]
    for i in range (0,10):
        input_number=int(input("Input number: "))
        number_inputed.append(input_number)
    return number_inputed
def module(input_numbers):
    module_result=[]
    list_count=[]
    for x in range (0,len(input_numbers)):
        module_result.append(input_numbers[x]%42)
    list_count.append(module_result[0])
    for z in range (1, len(module_result)):
        if (module_result[z]==module_result[z-1]):
            continue
        else:
            list_count.append(module_result[z])
    print(len(list_count))
def main():
    module(input_numbers())
main()
# this one is quite tricky....
