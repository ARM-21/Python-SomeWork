
from datetime import datetime 


# This function updates details in a rental file based on certain conditions.
def updating_Details_in_rentFile(old_details_of_file_As_List,existed_kitta,from_Where,file_path="rent_details.txt"):
    """
    This function updates details in a rental file based on certain conditions.

    Arguments:
    old_details_of_file_As_List (list): List containing dictionaries representing old details.
    existed_kitta (int): The Kitta number to search for.
    from_Where (str): Indicates the action to be performed, either "rent" or "return".
    file_path= (str): The path to the file to be read. Default is "rent_details.txt".

    Returns:
    None
    """
    # Iterate through each element in the old_details_of_file
    for value in old_details_of_file_As_List:
        # Check if the Kitta number matches user_provided_kiita
        if(int(value['Kitta'])== existed_kitta or value['Kitta'] == str(existed_kitta)):
            # check if the request is from rent then update the old deatils with value of availability to  not available
            if(from_Where == "rent"):
                value['Availability'] = 'Not Available'
            # check if the request is from return then update the old details with value of availability to available
            elif(from_Where == "return"):
                value['Availability'] = 'Available'
            # Open the file in write mode.
            file = open(file_path,'w')
            # Write the updated details back to the file.
            for value in old_details_of_file_As_List:
                file.write(f"{value['Kitta']},{value['Location']},{value['Direction(land)']},{value['Anna']},{value['Price(per/month)']},{value['Availability']}"+"\n")
            # Close the file.
            file.close()

# assigning a global variable to empty and 0 respectively
user_name_holder=""
user_address_holder =""
user_phone_holder = 0



def user_input_validator(user_input):
    """
    This function validates user input to ensure it is an integer.

    Args:
        user_input (str): The user input to be validated.

    Returns:
        int: The validated integer input.
    """
    while( not user_input.isdigit()):
        try:
            user_input = int(input("Enter a valid int input>>>"))
        except:
            print("<---------Enter a valid int input------>")
            continue
        # returns the user_input if user inputs integer
        if(str(user_input).isdigit()):
            return user_input
    return user_input

def return_bill_maker(user_Picked_Land_Holder,return_list,count,month,price=0):
    """
        This function generates a bill for returning rented land, which contains user details and rental information.

        Arguments:
            user_Picked_Land_Holder (dict): A dictionary containing details of the rented land.
            return_list (list): A list containing dictionaries representing rented lands.
            count (int): A counter to track the number of looping.
            month (int): The duration for rented land.
            price (int): The penalty price. Defaults to 0.

        Returns:
            tuple: A tuple containing the updated count and return_list.
    """

    name = ""  # User's name
    phone = ""  # User's phone number
    address = ""  # User's address
    total_return = 0  # Total amount to be returned
    global user_name_holder, user_phone_holder, user_address_holder  # Global variables to store user information
    middle_return_bill = ""  # Middle part of the bill

    # Check if this is the first transaction
    if(count== 0):
        count = count+1
        # asking user details like name,phone
        while True:
            # asking for name until user inputs the name correctly
            name = input("Please enter your name (first name or first and last name): ")
            # passes through only if user input is valid
            if name_validator(name):
                print(" your name is valid.")
                break
            else:
                print("Invalid name. Please enter alphabetic characters only, and a maximum of one space.")
                continue

        phone= input("Enter len()=10 your Phone Number: >>") 
        # Validate phone number length and format               
        while(len(phone) <10 or not (phone.isdigit())):
            phone = input("Enter a valid int phone length=10 of  phone Number:>>")

        address = input("Enter your address>>> ")
        # Creating dictionary for the rented land and update with user details
        rented_owner_dict = {'Name':name,'Duration':month}# Initialize dictionary with user's name and duration of rental
        rented_owner_dict.update(user_Picked_Land_Holder) # Update dictionary with details of the rented land
        # Appending the dictionary to the return list
        return_list.append(rented_owner_dict)
        # Updating global variables with user information
        user_name_holder = name
        user_address_holder=address
        user_phone_holder = phone

    else:
        count = count + 1
        # Creating dictionary for the rented land and update with user details
        rented_owner_dict = {'Name':user_name_holder,'Duration':month}
        # Initializing dictionary with user's name and duration of rental
        rented_owner_dict.update(user_Picked_Land_Holder)
        # Updating dictionary with details of the rented land
        return_list.append(rented_owner_dict)




# This is the top part of the bill format
    top_return_bill = f"""
    =========================================================================================================
    |bill No:-{int(datetime.now().timestamp()):10}                                                                                    |
    |                                        Techno Property Nepal                                          |
    |                               Hospital Chowk  -   10, Pokhara Nepal                                   |
    |                    VAT:5999524                             Ph. No: {user_phone_holder:10}                         |
    |=======================================================================================================|
    |              Name : {user_name_holder:<20}                              Date: {datetime.now().date()}                |
    |              Address : {user_address_holder:<15}                                                                |
    |              Phone: {user_phone_holder:<10}                                                                        |
    |-------------------------------------------------------------------------------------------------------|
    |-------------------------------------------------------------------------------------------------------|
    | SN |     Kitta      |  Location     |   Anna   |  Direction    |  Duration       |       Price        |
    |-------------------------------------------------------------------------------------------------------|"""
    i = 0
    # Iterate through the return list and construct the middle part of the bill format
    for value in return_list:
                # Check if the current land belongs to the same user and if there have been multiple transactions
                if (value['Name'] == user_address_holder and count > 1) :
                    i += 1
                    # concanating details to middle section of the bill
                    middle_return_bill = middle_return_bill + f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                    # Calculate the total amount
                    total_return = total_return + (int(value['Price(per/month)']) * int(month)) + int(price)
                else:
                    i += 1
                    # concanating details to middle section of the bill
                    middle_return_bill = middle_return_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                    total_return = total_return + (int(value['Price(per/month)']) * int(month)) + int(price)

# This is  the bottom part of the bill format
    bottom_return_bill = f"""
    ---------------------------------------------------------------------------------------------------------
    |                                                                        Total :{total_return:<18}      |
    |                                                                        VAT   : 13 %                   |
    |Process:-returning                                                Grand Total :{(total_return + (total_return * 0.13)):<22}  |
    ---------------------------------------------------------------------------------------------------------
    """

    # Joining the bill parts to form the complete bill format
    return_bill_format = top_return_bill + middle_return_bill + bottom_return_bill
    file = open("rentedLand.txt","w")
    file.write(return_bill_format) 
    file.close()
    return count,return_list



    return updated_name



def name_validator(name):
    """
        This function validates a given name. if user input is integer or space.

        Args:
        name (str): The name to be validated.

        Returns:
        str: The validated name.
        """


    # Split the name based on spaces
    parts = name.split()
    
    # Check each part is alphabetic
    for part in parts:
        if not part.isalpha() or len(name) <=2 or name.isspace():
            return False  # Contains non-alphabetic characters

    # If all checks pass, the name is valid
    if(len(name.strip()) >=3 ):
        return True
    return False








def bill_maker(rented_list,user_Picked_Land_Holder,count,month=0):
    """
    This function generates a bill for renting land, including user information and rental details.

    Args:
        rented_list (list): A list containing dictionaries containing rental details.
        user_Picked_Land_Holder (dict): A dictionary containing details of the user picked land.
        count (int): The count of user purchase.
        month (int): The duration of the rented by user. Defaults to 0.

    Returns:
        tuple: A tuple containing the updated count and rented_list.
    """


    # Global variables to store user information
    global user_address_holder,user_phone_holder,user_name_holder
    middle_rented_bill = "" # Initialize empty string for middle section of the bill
    name ="" # Initialize name variable
    address="" # Initialize address variable
    
    # Initialize variables for indexing, total price, and phone number
    i = 0 
    total = 0
    phone = 0

    # If count is 0, it's a new rental, so gather user information
    if(count == 0):
        count = count + 1
        # asking name from  user
        while True:
            # asking for name until user inputs the name correctly
            name = input("Please enter your name (first name or first and last name): ")
            # passes through only if user input is valid
            if name_validator(name):
                print(" your name is valid.")
                break
            else:
                print("Invalid name. Please enter alphabetic characters only, and a maximum of one space.")
                continue

        phone= input("Enter len()=10 your Phone Number: >> ")
        # chceks phone number is valid
        while(len(phone) <10 or not (phone.isdigit())):
            phone = input("Enter a length=10 of  phone Number:>> ")
        address = input("Enter your address>>> ")
        # Ask for rental duration
        month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
        month = user_input_validator(month) # Validate month input
        # Create dictionary to store user and land details
        rented_owner_dict = {'Name':name,'Duration':month}
        # Merge user and land details
        rented_owner_dict.update(user_Picked_Land_Holder)
        # Append details to rented_list
        rented_list.append(rented_owner_dict)
        # Stores user information globally(outside this block/global to this function)
        user_name_holder = name
        user_address_holder = address
        user_phone_holder = phone
        
    else:
        count = count +1
        # Asking for rental duration
        month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
        month = user_input_validator(month) # Validate month input
        # Create dictionary to store user deatils
        rented_owner_dict = {'Name':user_name_holder,'Duration':month}
        # Merge user and land details
        rented_owner_dict.update(user_Picked_Land_Holder)
        # Append details to rented_list
        rented_list.append(rented_owner_dict)
            
    # Generate top section of the bill
    top_rented_bill =f"""
    =========================================================================================================
    |bill No:-{int(datetime.now().timestamp()):10}                                                                                    |
    |                                        Techno Property Nepal                                          |
    |                               Hospital Chowk  -   10, Pokhara Nepal                                   |
    |                    VAT:5999524                             Ph. No: {user_phone_holder:10}                         |
    |=======================================================================================================|
    |              Name : {user_name_holder:<20}                              Date: {datetime.now().date()}                |
    |              Address : {user_address_holder:<15}                                                                |
    |              Phone: {user_phone_holder:<10}                                                                        |
    |-------------------------------------------------------------------------------------------------------|
    |-------------------------------------------------------------------------------------------------------|
    | SN |     Kitta      |  Location     |   Anna   |  Direction    |  Duration       |       Price        |
    |-------------------------------------------------------------------------------------------------------|"""

    # Loop through rented_list to generate middle section of the bill
    for value in rented_list:
        # Check if user's name matches, increment count accordingly
        if(value['Name'] == user_name_holder and count > 1):
            count = count +1
            i += 1
            # Append details to middle section of the bill
            middle_rented_bill =middle_rented_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
            # Calculate total price
            total = total + (int(value['Price(per/month)'])*int(month))
        else:
	
            i+=1
            count += 1
            #  middle section of the bill for each rented values
            middle_rented_bill = f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
            # Calculate total price
            total = total + (int(value['Price(per/month)'])*int(month))   

    # stores bottom section of the bill
    bottom_rented_bill =f"""
    ---------------------------------------------------------------------------------------------------------
    |                                                                        Total :{total:<18}      |
    |                                                                        VAT   : 13 %                   |
    |Process:-renting                                                  Grand Total :{(total + (total * 0.13)):<22}  |
    ---------------------------------------------------------------------------------------------------------"""

    # Concatenate the entire bill format
    return_bill_format = top_rented_bill+middle_rented_bill+bottom_rented_bill
    # Write the bill to a file
    file = open("rentedLand.txt","w")
    #Writes the return_bill_format content in file
    file.write(return_bill_format) 
    file.close()
    # Returns the updated count and rented_list
    return count, rented_list

