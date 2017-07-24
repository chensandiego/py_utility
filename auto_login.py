from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



usernameStr=''
passwordStr=''

browser=webdriver.Chrome()

browser.get(('https://accounts.google.com/ServiceLogin?'
            'service=mail&continue=https://mail.google'
            '.com/mail/#identifier'))


username=browser.find_element_by_xpath("//input[@type='email']")
#username=browser.find_element_by_id('identifierId')
username.send_keys(usernameStr)

browser.find_element_by_xpath("//span[text()='Next']").click()
#nextButton=browser.find_element_by_class_name('CwaK9')

password1=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,"password")))

#gmail_password=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,"password")))
password1.send_keys(passwordStr)

browser.find_element_by_xpath("//span[text()='Next']").click()
