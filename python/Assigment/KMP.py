def convert (full_name):
    printing_list=[]
    container_list= list(full_name.upper())
    printing_list.append(container_list[0])
    for i in range (0, len(container_list)):
        if (container_list[i]=="-"):
            printing_list.append(container_list[i+1])
        else:
            continue
    print(''.join(printing_list))
def main():
    while True:
        full_name=input("Input full name: ")
        convert(full_name)
main()

# make input to list
# make all into capital letters
# append first letter to a new list
# use loop to get the letter after "-" and append it
# join the appended letters then print it
