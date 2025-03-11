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
ireland_data = (response2.json()[0])
usa_population = usa_data["population"]
ireland_population = ireland_data["population"]
print(f"the US population is: {usa_population}, the Irish population is: {ireland_population}")