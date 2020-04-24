import random
import string

container = []
status = True


while status:

    first_name = input("Enter your first name ")
    last_name = input("Enter your last name ")
    mail = input("enter your email address ")
    #num = random.randint(10000, 99999)
    letters = string.ascii_letters
    random_string = ''.join(random.choice(letters) for i in range(5))

    password = first_name[0:2].upper() + last_name[-2:].upper() + random_string
    passW = input("your password is " + password + ", do you like it? (input yes or no) ")
    user_details = {}
    if passW.upper() == "YES":
        user_details["FIRST NAME"] = first_name
        user_details["LAST NAME"] = last_name
        user_details["E-MAIL"] = mail
        user_details["PASSWORD"] = password
        container.append(user_details)


    else:
        password = input("Enter your choice  password ")

        while len(password) < 7:
            password = input("Please a password with 7 or more characters ")
        else:
            user_details["FIRST NAME"] = first_name
            user_details["LAST NAME"] = last_name
            user_details["E-MAIL"] = mail
            user_details["PASSWORD"] = password
            container.append(user_details)

    newUser = input("Would you like to enter a new user? enter yes or no ")
    if newUser.upper() == "NO":
        status = False

        for items in container:
            print(items)
    else:
        status = True






















