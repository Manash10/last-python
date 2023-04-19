phoneDirectory = {}

while True:
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n"
          "1. Add a record\n"
          "2. Search a record\n"
          "3. Change a record\n"
          "4. Delete a record\n"
          "5. Quit\n")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = phone
        print("Record added\n")
    
    elif choice == '2':
        name = input("Enter name to search: ")
        if name in phoneDirectory:
            print(f"{name}: {phoneDirectory[nam
                  
                  e]}\n")
        else:
            print("Record not found\n")
    
    elif choice == '3':
        name = input("Enter name: ")
        if name in phoneDirectory:
            phone = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = phone
            print("Record updated\n")
        else:
            print("Record not found\n")
    
    elif choice == '4':
        name = input("Enter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("Record deleted\n")
        else:
            print("Record not found\n")
    
    elif choice == '5':
        break
    
    else:
        print("Invalid choice\n")

