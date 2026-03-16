import os
import requests
from dotenv import load_dotenv
import pandas as pd
import streamlit as st

load_dotenv()
weatherapi_key = os.getenv('weatherapi_key')

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={weatherapi_key}&q={city}&aqi=no"
    return requests.get(url).json()

st.title(f"Weather App")

city = st.text_input("Enter a city name for which you want the weather: ")

if __name__ == "__main__":

    if city:
        weather = get_weather(city)
    else:
        st.warning("Please enter a city name to get the weather information.")
        st.stop()

    st.markdown("---")

    st.write(f"Temperature (°C): {weather['current']['temp_c']}")
    st.write(f"Condition: {weather['current']['condition']['text']}")
    st.write(f"Wind Speed (km/h): {weather['current']['wind_kph']}")

    
    