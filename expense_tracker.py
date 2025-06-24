# Displaying the menu.
while True:
    print("")
    print("Hello User, please select a choice from the menu")
    print("")

    print("1). Add an expense")
    print("2). View expenses")
    print("3). view the toatal expenses")
    print("4). Exit")
    print("")
    print("")

    try:
        choice = int(input("Please enter Your choice : "))             # checking for valid input 
    except:
        print("Incorrect choice!!! Please enter an integer")
        print("")
        print("")
        continue


    if choice == 1:
        
        try : 
            print("")
            amount = float(input("Please enter the amount : "))
        except :
            print("Please enter an integer or a float number \n \n")
            continue
        
        category = input("Please enter the category : ")
        note = input("Please enter a note(optional) : ")
        print()
        print()

        with open("Expenses.txt","a") as f:
            f.write(f"{amount},{category},{note}\n")
        print("Expenses Added successfully!!! \n\n")


    elif choice == 2:
        try:
            with open("Expenses.txt","r") as f:                       # Checking if the file exist 
                lines = f.readlines()
        except FileNotFoundError:
            print("The file does not exist yet!!! \n\n")


        for line in lines:
            parts=line.strip().split(",")
            amount = parts[0].strip()
            category = parts[1].strip()
            note = parts[2].strip()
            print(f"Amount : {amount} | Category : {category} | Note : {note} \n \n ")

    elif choice == 3:
        total = 0.0                                              # Storing the total 

        try:
            with open("Expenses.txt","r") as f:                  # Checking if the file exist 
                lines = f.readlines()
        except FileNotFoundError:
            print("The file does not exist yet!!! \n\n")
            continue

        for line in lines:
            parts=line.strip().split(",")
            amount = parts[0].strip()
            total += float(amount)
        print("The total amount spent is : ",total,"\n\n")
    
    elif choice == 4:
        print ("Thank You !!!")
        break
    else: 
        print("Invalid choice !!!")
        continue
