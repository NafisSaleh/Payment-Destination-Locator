from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

import Model

#from tester import getLocation

# import json
# import requests
# from bs4 import BeautifulSoup

class user_controller:
    user_ID = None
    #wronglc = ""
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
        #loc_String = "Flat - 6B, House - 319, Road -2, Adabar 2, Mohammadpur, Dhaka - 1207"
        # loc_String = "Banani"
        # print(loc_String)
        return loc_String
        # loc_list = loc_String.split(", ")
        # loc_list_final=[]
        # for loc in loc_list:
        #     box = loc.split(" ")
        #     for item in box:
        #         loc_list_final.append(item)
        ## return loc_list_final
     

    # def get_location(cls):
    #     source = requests.get("https://ipinfo.io/json").text
    #     soup = BeautifulSoup(source,"html.parser")
    #     json_text = json.loads(soup.text)
    #     location_info = json_text
    #     return location_info

class registered_user(user_controller):

    def __init__(self):
        self.model = Model.user_model()
        self.model.create_table()   

    def add_user(self, f_name, l_name, u_ID, password):
        user_controller.user_ID = u_ID
        self.model.new_user(f_name, l_name, u_ID, password)


    def login(self, u_ID, password):
        user_controller.user_ID = u_ID
        return self.model.login(u_ID, password)

    def logout(self):
        user_controller.user_ID = None
        self.model.logout()

    def logged_in_user(self):
        user = self.model.logged_in_user()
        return user

    def not_duplicate(self, u_ID):
        if self.model.duplicate_checker(u_ID):
            return True
        return False        

    #test method
    def show_users(self):
        all_records = self.model.show_users()
        print(all_records)
        
    #test method
    def delete_all(self):
        self.model.delete_all()




#import history_model

class history_controller:

    user_ID = None

    def __init__(self, uID):
        history_controller.user_ID = uID

class transaction_history(history_controller):

    def __init__(self, uID=""):
        super().__init__(uID)
        self.model = Model.transaction_history()
        self.model.get_ID(history_controller.user_ID)

    def add_transaction(self, bill_type, amount, date, method):
        self.model.save_transaction(bill_type, method, amount, date)

    def check_transactions(self):
        box = self.model.show_transactions()
        print("control test:")
        for item in box:
                print(item)
        return box

    def update_uName(self, uID):
        self.model.get_ID(uID)    

    def delete_all(self):
        self.model.delete_all()  

class preffered_banks(history_controller):

    def __init__(self, uID=""):
        super().__init__(uID)
        self.model = Model.preferred_banks()
        self.model.get_ID(history_controller.user_ID)

    def save_preference(self, bank_name):
        self.model.save_preference(bank_name)

    def check_preferences(self):
        box = self.model.show_banks()
        return box           

    def update_uName(self, uID):
        self.model.get_ID(uID)

    def delete_all(self):
        self.model.delete_all()               




from pandas.io.html import read_html
import pandas as pd

class bank_controller:

    def __init__(self):
        # masterPandasFile=pd.DataFrame({'BANKNAME':[],'BRANCH':[],'ADDRESS':[],'CONTACT':[]},columns=['BANKNAME','BRANCH','ADDRESS','CONTACT'])

        self.testerDataFrameFile=pd.DataFrame({'BANKNAME':[],'BRANCH':[],'ADDRESS':[],'CONTACT':[]},columns=['BANKNAME','BRANCH','ADDRESS','CONTACT'])

        # pandas.set_option() TO PRINT AN ENTIRE PANDAS DataFrame
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)


    def AddBankToDataFrame(self, bankNameInput="SKIP", UrlInput="SKIP"):
        if(bankNameInput=="SKIP" and UrlInput=="SKIP"):
            print("ADDBankToDataFrame OPPERATION SKIPPED")
            return

        bankKey=bankNameInput
        pageUrl=UrlInput

        #global testerDataFrameFile


        # class="table table-striped"
        bankTableFromPage=pd.read_html(pageUrl,attrs={"class":"table table-striped"})
        columnName=['BRANCH','ADDRESS','CONTACT']
        columnNameReordered=['BANKNAME','BRANCH','ADDRESS','CONTACT']

        for items in bankTableFromPage:
            items.columns=columnName
            items['BANKNAME']=bankKey
            items=items[columnNameReordered]
            self.testerDataFrameFile=pd.concat([self.testerDataFrameFile,items],ignore_index=True)

        # data['Name'] = data['Name'].str.upper()
        # to deal with case sensitivity
        self.testerDataFrameFile['BANKNAME'] = self.testerDataFrameFile['BANKNAME'].str.upper()
        self.testerDataFrameFile['BRANCH'] = self.testerDataFrameFile['BRANCH'].str.upper()
        print(bankKey+" ADDED SUCCESSFULLY")


    def SearchDataFrameByLocation(self, location="SKIP"):
        if(location=="SKIP"):
            print("SearchDataFrameByLocation OPPERATION SKIPPED")
            return
        #global testerDataFrameFile
        df1=self.testerDataFrameFile[self.testerDataFrameFile['BRANCH']==location.upper()]
        return df1
        # case sensitivity handled
        # print(df1)
        #print(df1.to_markdown())    


    def SearchDataFrameByPrefered(self, bankName="SKIP"):
        if(bankName=="SKIP"):
            print("SearchDataFrameByPrefered OPPERATION SKIPPED")
            return
        #global testerDataFrameFile
        df1=self.testerDataFrameFile[self.testerDataFrameFile['BANKNAME']==bankName.upper()]
        # case sensitivity handled
        # print(df1)
        #print(df1.to_markdown())
        return df1

    def see_nearby_banks(self, loc_list):
        res_list = []
        index = 0
        while(index<=len(loc_list)-1):
            print("index: "+str(index))
            print("content:"+str(loc_list[index]))
            df_tester = self.SearchDataFrameByLocation(loc_list[index])
            if not df_tester.empty:
                listtester=df_tester.values.tolist()
                for test in listtester:
                    res_list.append(test)
                break
            index += 1
        # print(dftester)
        return res_list
        
    def get_branch_list(self):
        branches = self.testerDataFrameFile['BRANCH'].unique()
        print(branches)
        return branches

    def see_nearby_banks_wrong(self, loc):
        res_list = []  
        df_tester = self.SearchDataFrameByLocation(loc)
        if not df_tester.empty:
            listtester=df_tester.values.tolist()
            for test in listtester:
                res_list.append(test)
        # print(dftester)
        return res_list
        
    def search_bank(self, bank_name):
        res_list = []
        df_tester = self.SearchDataFrameByPrefered(bank_name)
        df_list = df_tester.values.tolist()
        for item in df_list:
            res_list.append(item)
        return res_list

    #def nearby_banks(self, location):
       

    #def search_bank(self, name):        