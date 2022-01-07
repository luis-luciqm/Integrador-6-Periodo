import unittest
from announcement.models import Announcement
from .views import ParticipateAnnounceFun
from authentication.models import User

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class TestAnounce(unittest.TestCase):
    
    def temp(self, value):
        time.sleep(value)

    def testvalid1(self):
        user = User.objects.get(username='leonas')
        slug = 'lorem-ipsum-dolor-sit-amet-consectetur-adipiscing'
        url = f'http://localhost:8000/anuncio/detalhes_anuncio/{slug}/'
        driver = webdriver.Chrome(executable_path='/home/leonardo/Área de Trabalho/IF/chromedriver_linux64/chromedriver')
        driver.get(url)
        
        self.temp(5)
        data = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div[3]/a')
        data.click()
        
        data_email = driver.find_element_by_xpath('//*[@id="username"]')
        data_password = driver.find_element_by_xpath('//*[@id="password"]')
        
        self.temp(2)
        data_email.send_keys('l4@gmail.com')
        data_password.send_keys('ifrn12345')

        data_password.submit()

        self.temp(4)
        data = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div[3]/a')
        data.click()

        self.temp(2)
        data_expected = 'Você ja se candidatou a esta vaga.'
        # data_expected = '//*[@id="app"]/div/div[3]/section/ul/li'
        data_result = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/ul/li[1]')

        # print('\n\n\n',data_result.text,'\n\n\n')
        print(data_expected,' ---> ', data_result.text)
        self.assertEqual(data_result.text, data_expected) 

    def testinvalid1(self):
        user = User.objects.get(username='leonas')
        slug = 'lorem-ipsum-dolor-sit-amet-consectetur-adipiscing'
        url = f'http://localhost:8000/anuncio/detalhes_anuncio/{slug}/'
        driver = webdriver.Chrome(executable_path='/home/leonardo/Área de Trabalho/IF/chromedriver_linux64/chromedriver')
        driver.get(url)
        
        self.temp(5)
        data = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div[3]/a')
        data.click()
        
        data_email = driver.find_element_by_xpath('//*[@id="username"]')
        data_password = driver.find_element_by_xpath('//*[@id="password"]')
        
        self.temp(2)
        data_email.send_keys('l4@gmail.com')
        data_password.send_keys('ifrn12345')

        data_password.submit()

        self.temp(4)
        data = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/div[2]/div[2]/div[3]/a')
        data.click()

        self.temp(2)
        data_expected = 'Você agora está concorrendo a vaga. Boa sorte!'
        # data_expected = '//*[@id="app"]/div/div[3]/section/ul/li'
        data_result = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/section/ul/li')

        # print('\n\n\n',data_result.text,'\n\n\n')
        print(data_expected,' ---> ', data_result.text)
        self.assertEqual(data_result.text, data_expected) 

    #Test Case Valid
       
            


if __name__ == '__main__':
    unittest.main()