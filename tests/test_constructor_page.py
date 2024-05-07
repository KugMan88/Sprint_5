from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from user import User


class TestBurgersConstructor:
    def test_make_click_on_constructor(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER), "Оформить заказ"))
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element((Locators.PROFILE_TEXT), "Профиль"))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))

    def test_make_click_on_logo(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER), "Оформить заказ"))
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element((Locators.PROFILE_TEXT), "Профиль"))
        driver.find_element(*Locators.BUTTON_LOGO).click()
        assert WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((Locators.BUTTON_ORDER)))