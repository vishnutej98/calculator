import database

USER_CHOICE = """
Please enter the choice:

'a' addition
's' subtraction
'm' multiplication
'd' division
"""


def menu():
    user_input = input(USER_CHOICE)
    #  while user_input != 'q':
    if user_input == 'a':
        prompt_addition()
    elif user_input == 's':
        prompt_subtraction()
    elif user_input == 'm':
        prompt_multiplication()
    elif user_input == 'd':
        prompt_division()
    else:
        print("\nThanks for opening app..!, see you soon..")
        quit()
        #  user_input() = input(USER_CHOICE)


def prompt_addition():
    num1 = float(input("\nenter 1st number: "))
    num2 = float(input("enter 2nd number: "))

    database.addition(num1, num2)
    print(f'the value is: ', database.addition(num1, num2))


def prompt_subtraction():
    num1 = float(input("\nenter 1st number: "))
    num2 = float(input("enter 2nd number: "))

    database.subtraction(num1, num2)
    print(f'the value is : ', database.subtraction(num1, num2))


def prompt_multiplication():
    num1 = float(input("\nenter 1st number: "))
    num2 = float(input("enter 2nd number: "))

    database.multiplication(num1, num2)
    print(f'the value is: ', database.multiplication(num1, num2))


def prompt_division():
    num1 = float(input("\nenter 1st number: "))
    num2 = float(input("enter 2nd number: "))

    database.division(num1, num2)
    print(f'the value is: ', database.division(num1, num2))


def re_menu():
    if_user_retry = input("\nwant to do other calculation? (y/n) ")
    if if_user_retry != 'n':
        menu()
    elif if_user_retry == 'n':
        print("\nThanks for using app..")
        exit()
    else:
        input("\nThanks for using app.. ")

    re_menu()


menu()
re_menu()
