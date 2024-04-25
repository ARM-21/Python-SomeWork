from fileRead import fileReader
from datetime import datetime 
# listOF = fileReader() 


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

counter = 0

def bill_maker(rented_list,user_Picked_Land_Holder,count,from_where,price=0,month=0):
    global counter,user_address_holder,user_phone_holder,user_name_holder
    middle_bill = ""
    total =0
    i =0 
    name =""
    phone =0
    address=""
    print(count)
    if(counter == 0):
            if(from_where == 'rent'):
                count = count + 1
                counter = counter +1
                name = input("Enter your name:>>>")
                phone= input("Enter len()=10 your Phone Number: >>")
                                
                while(len(phone) <10 or not (phone.isdigit())):
                    phone = input("Enter a length=10 of  phone Number:>>")
                address = input("Enter your address>>> ")
                month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
                month = user_input_validator(month) 
                
                rented_owner_dict = {'Name':'','Duration':month}
                rented_owner_dict.update(user_Picked_Land_Holder)
                rented_list.append(rented_owner_dict)
              
            else:
                counter = counter+1
                
                name = input("Enter your name:>>>")
                phone= input("Enter len()=10 your Phone Number: >>")
                                
                while(len(phone) <10 or not (phone.isdigit())):
                    phone = input("Enter a length=10 of  phone Number:>>")
                address = input("Enter your address>>> ")
                rented_owner_dict = {'Name':'','Duration':month}
                rented_owner_dict.update(user_Picked_Land_Holder)
                rented_list.append(rented_owner_dict)
            user_name_holder = name
            user_address_holder=address
            user_phone_holder = phone

            
                   
    else:
        counter = counter+1
        if(from_where == "rent"):
            count = count +1
            month = input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")
            month = user_input_validator(month) 
            rented_owner_dict = {'Name':user_name_holder,'Duration':month}
            rented_owner_dict.update(user_Picked_Land_Holder)
            rented_list.append(rented_owner_dict)
        elif(from_where == "return"):
            rented_list[0]['Name'] = user_name_holder
            rented_owner_dict = {'Name':user_name_holder,'Duration':month}
            rented_owner_dict.update(user_Picked_Land_Holder)
            rented_list.append(rented_owner_dict)
             
        
    top_bill =f"""
    =========================================================================================================
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
                        
                        if(value['Name'] == name):
                             i += 1
                             middle_bill =middle_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                             total = total + (int(value['Price(per/month)'])*int(month))+int(price)
                        else:
                            i+=1
                            middle_bill = middle_bill + f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                            total = total + (int(value['Price(per/month)'])*int(month))+int(price)   
    
    bottom_bill =f"""
    ---------------------------------------------------------------------------------------------------------
    |                                                                        Total :{total:<18}      |
    |                                                                        VAT   : 13 %                   |
    |                                                                  Grand Total :{(total + (total * 0.13)):<22}|
    --------------------------------------------------------------------------------------------------------
    """
                           
                        # break 

               
    bill_format = top_bill+middle_bill+bottom_bill 
    file = open("rentedLand.txt","w")
    file.write(bill_format) 
    file.close()
    return bill_format 


# def bill_maker(name,address,phone,rented_land_Owner_List,month,price=0):
    
#     middle_bill = ""
#     total =0
#     i =0 
#     top_bill =f"""
#     =========================================================================================================
#     |                                        Techno Property Nepal                                          |
#     |                               Hospital Chowk  -   10, Pokhara Nepal                                   |
#     |                    VAT:5999524                             Ph. No: {phone:10}                         |
#     |=======================================================================================================|
#     |              Name : {name:<20}                              Date: {datetime.now().date()}                |
#     |              Address : {address:<15}                                                                |
#     |              Phone: {phone:<10}                                                                        |
#     |-------------------------------------------------------------------------------------------------------|
#     |-------------------------------------------------------------------------------------------------------|
#     | SN |     Kitta      |  Location     |   Anna   |  Direction    |  Duration       |   Price            |
#     |-------------------------------------------------------------------------------------------------------|"""
#     for value in rented_land_Owner_List:
                        
#                         if(value['Name'] == name):
#                              i += 1
#                              middle_bill =middle_bill+f"""
#     |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
#                              total = total + (int(value['Price(per/month)'])*int(month))+int(price)
#                         else:
#                             i +=1
#                             middle_bill =middle_bill + f"""
#     |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}|{value['Price(per/month)']:^18} |"""
#                             total = total + (int(value['Price(per/month)'])*int(month))+int(price)   
    
#     bottom_bill =f"""
#     ---------------------------------------------------------------------------------------------------------
#     |                                                                        Total :{total:<18}      |
#     |                                                                        VAT   : 13 %                   |
#     |                                                                  Grand Total :{(total + (total * 0.13)):<22}|
#     --------------------------------------------------------------------------------------------------------
#     """
                           
#                         # break 

               
#     bill_format = top_bill+middle_bill+bottom_bill 
#     file = open("rentedLand.txt","w")
#     file.write(bill_format) 
#     file.close()
#     return bill_format 





# file = open('rentedLand.txt')
# bill = f"""{file.read()}"""
# print(bill) 
# file.close()




# import mysql.connector 

# cone = mysql.connector.connect(
#       host="127.0.0.1",
#       user="root",
#       password="",
#       database="registration"
# )
# mycursor  = cone.cursor()
# mycursor.execute("SELECT * FROM details") 


# results = mycursor.fetchall() 

# print(results) 

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
