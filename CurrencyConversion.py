import pandas as pd #Import Panda as pd 
import requests #import request (To allow the request of a HTTP (One of Pythons HTTP library))
r = requests.get('https://v6.exchangerate-api.com/v6/92b6d8d45f1603ce1b3163bc/latest/USD') #Grab the request from a currency conversion API
json = r.json() #Set json as r, the requested HTTP variable, .json to trasport data to variable
#print(json)
df = pd.DataFrame(json['conversion_rates'], index=[0]) #pandas.DataFrame of the json key "conversion_rates", at index 0 (Max is index 0 because it is a single dictionary and not a list)
#print(df)
initial = input("What currency are you converting from(Please enter the currency acronym)? ") #Questions
final = input("What currency are you converting to? ")
value = float(input("How much of this currency do you want to convert? "))
initial_c = float(df.get(initial))
final_c = float(df.get(final))
#print(str(initial_c) + ": "+ str(final_c))
converted = value * (final_c/initial_c) #The conversion using ratio
print("If you were to convert "+str(value) +" "+ initial + "to " + final + ", you would have " + str(converted) + " " + final) #Result


