from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import time

desired_capabilities = {
    'platformName': 'Android',
    'platformVersion': '13',  # Replace with '13' or your actual Android 13 version
    'deviceName': 'xyz',  # Replace with your actual device name
    'appPackage': 'com.serwylo.lexica',
    'appActivity': 'com.serwylo.lexica.MainMenuActivity',
    'automationName': 'UiAutomator2',
    'newCommandTimeout': 300,
}

appium_server_url = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(appium_server_url, desired_capabilities)

time.sleep(5)

# Find the element with ID "com.serwylo.lexica:id/high_score" using AppiumBy
element = driver.find_element(MobileBy.ID, 'com.serwylo.lexica:id/high_score')

print("High Score:", element.text)

driver.quit()

