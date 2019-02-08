#start with asking how much flour
#then ask how much of the ingredient
# the flour percentage is always going to be 100%

def convert_to_bpercentage(number_of_ingred):
    fl_ounces = float(input("Enter the amount of flour in ounces: "))
    ingred_list = [] 
    
    i = 0
    while i < number_of_ingred:
        ingredient = input("What kind of ingredient are you adding?: ")
        ingred_amount = float(input("Enter the amount of your ingredient: "))
        units = input("Units?: ")
        if "kg" in units:
            #first convert to oz
            ingred_amount = ingred_amount * 35.274
            bk_percentage = 100 *(ingred_amount / fl_ounces)
            ingred_list.append(str(bk_percentage) +"% " + ingredient)
        
        elif "g" in units:
            #first convert to oz
            ingred_amount = ingred_amount * .283
            bk_percentage = 100 *(ingred_amount / fl_ounces)
            ingred_list.append(str(bk_percentage) +"% " + ingredient)

        elif "lb" in units:
            #first convert to oz
            ingred_amount = ingred_amount * 16
            bk_percentage = 100 *(ingred_amount / fl_ounces)
            ingred_list.append(str(bk_percentage) +"% " + ingredient)
       
        elif "oz" in units:
            #first convert to oz
            bk_percentage = 100 *(ingred_amount / fl_ounces)
            ingred_list.append(str(bk_percentage) +"% " + ingredient)   
        
        else:
            print("Enter one of the following units of measurement: kg, g ,lb, oz")
            
        i+=1
    ingred_list.insert(0, "100.0%\ flour")
    return ingred_list


print(convert_to_bpercentage(2))
    

