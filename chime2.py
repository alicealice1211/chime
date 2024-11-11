import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import undetected_chromedriver as uc
 


def setup():
    global driver
    # options = uc.ChromeOptions()
    # driver = uc.Chrome(options = options)
   
    driver = webdriver.Chrome()
    driver.get('https://app.chime.com/login')


def login():
    #enter user name
    driver.find_element(By.XPATH, '//label[@for="Email"]').send_keys('alicealice1211@gmail.com')
    time.sleep(0.1)
    
    #enter user password
    driver.find_element(By.XPATH, '//label[@for="Password"]').send_keys('Chimetesting1')
    time.sleep(0.1)
    
    #enter
    driver.find_element(By.XPATH, '//label[@for="Password"]').send_keys(Keys.ENTER)
    time.sleep(1)
    
def enter_code():
    #enter verfication code
    code = input('enter verfication code: ')
    
    #pop-up
    body_element = driver.find_element(By.XPATH, '//body')
    body_element.send_keys(Keys.ESCAPE)
    
    #enter code
    driver.find_element(By.XPATH, '//label[@for="Security code"]').send_keys(str(code))
    time.sleep(0.1)
    
    #enter
    driver.find_element(By.XPATH, '//label[@for="Security code"]').send_keys(Keys.ENTER)
    time.sleep(1)

def scrape_balance():
    time.sleep(5)
    balance = driver.find_element(By.XPATH, '//a[@href="/accounts/checking"]').text.split('\n')[1]
    print('Checking Account: '+str(balance))
    
def main():
    setup()
    login()
    enter_code()
    scrape_balance()
    time.sleep(10)
    
if __name__ == '__main__':
    main()
 




