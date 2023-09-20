from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests


Webdriver = webdriver.Chrome()

Website_url = "https://www.weather.com/"
# Zip code for the location we want to get the info of
zip_code = "20852"

def test_get_temperature_byZIPCode(zip_code_data):
    Webdriver.get(Website_url)

    WebDriverWait(Webdriver, 20).until(EC.element_to_be_clickable((By.ID, "LocationSearch_input")))
    Value = Webdriver.find_element(By.XPATH, '//*[@id="LocationSearch_input"]')
    #Value = Webdriver.find_element(By.XPATH, "//input[@id='LocationSearch_input' and @class='SearchInput--InputField--1UoCv']")
    Value.click()
    Value.send_keys(zip_code_data)
    Value.send_keys(Keys.ENTER)

    Temperature = Webdriver.find_element((By.XPATH, "//span[data-testid='TemperatureValue'"))
    print(Temperature)
    return Temperature

test_get_temperature_byZIPCode(zip_code)


api_key = "API_KEY_To_set"

api_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={zip_code}&aqi=no"

def test_get_temperature_byZIPCodeAPI(zip_code_data):
    # Send the API request
    response = requests.get(api_url)

    if response.status_code == 200:

        weather_data = response.json()
        temperature_celsius = weather_data["current"]["temp_c"]

    # Print the weather data
        print(f"Temperature: {temperature_celsius}°C ")
        return temperature_celsius


temp1= test_get_temperature_byZIPCode(zip_code)
tempAPI = test_get_temperature_byZIPCodeAPI(zip_code)

allowable_percentage_difference = 10

def calculate_diff_and_check_smaller_than_10(temp1, temp2):# Calculate the percentage difference between the temperatures
    percentage_difference = abs(temp1 - temp2) / temp1 * 100
    if percentage_difference <= allowable_percentage_difference:
         print(f"The temperature difference is within {allowable_percentage_difference}%.")
    else:
        print(f"The temperature difference exceeds {allowable_percentage_difference}%.")

calculate_diff_and_check_smaller_than_10(temp1,tempAPI)