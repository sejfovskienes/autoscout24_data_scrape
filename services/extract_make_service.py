from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from services import driver_service


def extract_make_values():
    driver = driver_service.setup_driver()
    make_dropdown = Select(driver.find_element(By.ID, "make"))

    for x in make_dropdown.options:
        print(x.text)

    return make_dropdown