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
        # case sensitivity handled
        # print(df1)
        print(df1.to_markdown())    


    def SearchDataFrameByPrefered(self, bankName="SKIP"):
        if(bankName=="SKIP"):
            print("SearchDataFrameByPrefered OPPERATION SKIPPED")
            return
        #global testerDataFrameFile
        df1=self.testerDataFrameFile[self.testerDataFrameFile['BANKNAME']==bankName.upper()]
        # case sensitivity handled
        # print(df1)
        print(df1.to_markdown())

    #def nearby_banks(self, location):

    #def search_bank(self, name):