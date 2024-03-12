import requests
import json
import pyttsx3

engine = pyttsx3.init()
print("Welcome To the Weather Service, Hope You enjoy the service ")
city = input("Enter the name of the City \n")
url = f"http://api.weatherapi.com/v1/current.json?key=7df248cc70fa490286035106241103&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
while True :

    a = int(input("What you Want to access in weather option \n 1. Temperature in celsius \n 2. Temperature in fahrnite \n 3. "
              "Wind speed in Kmph \n 4. pressure  \n 5. stop \n"))

    match a:
        case 1:
            print(wdic["current"]["temp_c"])
            engine.say(f"The current Temperature at {city} is {wdic["current"]["temp_c"]} degree")
            engine.runAndWait()
        case 2:
            print(wdic["current"]["temp_f"])
            engine.say(f"the current Temperature in fahrenheit scale at {city} is {wdic["current"]["temp_f"]} ")
            engine.runAndWait()
        case 3:
            print(wdic["current"]["wind_kph"])
            engine.say(f"The current wind at {city} is {wdic["current"]["wind_kph"]} kilometer per hour  ")
            engine.runAndWait()
        case 4:
            print(wdic["current"]["pressure_mb"])
            engine.say(f"The current pressure at {city} is {wdic["current"]["pressure_mb"]} millibar ")
            engine.runAndWait()
        case 5:
            print("Thanks for Using our Weather service , We look again for your visit for service")
            break
        case _:
            print("Please reinsert Between number 1 to 5 ")


