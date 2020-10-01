from pandas.io.html import read_html
import pandas as pd
from unittest import TestCase, mock, main
from pandas.testing import assert_frame_equal

from Control import bank_controller


class test_bank_controller(TestCase):

    def setUp(self):
        print("****SET UP****")
        self.bc = bank_controller()
        #print(bc.testerDataFrameFile)
        self.bc.AddBankToDataFrame("Brac Bank","https://www.banksbd.org/brac/branches/dhaka.html")
        #print(bc.testerDataFrameFile)
        self.test_df = pd.DataFrame({'BANKNAME':[],'BRANCH':[],'ADDRESS':[],'CONTACT':[]},columns=['BANKNAME','BRANCH','ADDRESS','CONTACT'])
        #print(test_df)
        test_page = pd.read_html("https://www.banksbd.org/brac/branches/dhaka.html",attrs={"class":"table table-striped"})
        columnName=['BRANCH','ADDRESS','CONTACT']
        columnNameReordered=['BANKNAME','BRANCH','ADDRESS','CONTACT']

        for items in test_page:
            items.columns=columnName
            items['BANKNAME']="Brac Bank"
            items=items[columnNameReordered]
            #self.testerDataFrameFile=pd.concat([self.testerDataFrameFile,items],ignore_index=True)
            self.test_df=pd.concat([self.test_df,items],ignore_index=True)
        self.test_df['BANKNAME'] = self.test_df['BANKNAME'].str.upper()
        self.test_df['BRANCH'] = self.test_df['BRANCH'].str.upper()    

    def test_AddBankToDataFrame(self):
        try:
            print("****ADD BANK TO DATAFRAME TEST****")
            self.bc.AddBankToDataFrame("Islami Bank","https://www.banksbd.org/ibbl/branches/dhaka.html")
            test_page = pd.read_html("https://www.banksbd.org/ibbl/branches/dhaka.html",attrs={"class":"table table-striped"})
            columnName=['BRANCH','ADDRESS','CONTACT']
            columnNameReordered=['BANKNAME','BRANCH','ADDRESS','CONTACT']
            for items in test_page:
                items.columns=columnName
                items['BANKNAME']="Islami Bank"
                items=items[columnNameReordered]
                #self.testerDataFrameFile=pd.concat([self.testerDataFrameFile,items],ignore_index=True)
                self.test_df=pd.concat([self.test_df,items],ignore_index=True)
            self.test_df['BANKNAME'] = self.test_df['BANKNAME'].str.upper()
            self.test_df['BRANCH'] = self.test_df['BRANCH'].str.upper()    
            # print("****PRINTING TEST_DF****")    
            # print(self.test_df)
            # print("****PRINTING BANK_CONTROL_DF****")
            # print(self.bc.testerDataFrameFile)    
            assert_frame_equal(self.bc.testerDataFrameFile, self.test_df)
        except:
            self.fail(msg="Error: connection problem or unequal dataframes")
        
    def test_SearchDataFrameByLocation(self):
        try:
            print("****SEARCH DATAFRAME BY LOCATION TEST****")
            compare_df = self.bc.SearchDataFrameByLocation("Banasree")
            df = self.test_df[self.test_df['BRANCH']=="BANASREE"]
            assert_frame_equal(compare_df, df)
        except:
            self.fail(msg="Error: unequal dataframes")

    def test_SearchDataFrameByPrefered(self):
        try:
            print("****SEARCH DATAFRAME BY PREFERRED TEST****")
            compare_df = self.bc.SearchDataFrameByPrefered("Brac Bank")
            df = self.test_df[self.test_df['BANKNAME']=="BRAC BANK"]     
            assert_frame_equal(compare_df, df)
        except:
            self.fail(msg="Error: unequal dataframes")

    def test_get_branch_list(self):
        #try:
        print("****GET BRANCH LIST TEST****")
        compare_df_list = self.bc.get_branch_list()
        df_list = self.test_df["BRANCH"].unique()
        #print(compare_df_list)
        print(type(df_list))
        print(df_list)
        #compare_df_list = []
        self.assertEqual(list(compare_df_list), list(df_list), msg="Error: unequal lists")
        # except:
        #     self.fail(msg="Error: unequal lists")

    def test_see_nearby_banks(self):
        print("****SEE NEARBY BANKS TEST****")
        #location_list = ["Road", "03", "Gulshan", "1", "Dhaka", "1212 "]
        location_list = ["Banasree", "Rampura", "Dhaka"]
        compare_df_list = None
        mock_df = self.test_df[self.test_df['BRANCH']=="BANASREE"]
        with mock.patch("Control.bank_controller.SearchDataFrameByLocation", return_value = mock_df):
            compare_df_list = self.bc.see_nearby_banks(location_list)
        print("compare_df_list:")    
        print(compare_df_list)    
        res_list = []
        index = 0
        while(index<=len(location_list)-1):
            print("index: "+str(index))
            print("content:"+str(location_list[index]))
            df_tester = self.test_df[self.test_df["BRANCH"]==location_list[index].upper()]#self.SearchDataFrameByLocation(location_list[index])
            if not df_tester.empty:
                listtester=df_tester.values.tolist()
                for test in listtester:
                    res_list.append(test)
                break
            index += 1
        print("res_list:")    
        print(res_list)    
        self.assertEqual(compare_df_list, res_list, msg="Error: unequal lists")    

    def test_see_nearby_banks_wrong(self):
        print("****SEE NEARBY BANKS WRONG TEST****")
        #location = "BANANI"
        location = "UTTARA"
        compare_df_list = None
        mock_df = self.test_df[self.test_df['BRANCH']==location]
        with mock.patch("Control.bank_controller.SearchDataFrameByLocation", return_value = mock_df):
            # print("mock method test:")
            # print(self.bc.SearchDataFrameByLocation())
            compare_df_list = self.bc.see_nearby_banks_wrong(location)
        print("compare_df_list:")    
        print(compare_df_list)    
        res_list = []
        df = self.test_df[self.test_df['BRANCH']=="UTTARA"]
        if not df.empty:
            listtester = df.values.tolist()
            for test in listtester:
                res_list.append(test)
        # print(dftester)
        print("res_list:")    
        print(res_list)    
        self.assertEqual(compare_df_list, res_list, msg="Error: unequal lists")    

    def test_search_bank(self):
        print("****SEARCH BANKS TEST****")
        #bank = "ISLAMI BANK"
        bank = "BRAC BANK"
        compare_df_list = None
        mock_df = self.test_df[self.test_df['BANKNAME']==bank]
        with mock.patch("Control.bank_controller.SearchDataFrameByPrefered", return_value = mock_df):
            # print("mock method test:")
            # print(self.bc.SearchDataFrameByPrefered())
            compare_df_list = self.bc.search_bank(bank)
        res_list = []
        df = self.test_df[self.test_df['BANKNAME']=="BRAC BANK"]
        df_list = df.values.tolist()
        for item in df_list:
            res_list.append(item)
        self.assertEqual(compare_df_list, res_list, msg="Error: unequal lists")
        #self.assertNotEqual(compare_df_list, [], msg="Error: empty list")

if __name__=="__main__":
    main()   