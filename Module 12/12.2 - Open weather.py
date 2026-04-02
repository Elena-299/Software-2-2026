import requests, json

municipality = input("Enter a municipality: ")
key = "1afbb216fcd4c1e6706b9873cbafa262"
request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={key}"
response = requests.get(request).json()
if response.get("cod") != 200:
    print(f"Error: {response.get('message','unknown error')} ")
else:
    description = response["weather"][0]["description"]
    temp_celsius = response["main"]["temp"] - 273.15
    print(f"The weather in {municipality}: {description} | Temperature: {temp_celsius:.1f} Celsius degrees")