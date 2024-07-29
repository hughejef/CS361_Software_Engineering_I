'''
Program Info
'''




def ProgramInfo():
    '''
    Information about the program if user needs additional information.
    '''
    print("\n\n\n-=-=-=-=-= Risk-Assist \\\ Program Information =-=-=-=-=-\n\n\n")
    print("\n\n\n-=-=-=-=-= Property Evaluator=-=-=-=-=-\n\n")
    print("Your time is valuable so use our Property Evaluator to quickly and easily assess the risk level of a property BEFORE you lend on it by utilizing the following tools:\n\n")
    
    print("Area median Income:")
    print("Query the most recent Census Bureau report for the property's zip code\n")
    
    print("FEMA Disasters:")
    print("Check all past and ongoing FEMA disaster declarations in the area of your subject property and review the five most recent events.\n\n")
    
    print("\n\n\n-=-=-=-=-= Instant APOR =-=-=-=-=-\n\n")
    print("Instant APOR checks your average percentage rate (APR) against the average prime offer rate (APOR) as of your rate lock day.")
    print("This useful tool ensures that the rate you provide to your borrower fits standards set by the CFPB.\n")
    print("NOTE: APR Varies from your interest rate in that it adds the finance charges of the transaction to the interest rate for determining lifetime cost of loan\n\n\n")
    
    input("Press 1 to return to previous screen: ")
    return
    
    
if __name__ == "__main__":
    ProgramInfo()