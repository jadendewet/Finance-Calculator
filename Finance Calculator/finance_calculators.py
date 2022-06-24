#Imports the math module
import math 

#Displays the following statemnets for the user to see.
print("Choose either 'Investment or 'Bond' from the menu below to proceed: ")

print("")       #Used for easeier reading - providing space between statements 

 #Displays possible options and gives the user an explaination of each one
print("Investment \t - to calculate the amount of intrest you'll earn on the investment ")
print("Bond       \t - to calculate the amount you'll have to pay on a home loan ")

print("")       #Used for easeier reading - providing space between statements 

#Recieves input from user 
choice = input("Which option would you like to select?: ")

#Creates conditional statement based off the input from variable choice 
if (choice.lower() == "investment"):

    #Recieves data from user and converts it into float data type 
    money_depositing = float(input(" How much money would you like to deposit?: "))

    #Receieves data from user and converts to int data type 
    intrest_rate = (float(input(" What is the current intrest rate?: "))) / 100
    year_period = int(input(" How many years do you plan on investing for?: "))

    print("")   	  #Used for easeier reading - providing space between statements 

    #Receives input from the user
    intrest_choice = input("Would you prefer the calculation to be based on simple or compound interest?: ")

    print("")   	  #Used for easeier reading - providing space between statements 


    #Creates conditional statement based off the input from variable choice 
    if (intrest_choice.lower() == "simple"):

        #Creates the calculation of simple intrest 
        simple_intrest_calculation = money_depositing * ( 1 + intrest_rate * year_period)
            
         #Displays message and provides the user with their total amount after x amount of years and thier intrest rate 
        print(f"Your new total with an investment of R{money_depositing} and an intrest rate of {intrest_rate} , simple intrest would be : R{simple_intrest_calculation}")


    #Else if the user selects compound:
    #Using the lower function enables any variation of the word would be accepted, this includes some or all capital letters as well
    elif(intrest_choice.lower() == "compound"):

            #Creates the calculation of compound intrest 
            compound_intrest_calculation = round(money_depositing * math.pow((1 + intrest_rate) , year_period),2)

            print(f"Your total with an initial investment of R{money_depositing} and an intrest rate of {intrest_rate}, compounded is R{compound_intrest_calculation}")
            print("")   	  #Used for easeier reading - providing space between statements 
   

#else if the user enters "bond" the following will statements will execute 
#Using the lower function enables any variation of the word would be accepted, this includes some or all capital letters as well
elif(choice.lower() == "bond"):     

    #Receives input from the user 
    present_value = float(input("Enter the current value of the property: "))
    intrest_rate = (float(input("Enter the current intrest rate: "))) / 100       #The value is divided to produce the value in a decimal format 
    duration_months = int(input("Enter the amount of months you plan on repaying the bond for: "))

    bond_monthly_repayment  = round((intrest_rate * present_value)/(1-(1 + intrest_rate)**(-duration_months)),2)

    #Prints out what the user's monthly repayment will be based on their input 
    print(f"Your monthly bond repayments for a property value of R{present_value} , is R{bond_monthly_repayment} per month")

    print("")   #Used for easeier reading - providing space between statements 






