from fileRead import fileReader 
from fileWrite import *
from datetime import datetime 
from fileWrite import bill_maker 
from fileWrite import counter

 
Final_bill = "" 
rented_Land_Owner_List = []  
returnable_Land_Owner_List = []
user_Phone_Number1 = 0
user_address1 = ""
name_of_land_owner1 = ""

def ask_user():
    print("<<<<<<<Choose the following options>>>>>")  
    print("<----1.Display Details---->\n<----2.Rent Land----> \n<----3.Return Land---->\n<----4.Exit---->")
    user_choice=0 
    while(user_choice != 1 or user_choice !=2 or user_choice != 3 or user_choice !=4):
        user_choice="y"
        while(str(user_choice).strip().isalpha() or str(user_choice).isspace()):
            try:
                user_choice = int(input("Enter your choice>>>> "))
            except:
                user_choice = input("Enter a valid choice>>>")

        if(user_choice == 1 or user_choice == str(1)):
            return "details"
            # break
        elif(user_choice == 2 or user_choice == str(2)):
            return "rent"
            # break
        elif(user_choice == 3 or user_choice == str(3)):
            return "return"
        elif(user_choice == 4 or user_choice == str(4)):
            return "exit"
        else:
            print("* Enter a valid choice *") 





"""It displays the welcoming intro and details of land available with it's different details like kitta and location"""
def display_The_Intro():
    
    print("\n\n\t\t\t\t<-------- Welcome to Techno Property Nepal --------->\n")

    display_Details_Of_File() 
    print("\n \t\t\t\t<--------------------------------------------------->")
    print("\n\t\t\t__________Choose kitta number to buy a Available land________\n")




"""This is method is used to gather the details in rent_details file and displays the information in tabular format"""
def display_Details_Of_File():
    list_Of_Land = fileReader() 
    count =1 
    for value in list_Of_Land:
        
        if count <=1:
            print("""------------------------------------------------------------------------------------------------------------------------------""")
            print("""------------------------------------------------------------------------------------------------------------------------------""")
            count= count +1
            # print("-----------------------------------------------------------------------------------------")
            for k in value.keys():
                
                if(k.strip() == "Availability"):
                     print("|{:^19}".format(k) + "|",end="\n")
                     print("""------------------------------------------------------------------------------------------------------------------------------""")
                else:
                    print("|{:^19}".format(k) + "|",end="" )
            
        
        for v in value.values():
            if (v.strip().lower() == "available" or v.strip().lower() == "not available" or v.strip().lower() == "unavailable"):
                
                print("|{:^19}".format(v) +"|",end="\n")
                

            else:
                
                print("|{:^19}".format(v) +"|",end="")
    print("""------------------------------------------------------------------------------------------------------------------------------""")



"""This is the process after displaying intro to the user which asks kitta from user and do other prcess"""
def after_Intro(count,owner_List):
    file = open('rentedLand.txt','w')
    bill = f"""{file.write("")}"""
    file.close()
    
    userTryAgain = True
    
    while(userTryAgain):
        
        user_picked_kitta_number ='y'
        user_picked_kitta_number = input("Enter the kitta number of available land:------>")
        if(not user_picked_kitta_number.isdigit()):
            user_picked_kitta_number = int(user_input_validator(user_picked_kitta_number))
        else:
            user_picked_kitta_number = int(user_picked_kitta_number)
 

        message,count= land_Purchase(user_picked_kitta_number,count) 
        print(message)
        user_Confirmation_to_exit = input("Do you want to buy again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            counter=0
            bill_printer()
        else:
            display_The_Intro()



"""This method accepts the kitta number input by user and look for the kiita number in file if exists then further process like renting and occurs"""

def land_Purchase(kittaInputFromUser,count):
    """this method takes a input from a user and checks whether the land is available or not \n
    and returns """
    
    kittaInputFromUser = int(kittaInputFromUser)
    print(kittaInputFromUser) 
    details_Of_File_Holder = fileReader()
    user_Picked_Land_Holder= {} 
    
    kitta_num_existing_checker = False
    kitta_num = kittaInputFromUser 
    indexing_for_existed_kitta=0 
    for i in range(len(details_Of_File_Holder)):
    # print(type(value[i]['kitta']))
        if(int(details_Of_File_Holder[i]['Kitta']) == kittaInputFromUser ):
            kitta_num = kittaInputFromUser
            indexing_for_existed_kitta = i 
            kitta_num_existing_checker=True
            break 
            
        
    if(kitta_num_existing_checker):
        user_Picked_Land_Holder = details_Of_File_Holder[indexing_for_existed_kitta]

        print("kitta = "+ user_Picked_Land_Holder['Kitta']+"\nLocation = " + user_Picked_Land_Holder['Location'])
        print("Land Faced = "+ user_Picked_Land_Holder['Direction(land)']+"\nAnna= " + user_Picked_Land_Holder['Anna'])
        print("Availability = "+ user_Picked_Land_Holder['Availability']+"\nPrice = " + user_Picked_Land_Holder['Price(per/month)']+"\n")

        if user_Picked_Land_Holder['Availability'].lower() == "available":
            user_Confirmation = input(f"Are you sure to buy kitta no {kittaInputFromUser} of price {user_Picked_Land_Holder['Price(per/month)']}: (y/n)")

            if(user_Confirmation.lower() == "y" or user_Confirmation.lower() == "yes"):
                # bill_Checker = True 
                # phoneNumber = user_Phone_Number
                # address = user_address
                # name = name_of_land_owner
                # if(count == 1):
                #     name_of_land_owner = input("Enter your name:>>>")
                #     name_of_land_owner1 = name
                #     user_Phone_Number = input("Enter len()=10 your Phone Number: >>")
                    
                #     while(len(user_Phone_Number) <10 or not (user_Phone_Number.isdigit())):
                #         user_Phone_Number = input("Enter a length=10 of  phone NUmber:>>")

                #     user_Phone_Number1 = user_Phone_Number
                #     user_address = input("Enter your address>>> ")
                #     user_address1 = user_address
                # # else:
                # #     # name_Of_land_owner = rented_Land_Owner_List[0]['Name']
                # #     name = name_of_land_owner1
                # #     phoneNumber = user_Phone_Number1
                # #     address = user_address1
                # period_Of_rent = user_input_validator(input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")) 
                
                # if (count == 1):
                #     count = count + 1 
                #     rented_owner_dict = {'Name':'','Duration':period_Of_rent}
                #     rented_owner_dict.update(user_Picked_Land_Holder)
                #     rented_Land_Owner_List.append(rented_owner_dict)
                #     Final_bill=bill_maker(name_of_land_owner,user_address,user_Phone_Number,rented_Land_Owner_List,period_Of_rent)
                # else:
                    
                #     rented_owner_dict = {'Name':name_of_land_owner,'Duration':period_Of_rent}
                #     rented_owner_dict.update(user_Picked_Land_Holder)
                #     rented_Land_Owner_List.append(rented_owner_dict)
                #     Final_bill=bill_maker(name_of_land_owner1,user_address1,user_Phone_Number1,rented_Land_Owner_List,period_Of_rent)
                Final_bill=bill_maker(rented_Land_Owner_List,user_Picked_Land_Holder,from_where='rent',count=count)
                updating_Details_in_rentFile(details_Of_File_Holder,kitta_num,'rent') 
                bill_Checker =False 
                return ("Purchase successfull",count) 
               
            else:
                return "failed",count
        else:
            return f"try again this land is {user_Picked_Land_Holder['Availability']}",count

    else:
        
        print("enter a valid kitta number")
        after_Intro(count,rented_Land_Owner_List)


def return_Land_Process(count,user_picked_returnable_land):

    list_Of_Land = fileReader() 
   
    
    userTryAgain = True
    while(userTryAgain):
        user_Input_Kitta ='y'
        
        user_Input_Kitta = input("Enter your kitta number>>>> ")
        user_Input_Kitta = user_input_validator(user_Input_Kitta)
        result_Of_Checker =kitta_Available_Checker(user_Input_Kitta,list_Of_Land)
        if( result_Of_Checker != "null"):
            if(list_Of_Land[result_Of_Checker]['Availability'] == "Not Available"):
                user_picked_returnable_land = list_Of_Land[result_Of_Checker]

                if(count == 1):
                    user_month = input("Enter for how many months you have rented?>>>")
                    user_month = user_input_validator(user_month)
                    while(int(user_month)<1 or int(user_month)>12):
                        user_month = input("Enter a valid months you have rented?>>>")
                    
                    current_month = input("Enter the running month>>>>")
                    user_input_validator(current_month)
                    while(int(current_month)<1 or int(current_month)>12 or current_month.isalpha()):
                        current_month = input("Enter the running month>>>>")
                    user_input_validator(current_month)
                    if(int(current_month) > int(user_month)):
                        exceded_Month = int(current_month) - int(user_month)
                        penalty_Price = int(exceded_Month) * 20000
                        print("<---------------------      you have exceded the time limit        ------------->")
                        print("<----------------------     penalty will added to your bill         ------------>")
                        print( f"""<-----------------          {exceded_Month} month-> {penalty_Price}               ------------->""")
                        
                        bill_maker(returnable_Land_Owner_List,user_picked_returnable_land,count,month=current_month,price=penalty_Price,from_where='return')
                    else:
                        bill_maker(returnable_Land_Owner_List,user_picked_returnable_land,count,month=current_month,from_where='return')
                    
                else:
                  bill_maker(returnable_Land_Owner_List,user_picked_returnable_land,count,from_where="return")     
                    
                updating_Details_in_rentFile(list_Of_Land,user_Input_Kitta,"return")
                
                return "Return sucessfull",count
                
                
            else:
                print("The land of kitta number"+str(user_Input_Kitta+"is available on sale"))
                continue
        else:
            print("Kitta Number Doesn't Exist")
            continue  
def land_return_starter(count,owner_List):
    userTryAgain = True
    file = open('rentedLand.txt','w')
    bill = f"""{file.write("")}"""
    file.close()
    while(userTryAgain):
        message,count= return_Land_Process(count,owner_List)
        print(message)
        user_Confirmation_to_exit = input("Do you want to return the land again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            counter =0
            bill_printer()
        else:
            display_The_Intro()


def month_validator(month):
    is_month_true = False
    while(month < 1 ):
        month = input("Enter a valid months you have rented?>>> ")
        is_month_true = True
    if(is_month_true):
        return month

    
    
def bill_printer():
    file = open('rentedLand.txt')
    bill = f"""{file.read()}"""
    print(bill) 
    file.close()    
    




def kitta_Available_Checker(kitta_num,list_value):
    """This method take int and a list as a parameter \n and returns int value if int value exists in list else null \nparameter:int , list
    returns:True or null"""
    is_Kitta_available = False
    index_Capturer = 0
    for i in range(len(list_value)):
        if(list_value[i]['Kitta'] == str(kitta_num) or list_value[i]['Kitta'] == kitta_num):
                index_Capturer = i
                is_Kitta_available = True
                break
    if(is_Kitta_available):            
        return index_Capturer
    else:
        return "null"
    

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

  
        
