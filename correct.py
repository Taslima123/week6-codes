print("Welcome to the Prudent Healthcare Hospital")
print("Lets start with users login process:-")


file="dic.txt"

def writes(patient_id, first_name, last_name, address, gender, contact):
    fw = open('dic.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact))
    fw.close()

textfile="data.txt"

def cost(extract,name,through,recebill):
        fw = open('data.txt', "a")
        fw.write("%1s%20s%20s%20s\n" % (extract,name,through,recebill))
        fw.close()


def credit(extract,name,through,amount,crebill):
    fw = open('data.txt', "a")
    fw.write("%1s%20s%20s%20s%20s\n" % (extract,name,through,amount,crebill))
    fw.close()


print("Are you \n1.Physian\n2.Accountant")


def login():
    email=input("Enter your username:")
    passw=input("Enter your password:")
    print("username and password matched")
    print("login successful")


def read():
    users = open("dic.txt",'r')
    extract = input("Please input patient ID")
    for each_line in users:
        (patient_id, first_name, last_name, address, gender, contact) = each_line.split()

        if (patient_id == extract):
            print(patient_id, first_name, last_name, address, gender, contact)
    users.close()



def registration():
    first_name = input("Enter your first_name:")
    last_name = input("Enter your last name:")
    patient_id = input("Enter patient_id:")
    address = input("Enter your address:")
    gender = input("Enter your gender: ")
    contact = input("Enter your contact number:")
    writes(patient_id, first_name, last_name, address, gender, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")
    print("information saved in text file")

def appointment():
    print("Book an appointment")
    print("List of specialists")
    print("1. Dr.Kelvin")
    print("2. Dr.Nitesh")
    print("3. Dr.Richard")
    print("4. Dr.Scott")

    # This is for Doctor A
    select_doctor = input("Choose your doctor\n")

    if select_doctor == "1":

        print("Dr.Kelvin \n a. 08:00AM-09:00AM \n b.12:00AM-01:00PM \n c. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 08:00AM-09:00AM")
        elif your_time == "b":
            print("b. 12:00AM-01:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")

        else:
            print("Not available")

            # This is for Doctor B

    elif select_doctor == "2":

        print("Dr.Nitesh \n a. 09:30AM-10:30AM\n b. 01:30PM-02:30PM \n c. 03:30PM-04:30PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 09:30AM-10:30AM")
        elif your_time == "b":
            print("b. 01:30PM-02:30PM")
        elif your_time == "c":
            print("c. 03:30PM-04:30PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done. Go for payment")
        else:
            print("waiting list")

            # This is for Doctor C

    elif select_doctor == "3":

        print("Dr. Richard\n a. 11:00AM-12:00AM \n b. 01:00PM-02:00PM \nc. 03:00PM-04:00PM")

        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 11:00AM-12:00AM")
        elif your_time == "b":
            print("b. 01:00PM-02:00PM")
        elif your_time == "c":
            print("c. 03:00PM-04:00PM")
        else:
            print("Not available")
        notification = input("notification goes to doctor for check up press y")
        if notification == "y":
            print("y. Check up done. Go for payment")
        else:
            print("waiting list")

            # This is for Doctor D

    elif select_doctor == "4":

        print("Dr. Scott \n a. 07:30AM-08:30AM \n b. 10:30AM-11:30AM \n c. 04:30PM-05:30PM")
        your_time = input("Favouralbe time")
        if your_time == "a":
            print("a. 07:30AM-08:30AM")
        elif your_time == "b":
            print("b. 10:30AM-11:30AM")
        elif your_time == "c":
            print("c. 04:30PM-05:30PM")
        else:
            print("Not available")

def payment():
    print("For cash Enter C")
    print("For credit Enter L")
    payment = input("finish the payment")
    if payment == "C":
        print("payment done by cash")
        extract = input("Please input patient ID")
        name=input("Enter your name")
        through=input("write through cash")
        recebill = input("Please enter the receipt for the bill in Rs.:-")

        print(recebill)
        cost(extract,name,through,recebill)
        print("Thank you")

    elif payment == "L":
        print("payment done by credit")
        extract = input("Please input patient ID")
        name = input("Enter your name")
        through = input("write through credit card")
        crebill = input("Please enter the credit card number")
        amount=input("please enter total amount in Rs.")
        print(crebill)
        credit(extract,name,through,amount,crebill)
        print("Thank you")
    else:
        print("not paid and go for payment")
        print("Thank You")

def logout():
    print("logout")


choose= input("Enter Choice?")
number= int(choose)
if (number==1):
    login()
    while True:
        users=input("is the patient is\n1.new patient\n2.old patient\n3.exit")
        number=int(users)
        if (number==1):
            registration()
        elif(number==2):
            users = input("press enter for patient information")
            read()

        elif(number==3):
            logout()
            break
        else:
            print("wrong choice")

        users=input("do you want to take an appointment?\n1.yes\n2.no")
        number=int(users)
        if(number==1):
            appointment()

        elif(number==2):
            print("continue main menu")

        else:
            print("wrong choice")

elif(number==2):
    login()
    users=input("press Enter for patient information")
    read()
    users=input("for payment press Enter")
    payment()
    logout()

else:
    print("Wrong Choice")

