import unittest
from announcement.models import Announcement

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# Create your tests here.
#   executable_path= r'C:\Users\leonn\OneDrive\Área de Trabalho\Desafio_Web_Scraping_Fotebol\Projeto2\app\chromedriver.exe'
# run test : python manage.py test
class TestAnounce(unittest.TestCase):
    
    #Test Case Valid
    def test_valid1(self):
        data_expected = 'Is triangle'
        
        data_test_1 = 4
        data_test_2 = 7
        data_test_3 = 8
        
        # result = main.main(data_test_1, data_test_2, data_test_3)
        
        # self.assertEqual(result,data_expected)


if __name__ == '__main__':
    unittest.main()