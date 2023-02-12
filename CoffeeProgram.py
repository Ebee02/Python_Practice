def user_name_or_not():
    name_choice = input("Hello value customer before you proceed, do you want to enter your name?\nWe take pride in knowing each and everyone of our value customer names, but you're not obligate to give it\nSimply clicked Y for Yes or N for No: ")
    nm_choice = name_choice.lower()
    if nm_choice == "y" or nm_choice == "yes":
        print("Wonderful!!!")
        user_name = input("Now all you have to do is enter your name to proceed: ")
    else:
        user_name = ""
    print("")
    return user_name

def coffee_menu(small_cup, medium_cup, large_cup, tbill):
    while True:
        coffee_choice = int(input(f"Select your coffee choice from the menu below\n1. Small cup of coffee ------------- ${small_cup}\n2. Medium cup of coffee ------------- ${medium_cup}\n3. large cup of coffee ------------- ${large_cup}\n4. Exit the coffee menu....................\nSelect your order: "))
        if coffee_choice == 1:
                tbill += small_cup
                print(f"your currently bill is: ${tbill}, because you order the small-size cup")
        elif coffee_choice == 2:
                tbill += medium_cup
                print(f"your currently bill is: ${tbill}, because you order the medium-size cup")
        elif coffee_choice == 3:
            tbill += large_cup
            print(f"your currently bill is: ${tbill}, because you order the large-size cup")
        elif coffee_choice == 4:
            print("Menu closed.........")
        else:
            print("Invalid input, your coffee choice doesn't exist, you need to try again")
        print("")
        user_choice = input("Do you still want to order coffee? \n")
        user_c = user_choice.lower()
        if user_c ==  "no" or user_c == "n" or user_c == "nope":
            break
    print("")
    final_order(tbill, name)
    
def final_order(tbill, name):
    if name == "":
        print(f"Your order have been inputed.........\nIt will reach you within 30 minutes\nYour total bill is: {tbill}\nThank you value customer, hope you dine with us soon................")
    else:
        print(f"Your order have been inputed.........\nIt will reach you within 30 minutes\nYour total bill is: {tbill}\nThank you {name}, hope you dine with us soon................")

small_cup = 2.
medium_cup =  3.7
large_cup =  5.5
tbill= 0.

name = user_name_or_not()
if name == "":
    print("Welcome valid customer to our online coffee shop.......")
else:
    print(f"Welcome {name} to our online coffee shop")

coffee_menu(small_cup, medium_cup, large_cup, tbill)
print("")
