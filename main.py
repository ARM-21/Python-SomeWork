from FileRead import fileReader 
from FileWrite import updating_Details_in_rentFile 
from datetime import datetime 
from FileWrite import bill_maker 
from threading import Timer 
Final_bill = "" 

"""This is method is used to gather the details in rent_details file and displays the information in tabular format"""
def displayDetailsOfFile():
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




"""This method accepts the kitta number input by user and look for the kiita number in file if exists then further process like renting and occurs"""
   
def landPurchase(kittaInputFromUser,count):
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
                bill_Checker = True 
                
                name_Of_land_owner = input("Enter your name:>")
                phoneNumber = input("Enter your Phone Number: >>")

                while(len(phoneNumber) <10 or not (phoneNumber.isdigit())):
                    phoneNumber = input("Enter a valid phone NUmber:>>")

                period_Of_rent = int(input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > ")) 
                if (count == 1):
                    count = count + 1 
                    rented_owner_dict = {'Name':'','Duration':period_Of_rent}
                    rented_owner_dict.update(user_Picked_Land_Holder)
                    rented_Land_Owner_List.append(rented_owner_dict)
                    # print(rented_Land_Owner_List)
                else:
                    # count = count+1 
                    
                    rented_owner_dict = {'Name':name_Of_land_owner,'Duration':period_Of_rent}
                    rented_owner_dict.update(user_Picked_Land_Holder)
                    rented_Land_Owner_List.append(rented_owner_dict)
                Final_bill=bill_maker(name_Of_land_owner,"jhalun",phoneNumber,rented_Land_Owner_List)
                updating_Details_in_rentFile(details_Of_File_Holder,kitta_num) 
                bill_Checker =False 
                return ("Purchase successfull",count) 
               
            else:
                return "failed",1
        else:
            return f"try again this land is {user_Picked_Land_Holder['Availability']}",1

    else:
        
        print("enter a valid kitta number")
        after_Intro(count,rented_Land_Owner_List)



def ask_user():
    print("<<<<<<<Choose the following options>>>>>")  
    print("\t1.Display Details\n\t2.Rent Land \n\t3.Return Land \n\t4.Exit")
    user_choice=0 
    while(user_choice != 1 or user_choice !=2):
        user_choice="y"
        while(str(user_choice).strip().isalpha() or str(user_choice).isspace()):
            try:
                user_choice = int(input("Enter your choice>>>> "))
            except:
                user_choice = input("Enter a valid choice>>>")

        if(user_choice == 1 or user_choice == str(1)):
            return "details"
            break
        elif(user_choice == 2 or user_choice == str(2)):
            return "rent"
            break
        elif(user_choice == 3 or user_choice == str(3)):
            return "return"
        elif(user_choice == 4 or user_choice == str(4)):
            return "exit"
        else:
            print("* Enter a valid choice *") 



"""It displays the welcoming intro and details of land available with it's different details like kitta and location"""
def displayTheIntro():
    
    print("\n\n\t\t\t\t<-------- Welcome to Techno Property Nepal --------->\n")

    displayDetailsOfFile() 
    print("\n \t\t\t\t<--------------------------------------------------->")
    print("\n\t\t\t__________Choose kitta number to buy a Available land________\n")
    
    
def bill_printer():
    file = open('rentedLand.txt')
    bill = f"""{file.read()}"""
    print(bill) 
    file.close()    
    

"""This is the process after displaying intro to the user which asks kitta from user and do other prcess"""
def after_Intro(count,owner_List):
    file = open('rentedLand.txt','w')
    bill = f"""{file.write("")}"""
    file.close()
    
    userTryAgain = True
    
    while(userTryAgain):
        
        user_picked_kitta_number ='y'
   
        try:
            user_picked_kitta_number = int(input("Enter the kitta number of available land:---> "))
        except:
            while(True):
                if(user_picked_kitta_number.strip().isalpha() or len(str(user_picked_kitta_number).strip()) <3 or user_picked_kitta_number.isspace()):
                    user_picked_kitta_number = input("Enter a valid kitta number: > ")
                else:
                    break    

        message,count= landPurchase(user_picked_kitta_number,count) 
        print(message)
        user_Confirmation_to_exit = input("Do you want to buy again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
           userTryAgain = False
        #    print(f"{"hello":10s} Printing your bill!! please wait be patience")
           bill_printer()
        #    delayed_Message = Timer(2,bill_printer)
        #    delayed_Message.start()
        else:
            displayTheIntro()


def kitta_Available_Checker(kitta_num,list_value):
    """This method take int and a list as a parameter \n and returns int value if int value exists in list else null \nparameter:int , list
    returns:True or null"""
    print(list_value);
    is_Kitta_available = False
    index_Capturer = 0
    for i in range(len(list_value)):
        print(i)
        print(list_value[i]['Kitta'])
        print(list_value[i]['Kitta'] == str(kitta_num))
        if(list_value[i]['Kitta'] == str(kitta_num)):
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
            user_input = int(input("Enter a valid input>>>"))
        except:
            print("<---------Enter a valid input------>")
            continue
        if(str(user_input).isdigit()):
            return True
    

def returnLandProcess():
    
    # displayTheIntro()
    list_Of_Land = fileReader() 
   
    
    userTryAgain = True
    while(userTryAgain):
        user_Input_Kitta ='y'
        try:
            user_Input_Kitta = int(input("Enter your kitta number>>>> "))
        except:
            print("\nEnter a  valid kitta number\n")
            continue;
        print(user_Input_Kitta)
        if(kitta_Available_Checker(user_Input_Kitta,list_Of_Land) != "null"):
            user_month = input("Enter for how many months you have rented?>>>")
            user_input_validator(user_month)
            current_month = input("Enter the curent month>>>>")
            user_input_validator(current_month)
            if(current_month > user_month):
                pass
        else:
            print("Kitta Number Doesn't Exist")
            continue    
        
                        
         
                    
    
       
                        

count =1       
bill_Checker = False 
rented_Land_Owner_List = []      

user_Desire=True 
while(user_Desire):
    
    user_Desire = ask_user()
            
    if(user_Desire == "details"):
        displayTheIntro()
    elif(user_Desire == "rent"):
         displayTheIntro()
         after_Intro(count,rented_Land_Owner_List) 
    elif(user_Desire == "return"):
        displayTheIntro()
        returnLandProcess()
    else:
        user_Desire = False 


