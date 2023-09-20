from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Webdriver = webdriver.Chrome()

Website_url = "https://www.metric-conversions.org/"

def test_convert_by_type(value_type,unit_from, unit_to,  value_to_convert):
    Webdriver.get(Website_url)
    Value = Webdriver.find_element(By.LINK_TEXT, value_type)
    Value.send_keys(Keys.ENTER)

    input_unit = Webdriver.find_element(By.NAME, "unitFrom")
    Select(input_unit).select_by_value(unit_from)


    if (value_type != "Weight"):
        output_unit = Webdriver.find_element(By.NAME, "unitTo")
        Select(output_unit).select_by_value(unit_to)
        input_temp = Webdriver.find_element(By.NAME, "argumentConv")
        input_temp.send_keys(value_to_convert)

    if (value_type == "Weight"):
        print("here")
        output_unit = Webdriver.find_element(By.ID, "queryTo")
        output_unit.click()
        output_unit.send_keys(unit_to)
        WebDriverWait(Webdriver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "argument")))
        convert_box = Webdriver.find_element(By.CLASS_NAME, "argument")
        convert_box.send_keys(value_to_convert)
        Webdriver.find_element(By.LINK_TEXT, "Convert").click()

    converted_value = Webdriver.find_element(By.ID, "answer").text
    print(converted_value)
    return converted_value


test_convert_by_type("Temperature", "/temperature/celsius-conversion.htm", "/temperature/celsius-to-fahrenheit.htm", 25 )
test_convert_by_type("Length", "/length/meters-conversion.htm", "/length/meters-to-feet.htm",10)
test_convert_by_type("Weight", "/weight/ounces-conversion.htm", "grams",10)