import requests
import pandas as pd
import schedule 
import time
from datetime import datetime

#Function to pipe data from the api database and stores it in dataframe
def weather_pipe():
    respond  = requests.get("https://api.openweathermap.org/data/2.5/weather?q=London&appid=7578f10f150554ae3e45a20691bca61d")
    data = respond.json()
#Extracting needed info from the api database
    min_temperature = data['main']['temp_min']
    max_temperature = data['main']['temp_max']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind_speed = data['wind']['speed']
    #Gets the current date and time from your computer in a formatted string
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#Turning the data into a dataframe
    weather_df = pd.DataFrame([{

    'Temp_min': min_temperature,
    'Temp_max': max_temperature,
    'Pressure': pressure,
    'Humididty': humidity,
    'Wind_Speed': wind_speed

    }])
# header=not pd.io.common.file_exists(...) the header is only written once.
    weather_df.to_csv('Weather_data.csv',mode='a', header=not pd.io.common.file_exists('Weather_data.csv'), index=False)

    print(weather_df)

schedule.every(1).hours.do(weather_pipe)

print("Scheduler started. Waiting to run every hour...")

while True:
    schedule.run_pending()
    time.sleep(1)