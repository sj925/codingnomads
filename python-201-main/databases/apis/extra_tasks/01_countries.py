'''
Use the countries API https://restcountries.com/ to fetch information
on your home country and the country you're currently in.

In your python program, parse and compare the data of the two responses:
* Which country has the larger population?
* How much does the are of the two countries differ?
* Print the native name of both countries, as well as their capitals

'''
import requests 
from pprint import pprint

url = "https://restcountries.com/v3.1/name"
country1 = "United States"
country2 = "Ireland"
response1 = requests.get(f"{url}/{country1}")
response2 = requests.get(f"{url}/{country2}")
usa_data = (response1.json()[1])
ireland_data = (response2.json()[1])

def get_population(data):
     population = data["population"]
     return f"the population of {get_nativename(data)} is {population}"

def get_nativename(data):
    nativename = data['name']['nativeName']
    lang = list(nativename.keys())[0]
    return nativename[lang]['official']

def get_area_difference(data1, data2):
    area1 = data1['area']
    area2 = data2['area']
    difference = abs(area1 - area2)
    return f"The area difference between {get_nativename(data1)} and {get_nativename(data2)} is {difference:,.2f} square kilometers"

def get_capital(data):
    return f"the capital of {get_nativename(data)} is {data["capital"][0]}"

print(get_area_difference(ireland_data, usa_data))
print(get_nativename(usa_data))
print(get_nativename(ireland_data))
print(get_population(usa_data))
print(get_population(ireland_data))
print(get_capital(usa_data))
print(get_capital(ireland_data))
