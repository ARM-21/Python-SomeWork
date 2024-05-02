
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


user_name_holder=""
user_address_holder =""
user_phone_holder = 0



def user_input_validator(user_input):
    while( not user_input.isdigit()):
        try:
            user_input = int(input("Enter a valid int input>>>"))
        except:
            print("<---------Enter a valid int input------>")
            continue
        if(str(user_input).isdigit()):
            return user_input
    return user_input

def return_bill_maker(user_Picked_Land_Holder,return_list,count,month,price=0):
    name = ""
    phone = ""
    address = ""
    total_return =0
    global user_name_holder,user_phone_holder,user_address_holder
    middle_return_bill = ""
    if(count== 0):
        count = count+1
                
        name = input("Enter your name:>>>")
        phone= input("Enter len()=10 your Phone Number: >>")
                        
        while(len(phone) <10 or not (phone.isdigit())):
            phone = input("Enter a valid int phone length=10 of  phone Number:>>")

        address = input("Enter your address>>> ")
        rented_owner_dict = {'Name':name,'Duration':month}
        rented_owner_dict.update(user_Picked_Land_Holder)
        return_list.append(rented_owner_dict)
        user_name_holder = name
        user_address_holder=address
        user_phone_holder = phone

    else:
        count = count + 1
        rented_owner_dict = {'Name':user_name_holder,'Duration':month}
        rented_owner_dict.update(user_Picked_Land_Holder)
        return_list.append(rented_owner_dict)





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
    for value in return_list:
                if (value['Name'] == user_address_holder and count > 1) :
                    i += 1
                    middle_return_bill = middle_return_bill + f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                    total_return = total_return + (int(value['Price(per/month)']) * int(month)) + int(price)
                else:
                    i += 1
                    middle_return_bill = middle_return_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                    total_return = total_return + (int(value['Price(per/month)']) * int(month)) + int(price)

    bottom_return_bill = f"""
    ---------------------------------------------------------------------------------------------------------
    |                                                                        Total :{total_return:<18}      |
    |                                                                        VAT   : 13 %                   |
    |                                                                  Grand Total :{(total_return + (total_return * 0.13)):<22}  |
    --------------------------------------------------------------------------------------------------------
    """

    
    return_bill_format = top_return_bill + middle_return_bill + bottom_return_bill
    file = open("rentedLand.txt","w")
    file.write(return_bill_format) 
    file.close()
    return count,return_list


def nameValidator(name):
    updated_name = name.strip()
    updated_name_list= name.split()
    print(updated_name)
    while(updated_name.strip().isdigit() and len(updated_name.strip())<3):
        updated_name = input("Enter a name(name must be non numeric value) or length > 3 in string>> ")
    
    i =0
    while(i<len(updated_name) and updated_name_list[i].isdigit()):
        # if(updated_name[i].isdigit):
        updated_name = input("Enter a name(name must be non numeric value) or length > 3 in string>> ")
            # break
        i= i+1
            
    return updated_name



# this is a example of tuple
my_tuple = ("apple", "banana", "cherry")
# printing tuple
print(my_tuple[0])





def bill_maker(rented_list,user_Picked_Land_Holder,count,month=0):
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
        name = input("Enter your name:>>> ")
        name = nameValidator(name) # Validate name input

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
    |                                                                  Grand Total :{(total + (total * 0.13)):<22}  |
    --------------------------------------------------------------------------------------------------------"""

    # Concatenate the entire bill format
    return_bill_format = top_rented_bill+middle_rented_bill+bottom_rented_bill
    # Write the bill to a file
    file = open("rentedLand.txt","w")
    #Writes the return_bill_format content in file
    file.write(return_bill_format) 
    file.close()
    # Returns the updated count and rented_list
    return count, rented_list
