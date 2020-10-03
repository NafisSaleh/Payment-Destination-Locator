import unittest
from unittest import mock
from Control import user_controller
import selenium.common.exceptions as se

class test_user_controller(unittest.TestCase):
    
    # def test_connection(self):
    #     self.assertRaises(se.WebDriverException, user_controller.get_coordinates)#, msg="**No connection problems**")

    def test_get_coordinates(self):
        try:
            latit, longit = user_controller.get_coordinates()
            print("latitude: "+latit)
            print("longitude: "+longit)
            self.assertRegex(str(latit), "[0-9]+\.[0-9]+", msg="Incorrect Latitude")
            self.assertRegex(str(longit), "[0-9]+\.[0-9]+", msg="Incorrect Longitude")
        except se.WebDriverException:
            self.fail(msg="Error: Check internet connection")    
        
    def test_get_location(self):
        try:
            with mock.patch("Control.user_controller.get_coordinates", return_value = (23.75080, 90.42195)):
                address = user_controller.get_location()
                print("address: "+address)
                self.assertRegex(address, "([A-Za-z0-9\s,]+\s[0-9A-Za-z]+)+", msg="Invalid Address!")
        except:
            self.fail(msg="Error: Check internet connection or access to Nominatim api services")

if __name__ == '__main__':
    unittest.main()