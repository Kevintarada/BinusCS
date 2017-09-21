row_number = int(input("Rows: "))
display_list=[]
for y in range (1,row_number+1):
    display_list.append(1)
    print(display_list)
    z=display_list[0]
    list_for_add=[]
    list_for_add.append(z)
    length_of_list= len(display_list)
    for x in range (0,length_of_list - 1):
        list_for_add.append(display_list[x]+display_list[x+1])
    display_list=list_for_add
