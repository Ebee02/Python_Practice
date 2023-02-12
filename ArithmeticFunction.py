def allOperation(n1, n2):
    sum = n1 + n2
    difference = n1 - n2
    reminder = n1 / n2
    prod= n1 * n2
    #Print the value of all the variables
    print(f"The sum of {n1} and {n2} is: {sum}")
    print(f"The difference of {n1} and {n2} is: {difference}")
    print(f"The reminder of {n1} and {n2} is: {reminder}")
    print(f"The prod of {n1} and {n2} is: {prod}")



def arithmeticOperation(n1, n2, choice):
    if choice == 1:
        answer = n1 + n2
        print(f"The sum of {n1} and {n2} is: {answer}")

    elif choice == 2:
        answer = n1 - n2
        print(f"The difference of {n1} and {n2} is: {answer}")

    elif choice == 3:
        answer = n1 / n2
        print(f"The quotient of {n1} and {n2} is: {answer}")
    
    elif choice == 4:
        answer = n1 * n2
        print(f"The product of {n1} and {n2} is: {answer}")
    
    elif choice == 5:
        allOperation(n1, n2)
    elif choice == 6:
        print("Program Canceled....")

        

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("")
userChoice = int(input("Press 1 to add\nPress 2 to subtract\nPress 3 to divide\nPress 4 to mutiply\nPress 5 to show use all \nPress 6 to cancel\n"))
arithmeticOperation(num1, num2, userChoice)


