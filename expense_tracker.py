#Display the menu and store users choice


while True:
    print("1) Add Expense ")
    print("2) View All Expenses ")
    print("3) View Total Spent ")
    print("4) Exit ")
    choice = input("Enter Your choice :")

    if choice == "1" :

        # Taking inputs 
        try:                                                     #check if the input is write 
            amount = float(input("Enter the amount to add : ")) 
        except:
            print("Please enter a valid number !!") 
            continue
        category = input( "Enter the category :")
        note = input("Enter any note(optional) :")
        
        # Adding data to a file
        with open("Expenses.txt","a+") as file: 
            file.write(f"{amount},{category},{note}\n")

        print("Expenses Added Successfully")
        print()

    elif choice == "2":
        # Displays all expenses
        print("Displaying all expenses")
        try:
            with  open("Expenses.txt", "r")  as f:
                lines = f.readlines()
        except:
            print("The file does not exist yet")
            continue
        for line in lines:
            parts = line.strip().split(",") # strip helps to remove the extra /n 

            amount = parts[0].strip()
            category = parts[1].strip()
            note = parts[2] .strip()
            print(f"Amount: ${amount} | Category: {category} | Note: {note}") # Printing thr final data
            print()
        
        
    elif choice == "3" :
        total = 0.0 # stores the total amount spent

        # Reading data from file 
        try:
            with  open("Expenses.txt", "r")  as f:
                lines = f.readlines()
        except:
            print("The file does not exist yet")
            continue

        for line in lines:
            parts = line.strip().split(",")
            amount = parts[0].strip()
            total+= float(amount) # Calculating total
        

        print("Total amount spent =",total)
        print()

    elif choice == "4" :

        break

    else :
        print("Incorrect choice please enter the choice again :")