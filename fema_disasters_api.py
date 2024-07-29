'''
FEMA Disaster check microservice
'''
# grab county from zip code

import requests

def CheckFema(state):
    
    # get county from user:
    county = input("What county is your property located in?\n")
    
    
    api_url = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
    query = {
        "$format": "json", # returns disaster summary in json to parse through
        "$filter": f"state eq '{state}' and designatedArea eq '{county} (County)'", # returns only disasters in state and county provided
        "$orderby": "incidentBeginDate desc", # puts most recent disasters at top
        "$top": 5 # return top 5
        } 
    
    response = requests.get(api_url, params = query)
    response = response.json() # convert response to json
    response = response['DisasterDeclarationsSummaries']  # filter to just the disaster summaries of the json
    return response
    
if __name__ == "__main__":
    # testing
    disasters = CheckFema("CA", "Los Angeles")
    disaster_count = 1
    
    for disaster in disasters: 
        print(f"\n{disaster_count}. Disaster Number: {disaster['disasterNumber']}\n Disaster Title: {disaster['declarationTitle']}\n Start Date: {disaster['incidentBeginDate'].split('T')[0]}\n End Date: {disaster['incidentEndDate'].split('T')[0]}\n Declaration Date: {disaster['declarationDate'].split('T')[0]}")
        disaster_count += 1