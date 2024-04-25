from fileRead import fileReader
from datetime import datetime 
# listOF = fileReader() 


def updating_Details_in_rentFile(old_details_of_file_As_List,existed_kitta,from_Where,file_path="rent_details.txt"):
    # updated_list = old_details_of_file_As_List
    # print(updated_list) 
    # print(old_details_of_file_As_List)
    print(type(existed_kitta))
    for value in old_details_of_file_As_List:
        if(int(value['Kitta'])== existed_kitta or value['Kitta'] == str(existed_kitta)):
            if(from_Where == "rent"):
                print("from rent")
                value['Availability'] = 'Not Available'
            elif(from_Where == "return"):
                 print("from return")
                 value['Availability'] = 'Available'
            file = open(file_path,'w')
            
            for value in old_details_of_file_As_List:
                file.write(f"{value['Kitta']},{value['Location']},{value['Direction(land)']},{value['Anna']},{value['Price(per/month)']},{value['Availability']}"+"\n")
            file.close()


def bill_maker(name,address,phone,rented_land_Owner_List,month,price=0):
    
    middle_bill = ""
    total =0
    i =0 
    top_bill =f"""
    =========================================================================================================
    |                                        Techno Property Nepal                                          |
    |                               Hospital Chowk  -   10, Pokhara Nepal                                   |
    |                    VAT:5999524                             Ph. No: {phone:10}                         |
    |=======================================================================================================|
    |              Name : {name:<20}                              Date: {datetime.now().date()}                |
    |              Address : {address:<15}                                                                |
    |              Phone: {phone:<10}                                                                        |
    |-------------------------------------------------------------------------------------------------------|
    |-------------------------------------------------------------------------------------------------------|
    | SN |     Kitta      |  Location     |   Anna   |  Direction    |  Duration       |   Price            |
    |-------------------------------------------------------------------------------------------------------|"""
    for value in rented_land_Owner_List:
                        
                        if(value['Name'] == name):
                             i += 1
                             middle_bill =middle_bill+f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}| {value['Price(per/month)']:^19}|"""
                             total = total + (int(value['Price(per/month)'])*int(month))+int(price)
                        else:
                            i +=1
                            middle_bill =middle_bill + f"""
    |{i:^4}|{value['Kitta']:^16}|{value['Location']:^15}|{value['Anna']:^10}|{value['Direction(land)']:^15}|    {value['Duration']:^13}|{value['Price(per/month)']:^18} |"""
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

