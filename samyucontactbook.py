def main(): 
    contactlist = open("contactinfo.txt", "w+")
    choice(contactlist)
    while True:
        decision = str(input("Do you want to do anything else? Yes or No"))
        if decision == "Yes": 
            choice(contactlist)
        else:
            contactlist.close()
            break

   
def choice(contactlist):
    decision = str(input("Do you want to add, delete, or search contact info? "))
    if decision == "add":
        addContact(contactlist)
    elif decision == "delete":
        deleteContact(contactlist)
    elif decision == "search":
        searchContact()
    else:
        print("Invalid answer")
    
def addContact(contactlist):
    add = str(input("What is the name of your contact? "))
    #addnumber = str(input("What is the phone number of your contact? "))
    contactlist.writelines([add + "\n"])
    #contactlist.writelines([addnumber + "\n"])
    
    
    
def deleteContact(contactlist):
    delete = str(input("What contact do you want to delete? "))
    contactlist.seek(0)
    num_lines = contactlist.readline()
    found = False
    with open("contactinfo.txt", "w") as temp_file:
        for lines in num_lines:
            if num_lines != delete:
                temp_file.write(lines)
            else:
                found = True
        
    if found == True: 
        print("Deleted contact")
    else:
        print("Contact not found")
            
                        
def searchContact():
    search = str(input("What contact do you want to search for"))
    
        
if __name__ == "__main__":
    main()