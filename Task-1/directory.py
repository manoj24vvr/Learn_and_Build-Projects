''' creating a dictionary named directory'''
directory = {}
var = 0
def NewContact (Name,Phone_number):
    directory[Name] = []
    directory[Name].append(Phone_number)

def AddNewContact (Name,Phone_number):
    directory[Name].append(Phone_number)
def UpdateExistingContact (Name,New_Number):
    for key in directory:
        if(key == Name):
            directory[Name] = []
            directory[Name].append(New_Number)
            print("Updated Contact Successfully") 

def DeleteExistingContact (Name):
    var = 0
    for key in directory:
        if(key == Name):
            var = 1
            del directory[Name]
            break
    if var == 0 :
        print('Contact not Found');
    else :
        print('Contact Deleted Successfully');
    
def SearchExistingContact (Name):
    var = 0
    for key in directory:
        if(key == Name):
            print("Name of Person: " + key)
            print("Available Phone Numbers: ")
            print(directory[key])
            var = 1
    if var != 1 :
        print('Contact not Found')
   
def switcher(no):
    if(no==1):
        Name=input("Enter Name : ")
        Pno=int(input("Enter Phone Number : "))
        NewContact(Name,Pno)
        print("Contact Added Succesfully")
    elif(no==2):
        Name=input("Enter Name : ")
        Pno=int(input("Enter Phone Number : "))
        AddNewContact(Name,Pno)
        print("Another Phone Number Added Successfully") 
    elif(no==3):
        Name=input("Enter Name : ")
        Pno=int(input("Enter Phone Number : "))
        UpdateExistingContact(Name,Pno)
        
    elif(no==4):
        Name=input("Enter Name : ")
        DeleteExistingContact(Name) 
    elif(no==5):
        Name=input("Enter Name : ")
        SearchExistingContact(Name) 
    elif(no==6):
       print(directory)   
    else:
        print("Invalid Input...!!!")

print("\t Welcome to Directory. \n")
print("Select one of the below options. (Select '0' to exit.)")
print("1. Create Contact ")
print("2. Add new Contact")
print("3. Update Contact")
print("4. Delete Contact")
print("5. Search for a given name and show their contact details")
print("6. Show all contacts.")

while(True):

    num=int (input('\nEnter a option: '))
    if num == 0:
        exit
    else:
        switcher(num)

