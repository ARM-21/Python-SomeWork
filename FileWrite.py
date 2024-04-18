from FileRead import fileReader
# listOF = fileReader();


def updating_Details_in_rentFile(old_details_of_file_As_List,existed_kitta,file_path="rent_details.txt"):
    # updated_list = old_details_of_file_As_List
    # print(updated_list);
    # print(old_details_of_file_As_List)
    for value in old_details_of_file_As_List:
        if(int(value['Kitta'])== existed_kitta):
            value['Availability'] = 'Not Available'

    
            file = open(file_path,'w')
            file.write('Kitta,Location,Direction(land),Anna,Price(per/month),Availability'+"\n")
            for value in old_details_of_file_As_List:
                file.write(f"{value['Kitta']},{value['Location']},{value['Direction(land)']},{value['Anna']},{value['Price(per/month)']},{value['Availability']}"+"\n")
            file.close()
#   print(updated_list);
#     print(old_details_of_file_As_List)
# updating_Details_in_rentFile(listOF,101)


# file = open("rent_details.txt")
# fileInput = file.readlines()
# file.close()
# print(fileInput);

# from datetime import datetime

# dateAndTime = datetime.now();
# date = dateAndTime.date()
# time = dateAndTime.time()
# print(dateAndTime,date)
def bill_maker(name,address,phone,rented_land_Owner_List):
    # phone="984000000"
    middle_bill = ""
    top_bill =f"""
                                        Trading Property Nepal
                                Hospital Chowk  -   10, Pokhara Nepal
                        VAT:5999524                                Ph. No: {phone}
                                                                
                    Name : {name:10}                                     Date:
                    Address : {address:10}
                    phone: {phone:10}

                ------------------------------------------------------------------------
                | SN | Name                                             |  Price        |
                ------------------------------------------------------------------------
                """
    # invoice = open('rentedLand.txt','w')
    for value in rented_land_Owner_List:
                        i =0;
                        total = 0;
                        # print(value)
                        if(value['Name'] == name):
                             i += 1;
                             middle_bill =middle_bill+f"""   |{i:^3}  | {value['Kitta']}                                          |{value['Price(per/month)']} |\n
               """
                            
                            # invoice.write("Name, kitta  , Location  , LandFaced  , Price , PhoneNumber ,  Duration  , Date  , Time\n")
                            # invoice.write(f"{name_Of_land_owner},{user_Picked_Land_Holder['Kitta']},{user_Picked_Land_Holder['Location']},{user_Picked_Land_Holder['Direction(land)']},{user_Picked_Land_Holder['Price(per/month)']},{period_Of_rent},{str(datetime.now().time())},{str(datetime.now().time())}\n")
                            # bill_maker(name,phone,value)
                            # invoice.write(f"{land}  ,  {value['Kitta']},  {value['Location']}  ,  {value['Direction(land)']}  ,  {value['Price(per/month)']}  ,{phone},  {period_Of_rent}  ,{str(datetime.now().date())}  ,  {str(datetime.now().time())}\n")



                        else:
                            # phone = 
                            value['Name']= name;
                            i += 1;
                            middle_bill =f"""|{i:^3}  | {value['Kitta']}                                            |  {value['Price(per/month)']}   |"""

                        bottom_bill =f"""
                -------------------------------------------------------------------------
                                                                            Total :{total + int(value['Price(per/month)'])}
                                                                            VAT   : 13 %
                                                                      Grand Total : {total + (int(value['Price(per/month)'])) * 0.13}
                            # invoice = open('rentedLand.txt','w')
                            #
                            # # invoice.write("Name,  kitta  ,Location  ,  Land Faced  ,  Price  ,  PhoneNumber  , Duration  ,  Date  , Time\n")
                            # invoice.write(f"{name}, {user_Picked_Land_Holder['Kitta']} ,{user_Picked_Land_Holder['Location']}  ,{user_Picked_Land_Holder['Direction(land)']}  , {user_Picked_Land_Holder['Price(per/month)']} , {phoneNumber} ,{period_Of_rent}  ,{str(datetime.now().date())}  ,{str(datetime.now().time())}\n") 
                            break;




    
    # middle_bill =middle_bill + f"""\n
    #             | {i}  | {user_choice_land[]}                                       |  |  |  |      |
               
    # """

                    

    """
    bill_format = top_bill+middle_bill+bottom_bill;
    file = open("rentedLand.txt","w")
    file.write(bill_format);
    file.close()
    return bill_format;


# print(bill_maker("manoj","mars","9849320765","hello"));




# bill =f"""
#                                     Trading Property Nepal
#                             Hospital Chowk  -   10, Pokhara Nepal
#                     VAT:5999524                                Ph. No: 984932000
                                                              
#                 Name : man                                     Date:lan
#                 Address :tan
#                 phone:ran

#             ------------------------------------------------------------------------
#             | SN | Name                                             | aa|bb|cc|dd   |
#             ------------------------------------------------------------------------
#             | 1  | samir tori                                       |  |  |  |      |
#             | 1  | samir tori                                       |  |  |  |      |
#             | 1  | samir tori                                       |  |  |  |      |
#             -------------------------------------------------------------------------
#                                                                         Total :
#                                                                         VAT   :
#                                                                   Grand Total : 
                 
                 
                 
                 
# """
# print(bill)
# bill_maker()




def ask_user():
    print("<<<<<<<Choose the following options>>>>>")  
    print("    1.Rent Land \n      2.Return Land \n ")

    while(True):
        user_choice = int(input("Enter your choice"))
        if(user_choice == 1):
            print("hahha")
            break
        elif(user_choice == 2):
            print("alla")
            break

