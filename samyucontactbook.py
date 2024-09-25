def main(): 
    contactlist = open("contactinfo.txt", "w+")
    choice(contactlist)
    contactlist.close()

   
def choice(contactlist):
    decision = str(input("Do you want to add, delete, or search contact info? "))
    if decision == "add":
        addContact(contactlist)
    elif decision.equals("delete"):
        deleteContact(contactlist)
   # elif decision.equals("search"):
       # search()
    
def addContact(contactlist):
    add = str(input("What is the name of your contact? "))
    addnumber = str(input("What is the phone number of your contact"))
    contactlist.writelines([add + " "])
    contactlist.writelines([addnumber + "\n"])
    
    
    
def deleteContact(contactlist):
    delete = str(input("What contact do you want to delete"))
    
  
#def search():
    
        
if __name__ == "__main__":
    main()