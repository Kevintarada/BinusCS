def winner(the_input):
    if (the_input%2==1):
        print("Winner: Alice")
    else:
        print("Winner: Bob")
def main():
    while True:
        number_of_stones=int(input("Number of stones: "))
        winner(number_of_stones)
main()
# this is the simple way..., may use for function and try function instead
