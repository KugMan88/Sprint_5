from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from user import User


class TestBurgersPersonalArea:
    def test_personal_area(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER),"Оформить заказ"))
        driver.find_element(*Locators.PERS_AREA).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element((Locators.PROFILE_TEXT),"Профиль"))