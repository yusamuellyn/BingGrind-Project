def main(): 
    choice()
    while True:
        decision = str(input("Do you want to do anything else? Yes or No"))
        if decision == "Yes": 
            choice()
        elif decision == "No":
            break
        else:
            "Invalid Answer"

   
def choice():
    decision = str(input("Do you want to add, delete, or search contact info? "))
    if decision == "add":
        addContact()
    elif decision == "delete":
        deleteContact()
    elif decision == "search":
        searchContact()
    else:
        print("Invalid answer")
    
def addContact():
    add = str(input("What is the name of your contact? "))
    addnumber = str(input("What is the phone number of your contact? "))
    with open("contactinfo.txt", "a") as file:
        file.write(add + " " + addnumber +  "\n")
    
def deleteContact():
    delete = str(input("What contact do you want to delete? "))
    deleteNum = str(input("What is the phone number of the contact? "))
    with open("contactinfo.txt", "r") as file:
            lines = file.readlines()
   
    with open("contactinfo.txt", "w") as file:
            for line in lines:
                if line.__contains__(delete) == False:
                    file.write(line)
                else:
                    print(delete + " has been deleted")
                    
    with open('contactinfo.txt', 'r') as file:
        for line in file:
            print(line.strip())
    
                        
def searchContact():
    search = str(input("What contact do you want to search for? "))
    names = []
    with open("contactinfo.txt", "r") as file:
        num = 0
        for line in file:
            if line.__contains__(search):
                num = num + 1
                print(line.strip())
    if num == 0:
        print("Contact not found")
                  
if __name__ == "__main__":
    main()