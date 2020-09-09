from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import user_model

#from tester import getLocation

# import json
# import requests
# from bs4 import BeautifulSoup

class user_controller:
    user_ID = None
    
    @classmethod
    def get_coordinates(cls):
        options = Options()
        options.add_argument("--use-fake-ui-for-media-stream")
        timeout = 20
        driver = webdriver.Chrome(executable_path = './chromedriver.exe', chrome_options=options)
        driver.get("https://mycurrentlocation.net/")
        wait = WebDriverWait(driver, timeout)
        time.sleep(3)
        longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
        longitude = [x.text for x in longitude]
        longitude = str(longitude[0])
        latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
        latitude = [x.text for x in latitude]
        latitude = str(latitude[0])
        driver.quit()
        return (latitude,longitude)

    @classmethod    
    def get_location(cls):
        locator = Nominatim(user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", timeout = 1)
        run_locator = RateLimiter(locator.reverse, min_delay_seconds=1)
        coordinates = (user_controller.get_coordinates())
        location = run_locator(coordinates, language = "en", exactly_one = True)
        location.raw
        loc_String = str(location.address)
        loc_list = loc_String.split(", ")
        return loc_list
     

    # def get_location(cls):
    #     source = requests.get("https://ipinfo.io/json").text
    #     soup = BeautifulSoup(source,"html.parser")
    #     json_text = json.loads(soup.text)
    #     location_info = json_text
    #     return location_info

class registered_user(user_controller):

    def __init__(self):
        self.model = user_model.user_model()
        self.model.create_table()   

    def add_user(self, f_name, l_name, u_ID, password):
        user_ID = u_ID
        self.model.new_user(f_name, l_name, u_ID, password)


    def login(self, u_ID, password):
        user_ID = u_ID
        return self.model.login(u_ID, password)

    def logout(self):
        user_ID = None
        self.model.logout()

    def logged_in_user(self):
        user = self.model.logged_in_user()
        return user

    #test method
    def show_users(self):
        all_records = self.model.show_users()
        print(all_records)
        
    #test method
    def delete_all(self):
        self.model.delete_all()