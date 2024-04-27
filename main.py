from fileWrite import *
from operations import *
from operations import ask_user




count =1
       
bill_Checker = False 
# list_Of_user_returnable_land =[]
counter_for_return_land = 0
counter_for_rent_land = 0
rented_list_by_user =[]
list_Of_user_returnable_land=[]
# rented_Land_Owner_List = {}
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
         
         display_The_Intro()
         rented_list_by_user = after_Intro(counter_for_rent_land,rented_list_by_user)
         rented_list_by_user = []
         counter_for_rent_land = 0
         
    elif(user_Desire == "return"):
       
        
        display_The_Intro()
        list_Of_user_returnable_land=land_return_starter(counter_for_return_land,list_Of_user_returnable_land)
        list_Of_user_returnable_land = []
        counter_for_return_land = 0
        
    else:
        user_Desire = False  


