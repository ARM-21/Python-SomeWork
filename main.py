from FileRead import fileReader;
from FileWrite import updating_Details_in_rentFile;
from datetime import datetime;

def displayDetailsOfFile():
    list_Of_Land = fileReader();
    count =1;
    for value in list_Of_Land:
        # print(value);
        # valuesFor = value.Keys()
        # print(value.values());
       
        if count <=1:
            count= count +1
            for k in value.keys():
                if(k.strip() == "Availability"):
                     print("{:19s}".format(k) + "|",end="\n")
                else:
                    print("{:19s}".format(k) + "|",end="" )
            # print(end="\n")
        
        for v in value.values():
            if (v.strip().lower() == "available" or v.strip().lower() == "not available" or v.strip().lower() == "unavailable"):
                
                print("{:19s}".format(v) +"|",end="\n")
                print(sep="~")

            else:
                
                print("{:19s}".format(v) +"|",end="")






   
def landPurchase(kittaInputFromUser,count,rented_Land_Owner_list):
    """this method takes a input from a user and checks whether the land is available or not \n
    and returns """
    print(kittaInputFromUser);
    details_Of_File_Holder = fileReader()
    user_Picked_Land_Holder= {};
    
    kitta_num_existing_checker = False
    kitta_num = kittaInputFromUser;
    indexing_for_existed_kitta=0;
    for i in range(len(details_Of_File_Holder)):
    # print(type(value[i]['kitta']))
        if(int(details_Of_File_Holder[i]['Kitta']) == kittaInputFromUser ):
            kitta_num = kittaInputFromUser
            indexing_for_existed_kitta = i;
            kitta_num_existing_checker=True
            break;
            
        
    if(kitta_num_existing_checker):
        user_Picked_Land_Holder = details_Of_File_Holder[indexing_for_existed_kitta]
        print("kitta = "+ user_Picked_Land_Holder['Kitta']+"\nLocation = " + user_Picked_Land_Holder['Location'])
        print("Land Faced = "+ user_Picked_Land_Holder['Direction(land)']+"\nAnna= " + user_Picked_Land_Holder['Anna'])
        print("Availability = "+ user_Picked_Land_Holder['Availability']+"\nPrice = " + user_Picked_Land_Holder['Price(per/month)']+"\n")

        if user_Picked_Land_Holder['Availability'].lower() == "available":
            user_Confirmation = input(f"Are you sure to buy kitta no {kittaInputFromUser} of price {user_Picked_Land_Holder['Price(per/month)']}: (y/n)")

            if(user_Confirmation.lower() == "y" or user_Confirmation.lower() == "yes"):
                
                name_Of_land_owner = input("Enter your name:>")
                period_Of_rent = int(input("For How months do you want to rent(warning:-greater than one month or equal to one month)? > "));
                if (count == 1):
                    count = count + 1;
                    rented_owner_dict = {'Name':'','Duration':period_Of_rent}
                    rented_owner_dict.update(user_Picked_Land_Holder)
                    rented_Land_Owner_List.append(rented_owner_dict)
                    # print(rented_Land_Owner_List)
                else:
                    # count = count+1;
                    rented_owner_dict = {'Name':name_Of_land_owner,'Duration':period_Of_rent}
                    rented_owner_dict.update(user_Picked_Land_Holder)
                    rented_Land_Owner_List.append(rented_owner_dict)
                    

                print(rented_Land_Owner_List);
                print(count);
                invoice = open('rentedLand.txt','w')
                for value in rented_Land_Owner_List:
                    
                    # print(value)
                    if(value['Name'] == name_Of_land_owner):
                        
                        invoice.write("Name,kitta,Location,Land Faced,Price,Duration,Date,Time\n")
                        # invoice.write(f"{name_Of_land_owner},{user_Picked_Land_Holder['Kitta']},{user_Picked_Land_Holder['Location']},{user_Picked_Land_Holder['Direction(land)']},{user_Picked_Land_Holder['Price(per/month)']},{period_Of_rent},{str(datetime.now().time())},{str(datetime.now().time())}\n")
                        invoice.write(f"{name_Of_land_owner},{value['Kitta']},{value['Location']},{value['Direction(land)']},{value['Price(per/month)']},{period_Of_rent},{str(datetime.now().date())},{str(datetime.now().time())}\n")

                    else:
                        value['Name']= name_Of_land_owner;
                        invoice.write("Name,kitta,Location,Land Faced,Price,Duration,Date,Time\n")
                        invoice.write(f"{name_Of_land_owner},{user_Picked_Land_Holder['Kitta']},{user_Picked_Land_Holder['Location']},{user_Picked_Land_Holder['Direction(land)']},{user_Picked_Land_Holder['Price(per/month)']},{period_Of_rent},{str(datetime.now().date())},{str(datetime.now().time())}")

                invoice.close()
                
                updating_Details_in_rentFile(details_Of_File_Holder,kitta_num);
                # count = count +1;
                return ("Purchase successfull",count);
            else:
                return "failed",1
        else:
            return f"try again this land is {user_Picked_Land_Holder['Availability']}",1

    else:
        
        print("enter a valid kitta number")
        after_Intro(count,rented_Land_Owner_List)



def displayTheIntro():
    # count =1
    print("\n\n\t\t\t\t<-------- Welcome to Techno Property Nepal --------->\n")
    displayDetailsOfFile();
    print("\n \t\t\t\t<--------------------------------------------------->")
    print("\n\t\t\t__________Choose kitta number to buy a Available land________\n")
    
    
    


def after_Intro(count,owner_List):
    
    userTryAgain = True
    
    while(userTryAgain):
        
        user_picked_kitta_number ='y';
    # if(user_picked_kitta_number.isalpha()):
        # while(user_picked_kitta_number.isalpha()):
        try:
            user_picked_kitta_number = input("Enter the kitta number of available land:--->")
        except:
            user_picked_kitta_number = input("Enter a valid kitta number: >")
    # else:
        # user_picked_kitta_number = int(input("Enter the kitta number of available land:--->"))

        message,count= landPurchase(int(user_picked_kitta_number),count,owner_List);
        print(message)
        # count = count +1;
        print(count);
        user_Confirmation_to_exit = input("Do you want to buy again: (y/n) >")
        if (user_Confirmation_to_exit.lower() == "n" or user_Confirmation_to_exit.lower() == "no"):
            userTryAgain = False
        else:
            displayTheIntro()



count =1;      
rented_Land_Owner_List = [];     
           

displayTheIntro();
after_Intro(count,rented_Land_Owner_List);

