import csv
from colorama import Fore, Style
from prettytable import PrettyTable
import pyfiglet
import time
import os


class registration():
    e_name = ''
    age = ''
    date_of_birth = ''
    e_id = ''
    e_id_number = ''
    address = ''
    contact = ''
    email = ''

    def register_data(self):

        with open("registration.csv", 'a', newline='') as file:
            data = csv.writer(file)

            while True:
                self.e_name = input("name: ")
                self.age = input("age: ")
                self.date_of_birth = input("date of birth: ")
                self.e_id = input("employee id: ")

                flag = 0
                while flag == 0:
                    self.e_id_number = input("employee id number(AADHAR): ")
                    if len(self.e_id_number) != 12:
                        print('enter 12 digit id_number')
                        flag = 0
                    else:
                        flag = 1

                self.address = input("address: ")

                flag = 0
                while flag == 0:
                    self.contact = input("contact: ")
                    if len(self.contact) != 10:
                        print('enter 10 digit contact number')
                        flag = 0
                    else:
                        flag = 1
                self.email = input("email: ")

                record = [self.e_name, self.age,  self.date_of_birth,  self.e_id,
                          self.e_id_number,  self.address,  self.contact,  self.email]
                print(record)
                data.writerow(record)
                ch = input("want to enter more data? :- ")
                if ch == 'n' or ch == 'N':
                    break

        file.close()
        input("!!!!PRESS ENTER TO MAIN MENU!!!!")
        os.system('cls')
        main()

    def fetch_data(self):

        l1 = []
        d1 = int(input(
            "SELECT ANY ONE:-\n1> See all records\n2> See specific record\n"))

        with open('registration.csv', 'r') as f:
            record = csv.reader(f, delimiter=',', dialect='excel')

            if d1 == 1:
                for dta in record:
                    l1.append(dta)

                print(Fore.BLUE)
                newTable = PrettyTable(
                    ['e_name', 'age', 'date_of_birth', 'e_id', 'e_id_number', 'address', 'contact', 'email'])
                newTable.add_rows(l1)
                print(newTable)
                print(Style.RESET_ALL)
            else:
                data1 = input("enter the employee id to see the record: ")
                for dta in record:
                    if data1 in dta:
                        l1 = dta
                        print(l1)
                        print(Fore.LIGHTBLUE_EX+'employee_name:      |', l1[0])
                        print('age:                |', l1[1])
                        print('date of birth:      |', l1[2])
                        print('employee id:        |', l1[3])
                        print('employee id number: |', l1[4])
                        print('address:            |', l1[5])
                        print('contact:            |', l1[6])
                        print('email:              |', l1[7])
                        print(Style.RESET_ALL)

                if data1 not in l1:
                    print("record not found!!!!!")

        f.close()
        input("!!!!PRESS ENTER TO MAIN MENU!!!!")
        os.system('cls')
        main()

    def update_data(self):

        newrecord = []
        l1 = []

        with open('registration.csv', 'r+', newline='') as f:

            data = csv.reader(f, delimiter=',', dialect='excel')

            fields = ['e_name', 'age', 'date_of_birth', 'e_id',
                      'e_id_number', 'address', 'contact', 'email']

            search_name = input(
                "enter the name of the employee whose record to be updated: ")

            print("1- name\n2- age\n3- date of birth\n4- employee id\n5- employee id number\n6- address\n7- contact\n8- email\n")

            selectfield = int(
                input("enter the number of field that u want to update: "))

            for dta in data:
                l1.append(dta)
            p = len(l1)

            for i in range(p-1):
                if l1[i][0] == search_name:

                    if selectfield == 1:
                        l1[i][0] = input("enter the new data: ")

                    if selectfield == 2:
                        l1[i][1] = input("enter the new data: ")

                    if selectfield == 3:
                        l1[i][2] = input("enter the new data: ")

                    if selectfield == 4:
                        l1[i][3] = input("enter the new data: ")

                    if selectfield == 5:
                        l1[i][4] = input("enter the new data: ")

                    if selectfield == 6:
                        l1[i][5] = input("enter the new data: ")

                    if selectfield == 7:
                        l1[i][6] = input("enter the new data: ")

                    if selectfield == 8:
                        l1[i][7] = input("enter the new data: ")

            f.seek(0, 0)
            dta1 = csv.writer(f, delimiter=',', dialect='excel')
            dta1.writerows(newrecord)
        f.close()
        input("!!!!PRESS ENTER TO MAIN MENU!!!!")
        os.system('cls')
        main()


def main():
   

    print(Fore.LIGHTGREEN_EX +
          (pyfiglet.figlet_format(text="HR MANAGEMENT SYSTEM", font="digital")))
    print(Fore.YELLOW+"1> NEW REGISTRATION OF EMPLOYEE\n2> SEE DETAIL OF EMPLOYEE\n3> UPDATE THE PRE-EXISTING EMPLOYEE RECORD\n4> EXIT")
    print(Style.RESET_ALL)
    c = int(input("Enter ur choice: "))

    if c == 1:
        r1.register_data()
    elif c == 2:
        r1.fetch_data()
    elif c == 3:
        r1.update_data()
    elif c == 4:
        print("thank u 😊😊")
        exit()

r1 = registration()
main()
