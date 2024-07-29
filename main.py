'''
Main program // Risk-Assist
A command line interface containing tools useful in the mortgage lending process
'''

from time import sleep
from fema_disasters_api import CheckFema
from census_api import get_ami
from apor import get_apor
from program_info import ProgramInfo

def main():
    '''
    Main Command Line Interface for program.
    '''
    # begin command line interface
    while True:
        # main menu selection
        print("\n \n-=-=-=-=-=Risk-Assist=-=-=-=-=-\n")
        print("Welcome to the Risk-Assist program! Please select from the following choices below:\n")
        print("1. Property Evaluator (Assist you in evaluating the risk factors and opportunities for your subject property)")
        print("2. Instant APOR (Retrieve instant APOR comparison against your locked APR)")
        print("3. More Info...")
        print("4. Exit \n")
        
        # prompt user for choice
        selection = input("Please select an option 1-4:")

        
        # navigate user to respective screen depending on selection
        if selection == '1':
            PropertyEvaluator()
        
        if selection == '2':
            InstantAPOR()
        
        if selection == '3':
            ProgramInfo()
   
            
        if selection == '4':
            quit_choice = input("Are you sure you want to exit? (You will lose all information retreived) (yes/no)")
            if quit_choice != "no":
                print("Program exiting...")
                sleep(1)
                print("Goodbye!")
                quit()
        
        else:
            print("\n ERROR: Selection must be in the form of a number 1-4 only")
        
  

    

def InstantAPOR():
    '''
    Instant APOR Menu. Utilizes CFPB API to compare loan Annual Percentage Rate against Average Prime Offer Rate. Useful in determining
    lender compliance to lending laws.
    '''
    while True:
        # main menu for Instant APOR
        print("\n\n\n-=-=-=-=-= Risk-Assist \\\ Instant APOR =-=-=-=-=-\n\n")
        sleep(1)
        print("Instant APOR\n")
        print("Please provide the following details:\n")
        
        # collect details for calculation from user
        loanTerm = int(input("Loan Term (in years): "))
        if loanTerm > 50 or loanTerm < 1:
            print("Loan Term must be less than or equal to 50 years")
            continue
        apr = input("Loan APR: ")
        lockDate = input("Date rate was locked: ")
           
        sleep(1)
        rateSpread = get_apor(loanTerm, apr, lockDate)
        apor = float(apr)-rateSpread
        print("\nHere are the APOR details of your transaction:\n")
        print(f"APR: {apr}")
        print(f"APOR: {apor}")
        print(f"Rate Spread: {rateSpread}\n")
        sleep(3)
        checkContinue = input("Do you want to check another rate? (yes/no) \n")
        if checkContinue != "yes":
            break


def PropertyEvaluator():
    '''
    Property Evaluator Menu. Utilizes APIs to check Area Median Income and FEMA Disaster status of a given
    property location.
    '''
    while True:
        # main menu for Property Evaluator
        
        print("\n\n\n-=-=-=-=-= Risk-Assist \\\ Property Evaluator =-=-=-=-=-\n\n")
        sleep(1)
        print("Property Evaluator\n")
        property_address = input("Please enter your property address in the format:\n [street address], [city], [state abbr] [zip code]:\n")
        sleep(1)
        try:
            valid_property, zipCode, state = CheckProperty(property_address)
            if valid_property is True:
                print(f"\n\nSubject Property: {property_address}\n")
                print("What service would you like to use for this address?\n")
                print("1. Area Median Income")
                print("2. FEMA Disaster")
                print("3. Go Back")
                print("4. Exit \n")
        except Exception as error:
            print(f"Error: {error}. Please enter a valid property address in the format [street address], [city], [state abbr] [zip code].")
            continue  # Goes back to the start of the while loop
            
        # prompt user for choice
        selection = input("Please select an option 1-4 or enter 'help' if you are feeling lost:")
        
        # navigate user to service screen
        if selection == "1":
            sleep(1)
            AreaMedianIncome(zipCode)
            
        if selection == "2":
            sleep(1)
            FemaDisasters(state)
            
        if selection == "3":
            sleep(1)
            break
            
        if selection == "4":
            print("Program exiting...")
            sleep(1)
            print("Goodbye!")
            quit()
            
        if selection == "help":
            print("Area Median Income: Returns the average median income for househoulds in the area surrounding your subject property\n")
            print("FEMA Disaster: Returns the five most recent disasters that have occurred in the area surrounding your subject property\n")
            print("Go back: Returns you to the main menu")
            print("Exit: Quits the program")
            
            
        # check if user wants to check another address
        checkContinue = input("Do you want to check another property? (yes/no)")
        if checkContinue != "yes":
            break    
            
def AreaMedianIncome(zipCode):
    '''
    Returns AreaMedianIncome of an area via Census Bureau API or Microservice
    '''
    print("\n\n\n-=-=-=-=-= Risk-Assist \\\ Property Evaluator \\\ AreaMedianIncome=-=-=-=-=-\n\n")
    sleep(1)
    print("According to the Census Bureau:\n")
    
    # check AMI
    ami = get_ami(zipCode)
    print(f"The Area median income in {zipCode} is: ${ami} / year  \n")
    sleep(4)
    print("Returning to previous screen. \n")
    sleep(3)
    
    
def FemaDisasters(state):
    '''
    Returns any past and ongoing FEMA-declared disasters of an area via openFEMA API or Microservice
    '''
    print("\n\n\n-=-=-=-=-= Risk-Assist \\\ Property Evaluator \\\ FEMA Disasters=-=-=-=-=-\n\n")
    sleep(1)

    
    
    # Check Properties
    disasters = CheckFema(state)
    sleep(1)
    disaster_count = 1
    print(f"We found the following FEMA-declared disasters in the area:\n")
    sleep(1)
    for disaster in disasters: 
        print(f"\n{disaster_count}. Disaster Number: {disaster['disasterNumber']}\n Disaster Title: {disaster['declarationTitle']}\n Start Date: {disaster['incidentBeginDate'].split('T')[0]}\n End Date: {disaster['incidentEndDate'].split('T')[0]}\n Declaration Date: {disaster['declarationDate'].split('T')[0]}")
        disaster_count += 1
    sleep(5)
    print("\n\n\n Returning to previous screen. \n")


def CheckProperty(address):
    '''
    Checks Validity of a property address (potential for microservice)
    '''           
    address = address.split(',')
    
    street = address[0]
    city = address[1].strip(" ")
    state = address[2].split()[0]
    zip = address[2].split()[1]
    while True:
 
        
        print(" ")
        
        print("\nAddress Entered:")
        print(f"Street: {street}")
        print(f"City: {city}")
        print(f"State: {state}")
        print(f"Zip Code: {zip}\n")
        if len(zip) == 5:
            return True, zip, state
        else:
            print("Why isn't your zip code at least 5 digits?\n")
            
 
 
    
if __name__ == "__main__":
    main()
    # CheckProperty("25320 Via paci,vlaencia, ca 91355")
