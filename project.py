import requests

from datetime import datetime

api_key = 'ada9292c65b85dc24ee9decdc73ae24c'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} °C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

#Appending data in a text file

with open('myfile.txt', 'a') as file:
    file.write("City = " + location + "\n" + "Date and Time = " + date_time + "\n" + "Temperature = " + str(format(temp_city,".2f")) + " °C" +
               "\n" + "Weather Description = " + weather_desc + "\n" + "Humidity = " + str(hmdt) + " %" + "\n" + "Wind Speed = " + str(wind_spd) + " kmph" +"\n\n")
file.close()