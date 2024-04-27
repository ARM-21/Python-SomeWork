from fileRead import fileReader 
from fileWrite import * 
from fileWrite import bill_maker
# from fileWrite import counter 



 
Final_bill = "" 
rented_Land_Owner_List = []  
returnable_Land_Owner_List = []
user_Phone_Number1 = 0
user_address1 = ""
name_of_land_owner1 = ""

counter_for_entry = 0

def ask_user():
    global counter
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
            counter=0
            return "rent"
            # break
        elif(user_choice == 3 or user_choice == str(3)):
            counter=0
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
def after_Intro(count,rented_list_by_user):
    file = open('rentedLand.txt','w')
    bill = f"""{file.write("")}"""
    file.close()
    
    userTryAgain = True
    
    while(userTryAgain):
        message = ""
        user_picked_kitta_number ='y'
        user_picked_kitta_number = input("Enter the kitta number of available land:------>")
        if(not user_picked_kitta_number.isdigit()):
            user_picked_kitta_number = int(user_input_validator(user_picked_kitta_number))
        else:
            user_picked_kitta_number = int(user_picked_kitta_number)
 
        try:
            message,count,rented_list_by_user= land_Purchase(user_picked_kitta_number,rented_list_by_user,count)
            print(message) 
        except:
            print(message)
        user_Confirmation_to_exit = input("Do you want to buy again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            rented_list_by_user = []
            count =0
            bill_printer()
            return rented_list_by_user
        else:
            display_The_Intro()
            # return rented_list_by_user


"""This method accepts the kitta number input by user and look for the kiita number in file if exists then further process like renting and occurs"""

def land_Purchase(kittaInputFromUser,rented_list_by_user,count):
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
   
        if(int(details_Of_File_Holder[i]['Kitta']) == kittaInputFromUser ):
            kitta_num = kittaInputFromUser
            indexing_for_existed_kitta = i 
            kitta_num_existing_checker=True
            
            
        
    if(kitta_num_existing_checker):
        user_Picked_Land_Holder = details_Of_File_Holder[indexing_for_existed_kitta]

        print("kitta = "+ user_Picked_Land_Holder['Kitta']+"\nLocation = " + user_Picked_Land_Holder['Location'])
        print("Land Faced = "+ user_Picked_Land_Holder['Direction(land)']+"\nAnna= " + user_Picked_Land_Holder['Anna'])
        print("Availability = "+ user_Picked_Land_Holder['Availability']+"\nPrice = " + user_Picked_Land_Holder['Price(per/month)']+"\n")

        if user_Picked_Land_Holder['Availability'].lower() == "available":
            user_Confirmation = input(f"Are you sure to buy kitta no {kittaInputFromUser} of price {user_Picked_Land_Holder['Price(per/month)']}: (y/n)")

            if(user_Confirmation.lower() == "y" or user_Confirmation.lower() == "yes"):
               
                count,rented_list_by_user=bill_maker(rented_list_by_user,user_Picked_Land_Holder,from_where='rent',count=count)
                updating_Details_in_rentFile(details_Of_File_Holder,kitta_num,'rent') 
             
                return ("Purchase successfull",count,rented_list_by_user) 
               
            else:
                return "failed",count,rented_list_by_user
        else:
            return f"try again this land is {user_Picked_Land_Holder['Availability']}",count,rented_list_by_user

    else:
        
        print("enter a valid kitta number")
        after_Intro(count,rented_list_by_user)
        return "failed",count,rented_list_by_user


def return_Land_Process(user_input_kitta,count,user_picked_returnable_land):

    list_Of_Land = fileReader() 
   
    
    userTryAgain = True
    while(userTryAgain):
        
        result_Of_Checker =kitta_Available_Checker(user_input_kitta,list_Of_Land)
        if( result_Of_Checker != "null"):
            if(list_Of_Land[result_Of_Checker]['Availability'] == "Not Available"):
                current_picked_land = list_Of_Land[result_Of_Checker]
        
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
                    
                    count,user_picked_returnable_land=return_bill_maker(current_picked_land,user_picked_returnable_land,count=count,month=current_month,price=penalty_Price)
                else:
                  count,user_picked_returnable_land = return_bill_maker(current_picked_land,user_picked_returnable_land,count=count,month=current_month)
                      
                    
                updating_Details_in_rentFile(list_Of_Land,user_input_kitta,"return")
                
                return "Return sucessfull",count,user_picked_returnable_land
                
                
            else:
                print("The land of kitta number"+str(user_input_kitta+"is available on sale"))
                return "failed",count,user_picked_returnable_land
        else:
            print("Kitta Number Doesn't Exist")
            return "failed",count,user_picked_returnable_land 
        

def land_return_starter(count,user_picked_returnable_land):
    
    userTryAgain = True
    file = open('rentedLand.txt','w')
    bill = f"""{file.write("")}"""
    file.close()
    while(userTryAgain):
        message = ""
        kitta_from_user = "y"
        kitta_from_user = input("Enter the kitta number of available land----->")
        if(not kitta_from_user.isdigit()):
            kitta_from_user = int(user_input_validator(kitta_from_user))

        try:
            message,count,user_picked_returnable_land= return_Land_Process(kitta_from_user,count,user_picked_returnable_land)
            print(message)
        except:
            print(message)
        user_Confirmation_to_exit = input("Do you want to return the land again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
            # count =0
            # user_picked_returnable_land=[]
            bill_printer()
            return user_picked_returnable_land
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

  
        
