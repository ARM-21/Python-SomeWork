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