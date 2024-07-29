'''
APOR Microservice. FFIEC API provides a rate spread calcualtion given specific loan terms. Using the rate spread,
we can add it back to the APR and get the APOR on the given day. This is a basic calcution, but users like to see
APOR in addition to the rate spread.
'''

import requests
import json

def get_apor(loanTerm, apr, lockDate):
    api_url = "https://ffiec.cfpb.gov/public/rateSpread"
    payload = {
        "actionTakenType": 1,            # assume loan originated for project scope
        "loanTerm": loanTerm,            # 1-30 years typically, but supports up to 50 year mortgage
        "amortizationType": 'FixedRate', # assume fixed rate for project scope
        "apr": apr,                      # can use interest rate for the exercise but APR usually takes into account finance costs as well
        "lockInDate": lockDate,          # date the loan was locked with investor/lender
        "reverseMortgage": 2             # not a tool for reverse mortgages in the scope o fthis project
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))
    response = response.json()
    rateSpread = float(response['rateSpread'])
    return rateSpread

if __name__ == "__main__":
    apr = 8.0
    rateSpread = get_apor(30,apr, "2023-11-29")
    apor = float(apr) - rateSpread
    print(f"\nAPR: {apr}")
    print(f"APOR: {apor}")
    print(f"Rate Spread: {rateSpread}")