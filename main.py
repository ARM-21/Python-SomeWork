from operations import *
from fileWrite import counter
count =1
counter_for_return_land = 1;       
bill_Checker = False 
list_Of_user_returnable_land =[]

user_Phone_Number = 0
user_address = ""
name_of_land_owner = ""

user_Desire=True 
print("""

┏━━━━┓╋╋╋╋┏┓╋╋╋╋╋┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋┏━┓╋┏┓╋╋╋╋╋╋╋╋┏┓
┃┏┓┏┓┃╋╋╋╋┃┃╋╋╋╋╋┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋┃┃┗┓┃┃╋╋╋╋╋╋╋╋┃┃
┗┛┃┃┣┻━┳━━┫┗━┳━━┓┃┗━┛┣━┳━━┳━━┳━━┳┻┓┏╋┓╋┏┓┃┏┓┗┛┣━━┳━━┳━━┫┃
╋╋┃┃┃┃━┫┏━┫┏┓┃┏┓┃┃┏━━┫┏┫┏┓┃┏┓┃┃━┫┏┫┃┃┃╋┃┃┃┃┗┓┃┃┃━┫┏┓┃┏┓┃┃
╋╋┃┃┃┃━┫┗━┫┃┃┃┗┛┃┃┃╋╋┃┃┃┗┛┃┗┛┃┃━┫┃┃┗┫┗━┛┃┃┃╋┃┃┃┃━┫┗┛┃┏┓┃┗┓
╋╋┗┛┗━━┻━━┻┛┗┻━━┛┗┛╋╋┗┛┗━━┫┏━┻━━┻┛┗━┻━┓┏┛┗┛╋┗━┻━━┫┏━┻┛┗┻━┛
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋╋╋┏━┛┃╋╋╋╋╋╋╋╋╋┃┃
╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛╋╋╋╋╋╋╋╋┗━━┛╋╋╋╋╋╋╋╋╋┗┛

""")
while(user_Desire):
    
    user_Desire = ask_user()
            
    if(user_Desire == "details"):
        display_The_Intro()
    elif(user_Desire == "rent"):
         counter= 0
         rented_Land_Owner_List = ""
         display_The_Intro()
         after_Intro(count,rented_Land_Owner_List) 
    elif(user_Desire == "return"):

        list_Of_user_returnable_land =""
        display_The_Intro()
        land_return_starter(count,list_Of_user_returnable_land)
    else:
        user_Desire = False  


