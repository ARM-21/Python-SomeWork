from fileRead import fileReader 
from fileWrite import * 

""" ask_user() method returns a string value based on user valid input i.e 1,2,3,4 otherwise print error message"""
# This function asks the user to choose an option and returns a string based on the user's input.

def ask_user():
    """Return String if user chooses a valid options  prints error message otherwise
    ((((  String----> \n 1.details \n 2.rent \n 3.return\n 4.exit  ))))"""

    # Display options for the user to choose from.
    # Print welcome message and options
    menu_options = {
        1: "Enter 1 to Show the details ",
        2: "Enter 2 to Rent the land",
        3: "Enter 3 to Return rented land",
        4: "Enter 4 to Exit the program"
    }

    # Print the menu header
    print("\t"+"[S.N.]\t                Menu")
    print("\t\t"+"-" * 50)  # it will print "-" 50 times

    # Print each menu option with its corresponding number
    for number, option in menu_options.items():
        
        print("\t"+f"  [{number }]\t       {   option}")
        print("\t\t"+"-"*50)


    # print("     1. Display Details     \n     2. Rent Land      \n     3. Return Land     \n     4. Exit     ")
    
    user_choice = 0  # Initialize user_choice variable
    
    # Keep asking for user input until a valid choice is made
    while user_choice not in [1, 2, 3, 4]:
        user_choice = "y"  # Initialize user_choice with a non-integer value
        print("\n")
        # Keep asking for user input until a valid numeric choice is entered
        while str(user_choice).strip().isalpha() or str(user_choice).isspace():

            try:
                user_choice = int(input("Enter your choice>>>> "))
            except:
                user_choice = input("Enter a valid choice>>>")

        # Return a string based on the user's choice
        if user_choice == 1 or user_choice == str(1):
            return "details"
        elif user_choice == 2 or user_choice == str(2):
            return "rent"
        elif user_choice == 3 or user_choice == str(3):
            return "return"
        elif user_choice == 4 or user_choice == str(4):
            return "exit"
        else:
            # Print an error message for invalid choices
            print("* Enter a valid choice *")
        







def display_The_Intro():
    """It displays the welcoming intro and details of land available with it's different details like kitta and location"""
    
    # Displaying welcoming message and header
    print("\n\n\t\t\t\t+--------------- Welcome to Techno Property Nepal ---------------+\n")

    # Calling a function to display details of the available land
    display_Details_Of_File() 
    
    # printing table last line
    print("\n \t\t\t\t+------------------------------------------------------+")
    
    # Printing inforamtion user to choose a kitta number for buying/renting a land
    print("\n\t\t\t__________Choose kitta number to buy/rent a land_____________\n")





def display_Details_Of_File():
    """
    This method is used to gather the details from the rent_details file 
    and displays the information in a tabular format.
    Args: none
    returns: none
    """

    # Reading the list of land from the file
    list_of_land = fileReader() 
    count = 1 
    
    # Loops through each land details
    for value in list_of_land:
        # Prints table header only once
        if count <= 1:
            print("""------------------------------------------------------------------------------------------------------------------------------""")
            print("""------------------------------------------------------------------------------------------------------------------------------""")
            count = count + 1

            # Prints column headers
            for k in value.keys():
                if k.strip() == "Availability":
                    print("|{:^19}".format(k) + "|", end="\n")
                    print("""------------------------------------------------------------------------------------------------------------------------------""")
                else:
                    print("|{:^19}".format(k) + "|", end="")
        
        # Prints values for each column
        for v in value.values():
            if v.strip().lower() in ["available", "not available", "unavailable"]:
                print("|{:^19}".format(v) + "|", end="\n")
            else:
                print("|{:^19}".format(v) + "|", end="")
    
    # Prints table footer
    print("""------------------------------------------------------------------------------------------------------------------------------""")






def after_Intro(count, rented_list_by_user):
    """This is the process after displaying intro to the user which asks for kitta from the user and performs other processes.
    Args:
    count(int):To keep track of logins by user
    rented_list_by_user(list):list of land picked by user

    retunrs:
    list: updated list of rented land
    
    """

    # Open rentedLand.txt file in write mode to clear its content
    file = open('rentedLand.txt', 'w')
    # Clear the file
    bill = f"""{file.write("")}"""
    file.close()
    
    # Sets the Boolean variable to True for loop
    userTryAgain = True
    
    # Loop 
    while userTryAgain:
        # String variable to store message like successfull,failure.Initailization with empty string 
        message = ""
        # assignment of kitta to a string value
        user_picked_kitta_number = 'y'
        
        # Ask user to input kitta number of the available land
        user_picked_kitta_number = input("Enter the kitta number of the available land:------>")
        
        # Check if the input is not a digit, then validate it
        if (not user_picked_kitta_number.isdigit()):
            user_picked_kitta_number = int(user_input_validator(user_picked_kitta_number))
        else:
            user_picked_kitta_number = int(user_picked_kitta_number)

        try:
            # executing land purchase process by calling land_Purchase() and capturing the returned value in tuple
            message, count, rented_list_by_user = land_Purchase(user_picked_kitta_number, rented_list_by_user, count)
            print(message) 
        except:
            print(message)
        
        # Ask user if they want to buy again
        user_Confirmation_to_exit = input("Do you want to buy again: (y/n) >")
        
        # If user doesn't want to buy again, reset variables and print bill
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            rented_list_by_user = []
            count = 0
            bill_printer()
            return rented_list_by_user
        else:
            display_The_Intro()

        




def land_Purchase(kittaInputFromUser,rented_list_by_user,count):
    """
    Purchases a land Kitta if available.

    Args:
        kitta_number (int): The Kitta number the user wants to purchase.
        rented_lands (list): A list containing dictionaries representing rented lands.
        count: counter to track the logins

    Returns:
        tuple
    """
    
    kittaInputFromUser = int(kittaInputFromUser)
    print(kittaInputFromUser) 
    details_Of_File_Holder = fileReader()
    user_Picked_Land_Holder= {} 
    # Boolean variable to check existing kitta num
    kitta_num_existing_checker = False
    kitta_num = kittaInputFromUser 
    indexing_for_existed_kitta=0 
    # Loop through each land in the lands list
    for i in range(len(details_Of_File_Holder)):
        # Check if the kitta number matches and the land is available
        if(int(details_Of_File_Holder[i]['Kitta']) == kittaInputFromUser ):
            kitta_num = kittaInputFromUser
            indexing_for_existed_kitta = i 
        # setting kitta_existing_checker to true
            kitta_num_existing_checker=True
            
            
        # passes through if kitta number is available in list of land details
    if(kitta_num_existing_checker):
        user_Picked_Land_Holder = details_Of_File_Holder[indexing_for_existed_kitta]

        print("kitta = "+ user_Picked_Land_Holder['Kitta']+"\nLocation = " + user_Picked_Land_Holder['Location'])
        print("Land Faced = "+ user_Picked_Land_Holder['Direction(land)']+"\nAnna= " + user_Picked_Land_Holder['Anna'])
        print("Availability = "+ user_Picked_Land_Holder['Availability']+"\nPrice = " + user_Picked_Land_Holder['Price(per/month)']+"\n")
        # checking if user_picked kittas availability is available or not
        if user_Picked_Land_Holder['Availability'].lower() == "available":
            # Ask for user confirmation to purchase
            user_Confirmation = input(f"Are you sure to buy kitta no {kittaInputFromUser} of price {user_Picked_Land_Holder['Price(per/month)']}: (y/n)")
            # if user confirmation is yes then further proceeds
            if(user_Confirmation.lower() == "y" or user_Confirmation.lower() == "yes"):
            # Making bill according to user provided details, it returns counter to track logins by user and rented_list contins user_rented land
                count,rented_list_by_user=bill_maker(rented_list_by_user,user_Picked_Land_Holder,count=count)
                updating_Details_in_rentFile(details_Of_File_Holder,kitta_num,'rent') 
            # returns a message,counter and list of rented land
                return ("Purchase successfull",count,rented_list_by_user) 
            
            else:
            # returns a message,counter and list of rented land
                return "failed",count,rented_list_by_user
        else:
            # prints error message if user picked land availability is not available
            return f"try again this land is {user_Picked_Land_Holder['Availability']}",count,rented_list_by_user

    else:
        
        print("enter a valid kitta number")
        after_Intro(count,rented_list_by_user)
        # returns a message,counter and list of rented land
        return "failed",count,rented_list_by_user



def return_Land_Process(user_input_kitta, count, user_picked_returnable_land):
    """This method basically handles all he return process which include choosing a land checking and so on
    Args:
    user_input_kitta(int):kitta of available land
    count(int):counter to track down the user logins
    user_picked_returnable_land(list):list which includes list of user picked returnable land

    Returns:tuple(message,count,user_picked_retunable_land)
    
    """

    # Read the list of lands from the file
    list_Of_Land = fileReader() 

    # Initialize a flag to control the loop
    userTryAgain = True
    
    # Start a loop to handle user input and process the return
    while userTryAgain:
        
        # Check if the provided kitta number exists in the list of lands
        result_Of_Checker = kitta_Available_Checker(user_input_kitta, list_Of_Land)
        
        # If the kitta number exists
        if result_Of_Checker != "null":
            # Check if the land corresponding to the kitta number is rented
            if list_Of_Land[result_Of_Checker]['Availability'] == "Not Available":
                # Retrieve the details of the rented land
                current_picked_land = list_Of_Land[result_Of_Checker]
        
                # Prompt the user to input the number of months they've rented the land
                user_month = input("Enter for how many months you have rented?>>>")
                user_month = user_input_validator(user_month)
                while int(user_month) < 1 or int(user_month) > 12:
                    user_month = input("Enter a valid number of months you have rented?>>>")
                
                # Prompt the user to input the current month
                current_month = input("Enter the running month>>>>")
                current_month = user_input_validator(current_month)
                while int(current_month) < 1 or int(current_month) > 12 or str(current_month).isalpha():
                    current_month = input("Enter the running month>>>>")
                    user_input_validator(current_month)
                    
                # Check if the rental duration has exceeded
                if int(current_month) > int(user_month):
                    # Calculate penalty for exceeding rental duration
                    exceded_Month = int(current_month) - int(user_month)
                    penalty_Price = int(exceded_Month) * 20000
                    print("<---------------------      You have exceeded the time limit      ------------->")
                    print("<----------------------     Penalty will be added to your bill        ------------>")
                    print(f"""<-----------------          {exceded_Month} month-> {penalty_Price}               ------------->""")
                    
                    # Update the count and rented lands list with penalty
                    count, user_picked_returnable_land = return_bill_maker(current_picked_land, user_picked_returnable_land, count=count, month=current_month, price=penalty_Price)
                else:
                    # Update the count and rented lands list without penalty
                    count, user_picked_returnable_land = return_bill_maker(current_picked_land, user_picked_returnable_land, count=count, month=current_month,price=penalty_Price)
                    
                # Update the rented lands list and rental file
                updating_Details_in_rentFile(list_Of_Land, user_input_kitta, "return")
                
                # Return success message, updated count, and rented lands list
                return "Return successful", count, user_picked_returnable_land
            else:
                # If the land is not rented, inform the user
                print("The land of kitta number " + str(user_input_kitta) + " is available on sale")
                # Return failure message and the current count and rented lands list
                return "failed", count, user_picked_returnable_land
        else:
            # If the provided kitta number doesn't exist, inform the user
            print("Kitta Number Doesn't Exist")
            # Return failure message and the current count and rented lands list
            return "failed", count, user_picked_returnable_land 

        

def land_return_starter(count,user_picked_returnable_land):
    """This is starter for land returning process
    Args:
    count(int),user_picked_returnable_land:(List)
    Returns:
    user_picked_returnable_land(List):updated version of user picked kitta num land
    """
    
    userTryAgain = True
     # Opens the file 'rentedLand.txt' in write and assign the return value to file
    file = open('rentedLand.txt','w')
    # Clears all the content in rentedLand.txt to Empty
    bill = f"""{file.write("")}"""
    # file is closed
    file.close()
    while(userTryAgain):
        # assigning message to empty
        message = ""
        kitta_from_user = "y"
        # Asking user to input kitta number
        kitta_from_user = input("Enter the kitta number of available land----->")
        # continues if kitta is not digit
        if(not kitta_from_user.isdigit()):
            # validates the kitta asks to input kitta until it is a number
            kitta_from_user = int(user_input_validator(kitta_from_user))

        try:
            # trying to execute this block of code which the process for returning land
            message,count,user_picked_returnable_land= return_Land_Process(kitta_from_user,count,user_picked_returnable_land)
            print(message)
        except:
            # catches error if try block encounters some error
            print(message)
        # Asking user if he wants to buy more land
        user_Confirmation_to_exit = input("Do you want to return the land again: (y/n) >")
        # if user confirmed no then all the bills are printed.
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            bill_printer()
            return user_picked_returnable_land
        else:
            display_The_Intro()

    
    
def bill_printer():
    """This method helps to print the bill generated during renting or returning process
    Args:None
    Returns:none
    """
    # Opens the file 'rentedLand.txt' and assign the return value to file
    file = open('rentedLand.txt')
    # sets the content of file to bill
    bill = f"""{file.read()}"""
    # Print the bill with user details
    print(bill) 
    # closes the files
    file.close()    
    




def kitta_Available_Checker(kitta_num,list_value):
    """This method take int and a list as a parameter \n and returns int value if int value exists in list else null 
    parameter:int , list
    returns:True or null"""
    # setting kitta available and index_capturer to false initially
    is_Kitta_available = False
    index_Capturer = 0
    # looping in each index of range of length list_value
    for i in range(len(list_value)):
        # passes through if kitta_num is existed in list_value
        if(list_value[i]['Kitta'] == str(kitta_num) or list_value[i]['Kitta'] == kitta_num):
                index_Capturer = i
                is_Kitta_available = True
                break
        
    if(is_Kitta_available):         
        # returns the index of kitta available in list   
        return index_Capturer
    else:
        return "null"
    

def user_input_validator(user_input):
    """
    This method helps to validate the user input value

    args:
    user_input(Any)

    returns:
    user_input(int)
    """
    # passes if user_input is not a number
    while( not user_input.isdigit()):
        try:
            # trying to convert the intput value to int
            user_input = int(input("Enter a kitta valid int input>>>"))
        except:
            # catches the errror if user input value is not int
            print("<---------Enter a kitta valid int input------>")
            continue
        if(str(user_input).isdigit()):
            # retruns integer value
            return user_input
    return user_input


        
