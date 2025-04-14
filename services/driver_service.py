from selenium import webdriver

def setup_driver():
    url = 'https://www.autoscout24.com/'
    driver = webdriver.Chrome()
    driver.get(url)

    if(driver):
        print("driver initialized succesfully")
    else:
        print("error while initializing driver")

    return driver