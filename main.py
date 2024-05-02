from fileWrite import *  # Imports all functions from the fileWrite module
from operations import *  # Imports all functions from the operations module
from operations import ask_user  # Imports the ask_user function from operations


# Initializing counters and empty lists for tracking rentals and returnable land
counter_for_return_land = 0
counter_for_rent_land = 0
rented_list_by_user = []
list_Of_user_returnable_land = []

# Prints a decorative banner of Techno property nepal

print(f"""

___________           .__                    __________                                     __            _______                      .__   
\__    ___/___   ____ |  |__   ____   ____   \______   \_______  ____ ______   ____________/  |_ ___.__.  \      \   ____ ___________  |  |  
  |    |_/ __ \_/ ___\|  |  \ /    \ /  _ \   |     ___/\_  __ \/  _ \\____ \_/ __ \_  __ \   __<   |  |  /   |   \_/ __ \\____ \__  \ |  |  
  |    |\  ___/\  \___|   Y  \   |  (  <_> )  |    |     |  | \(  <_> )  |_> >  ___/|  | \/|  |  \___  | /    |    \  ___/|  |_> > __ \|  |__
  |____| \___  >\___  >___|  /___|  /\____/   |____|     |__|   \____/|   __/ \___  >__|   |__|  / ____| \____|__  /\___  >   __(____  /____/
             \/     \/     \/     \/                                  |__|        \/             \/              \/     \/|__|       \/      
     
                                                    
                                                    """)


user_Desire = True  # Bool Varible to control the main loop

# This loop keeps running until the user chooses to exit
while (user_Desire):
    # Get user's choice using the ask_user function
    user_Desire = ask_user()

    # Displays introductory information of Organization and available land of different places with different information like anna,location) if user chooses "details"
    if (user_Desire == "details"):
        display_The_Intro()  # This function displays introductory content

    # Handles renting land if user chooses "rent"
    elif (user_Desire == "rent"):
        display_The_Intro()  # Display introductory content 
        rented_list_by_user = after_Intro(counter_for_rent_land, rented_list_by_user)  # Function helps to calculate renting which returns a list of land choosen by user 
        rented_list_by_user = []  # Reset rental list to enmty to process new rent details
        counter_for_rent_land = 0  # Reset rental counter to zero to process start for new process

    # Handles returning land if user chooses "return"
    elif (user_Desire == "return"):
        # Display introductory content
        display_The_Intro()  
        # Function  processes land returning by user and returns a list of land chosen by user
        list_Of_user_returnable_land = land_return_starter(counter_for_return_land, list_Of_user_returnable_land) 
        list_Of_user_returnable_land = []  # Reset return list to start new process
        counter_for_return_land = 0   # Reset return counterto start new process

    # Exit the loop if user enters anything else
    else:
        user_Desire = False  # Set user_desire to False to exit the loop
        print(f"""
 _____ _                  _                            __             __     ___     _   _               __  
 |_   _| |__   __ _ _ __ | | __   _   _  ___  _   _   / _| ___  _ __  \ \   / (_)___| |_(_)_ __   __ _   \ \ 
   | | | '_ \ / _` | '_ \| |/ /  | | | |/ _ \| | | | | |_ / _ \| '__|  \ \ / /| / __| __| | '_ \ / _` | (_) |
   | | | | | | (_| | | | |   <   | |_| | (_) | |_| | |  _| (_) | |      \ V / | \__ \ |_| | | | | (_| |  _| |
   |_| |_| |_|\__,_|_| |_|_|\_\   \__, |\___/ \__,_| |_|  \___/|_|       \_/  |_|___/\__|_|_| |_|\__, | (_) |
                                  |___/                                                          |___/   /_/ 
""")



