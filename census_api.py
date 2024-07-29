import requests

def get_ami(zip_code):
    """
    takes a zip code as a parameter and returns the area median income for households in that area
    """
    api_url = "https://api.census.gov/data/2020/acs/acs5"
    query = {
        "get": "B19013_001E", # B19013_001E is household income, see https://api.census.gov/data/2019/acs/acs5/groups/B19013.html
        "for": f"zip code tabulation area:{zip_code}",
    }

    response = requests.get(api_url, params = query)
    response = response.json()
    ami = response[1][0]  # row 1 is header, row 2 is income number
    return ami


if __name__ == "__main__":
    zip_code = "91321"
    median_income = get_ami(zip_code)
    if median_income:
        print(f"\nThe median household income for ZIP code {zip_code} is ${median_income}")
