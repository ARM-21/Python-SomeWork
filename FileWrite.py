from FileRead import fileReader
from datetime import datetime;
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

def bill_maker(name,address,phone,rented_land_Owner_List):
    # phone="984000000"
    middle_bill = ""
    total =0
    i =0;
    top_bill =f"""
                                        Techno Property Nepal
                                Hospital Chowk  -   10, Pokhara Nepal
                        VAT:5999524                                Ph. No: {phone}
                                                                
                    Name : {name:10}                               Date: {datetime.now().date()}
                    Address : {address:10}
                    phone: {phone:10}

                ------------------------------------------------------------------------
                | SN | Name                                             |  Price        |
                ------------------------------------------------------------------------
                """
    # invoice = open('rentedLand.txt','w')
    for value in rented_land_Owner_List:
                        
                       
                        # print(value)
                        if(value['Name'] == name):
                             i += 1;
                             middle_bill =middle_bill+f"""
                |{i:^3} | {value['Kitta']}                                              |   {value['Price(per/month)']}      |"""
                             total = total + int(value['Price(per/month)'])
                        else:
                            
                            # phone = 
                            value['Name']= name;
                            i += 1;
                            middle_bill =f"""|{i:^3} | {value['Kitta']}                                              |  {value['Price(per/month)']}        |"""
                            print(total);
                            total = total + int(value['Price(per/month)'])
                            print(total)
    
    bottom_bill =f"""
                -------------------------------------------------------------------------
                                                                            Total :{total:<13}
                                                                            VAT   : 13 %
                                                                      Grand Total :{(total + (total * 0.13)):<13}"""
                           
                        # break;

               
    bill_format = top_bill+middle_bill+bottom_bill;
    file = open("rentedLand.txt","w")
    file.write(bill_format);
    file.close()
    return bill_format;






# file = open('rentedLand.txt')
# bill = f"""{file.read()}"""
# print(bill);
# file.close()




