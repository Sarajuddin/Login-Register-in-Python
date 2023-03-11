from sys import exit
from re import fullmatch
import database

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

class Registration:

    def display(self):
        print("\n\tPress 1 : Register")
        print("\tPress 2 : Login")
        print("\tPress 3 : Exit")
        c = input("\n\tWhat do you want to do : ")
        return c
    
    def validateLoginData(self, my_dict = {}):
        for key in my_dict:
            if key == 'email':
                if not (fullmatch(regex, my_dict[key])):
                    return "Email ID is not valid"
        return "OK"

    def validateRegData(self, my_dict = {}):
        for key in my_dict:
            if key == 'age':
                if my_dict[key] < 0 or my_dict[key] > 150:
                    return "Please enter valid age"
            if key == 'mobile':
                if not (len(my_dict[key])==10 and my_dict[key].startswith('6') or my_dict[key].startswith('7') or my_dict[key].startswith('8') or my_dict[key].startswith('9')):
                    return "Please enter correct mobile number"
            if key == 'email':
                if not (fullmatch(regex, my_dict[key])):
                    return "Email ID is not valid"
            if key == 'password' or key == 'c_password':
                if my_dict['password'] != my_dict['c_password']:
                    return "Password and Confirm Password are not same."
        return "OK"

    def register(self):
        name = input("\n\tEnter Name : ").title()
        age = int(input("\tEnter Age : "))
        mobile = input("\tEnter 10-Digit Mobile Number : ")
        email  = input("\tEnter Email ID : ")
        password = input("\tEnter Password : ")
        c_password = input("\tConfirm Password : ")

        my_dict = {'name':name, 'age':age, 'mobile':mobile, 'email':email, 'password':password, 'c_password':c_password}
        print(my_dict)
        data_list = tuple(my_dict.values())
        print(data_list)

        # 1. Firsly Validate Data ...
        responce = self.validateRegData(my_dict)
        print(responce)
        if responce == "OK":
            # Check if Record already exists or not
            data = database.getData(email, password)
        
            if data:
                print("\n\t-------------------------")
                print("\t| Record Already Exists |")
                print("\t-------------------------\n")
            else:
                database.createTable()
                database.writeData(data_list)

                print("\n\t-------------------------------")
                print("\t| Data Stored Successfully 🐤 |")
                print("\t-------------------------------\n")
        else:
            print("\n\t-------------------------------")
            print(f"\t| {responce} |")
            print("\t-------------------------------\n")

    def login(self):
        email  = input("\tEnter Email ID : ")
        password = input("\tEnter Password : ")

        my_dict = {'email':email, 'password':password}
        # data_list = list(my_dict.values())

        # 1. Firsly Validate Data ...
        responce = self.validateLoginData(my_dict)

        if responce == "OK":
            # Check if Record already exists or not
            data = database.getData(email, password)
        
            if data:
                print("\n\t-------------------------")
                print("\t| Record Already Exists |")
                print("\t-------------------------\n")
                print(f"\n\t{data}\n")
            else:
                print("\n\t-------------------------------")
                print("\t| Record doesn't Exists 🐤 |")
                print("\t-------------------------------\n")
        else:
            print("\n\t-------------------------------")
            print(f"\t| {responce} |")
            print("\t-------------------------------\n")



obj = Registration()
while True:
    char = obj.display()
    if char == '1':
        obj.register()
    elif char == '2':
        obj.login()
        pass
    elif char == '3':
        print("\n\t---------------------------------")
        print("\t| Thank You! Have a nice day 🐤 |")
        print("\t---------------------------------\n")
        exit()
    else:
        print("\n\t----------------------------")
        print("\t| Please Enter Valid Input |")
        print("\t----------------------------\n")
