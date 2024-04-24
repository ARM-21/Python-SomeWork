from operations import *
                        
count =1
counter_for_return_land = 1;       
bill_Checker = False 
list_Of_user_returnable_land =[]
    

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
        land_return_starter(count,list_Of_user_returnable_land)
    else:
        user_Desire = False 


