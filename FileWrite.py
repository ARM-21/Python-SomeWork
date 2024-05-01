
from datetime import datetime 


def updating_Details_in_rentFile(old_details_of_file_As_List,existed_kitta,from_Where,file_path="rent_details.txt"):
    for value in old_details_of_file_As_List:
        if(int(value['Kitta'])== existed_kitta or value['Kitta'] == str(existed_kitta)):
            if(from_Where == "rent"):
                
                value['Availability'] = 'Not Available'
            elif(from_Where == "return"):
                
                 value['Availability'] = 'Available'
            file = open(file_path,'w')
            
            for value in old_details_of_file_As_List:
                file.write(f"{value['Kitta']},{value['Location']},{value['Direction(land)']},{value['Anna']},{value['Price(per/month)']},{value['Availability']}"+"\n")
            file.close()
user_name_holder=""
user_address_holder =""
user_phone_holder = 0



def bill_maker(rented_list,user_Picked_Land_Holder,count,month=0):
    global user_address_holder,user_phone_holder,user_name_holder
    middle_rented_bill = ""
    name =""
    address=""

    i =0 
    total =0
    phone =0

   
    if(count == 0):
                count = count + 1
    
                name = input("Enter your name:>>>")
                phone= input("Enter len()=10 your Phone Number: >>")
                                
                while(len(phone) <10 or not (phone.isdigit())):
                    phone = input("Enter a length=10 of  phone Number:>>")
                address = input("Enter your address>>> ")
                month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
                month = user_input_validator(month) 
                
                rented_owner_dict = {'Name':name,'Duration':month}
                rented_owner_dict.update(user_Picked_Land_Holder)
                rented_list.append(rented_owner_dict)
                user_name_holder = name
                user_address_holder = address
                user_phone_holder = phone
            
                
    else:
        
                count = count +1
                month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
                month = user_input_validator(month) 
                rented_owner_dict = {'Name':user_name_holder,'Duration':month}
                rented_owner_dict.update(user_Picked_Land_Holder)
                rented_list.append(rented_owner_dict)
            
            
        
    top_rented_bill =f"""
    =========================================================================================================
    |bill No:-{int(datetime.now().timestamp()):10}                                                                                   |
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
    for value in rented_list:
                        
            if(value['Name'] == user_name_holder and count > 1):
                    count = count +1
                    i += 1
                    middle_rented_bill =middle_rented_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                    total = total + (int(value['Price(per/month)'])*int(month))
            else:
                i+=1
                count += 1
                middle_rented_bill = f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                total = total + (int(value['Price(per/month)'])*int(month))   
    
    bottom_rented_bill =f"""
    ---------------------------------------------------------------------------------------------------------
    |                                                                        Total :{total:<18}      |
    |                                                                        VAT   : 13 %                   |
    |                                                                  Grand Total :{(total + (total * 0.13)):<22} |
    --------------------------------------------------------------------------------------------------------
    """


    return_bill_format = top_rented_bill+middle_rented_bill+bottom_rented_bill
    file = open("rentedLand.txt","w")
    file.write(return_bill_format) 
    file.close()
    return count,rented_list                 
    







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


