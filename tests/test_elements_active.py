from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from user import User


class TestBurgersElements:
    def test_active_element_sauce(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER),"Оформить заказ"))
        driver.find_element(*Locators.ELEM_SAUCE).click()
        assert driver.find_element(*Locators.ACTIVE_ELEM).text == 'Соусы'

    def test_active_element_buns(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER), "Оформить заказ"))
        driver.find_element(*Locators.ELEM_SAUCE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.ELEM_BUNS)))
        driver.find_element(*Locators.ELEM_BUNS).click()
        assert driver.find_element(*Locators.ACTIVE_ELEM).text == 'Булки'

    def test_active_element_toppings(self, driver):
        driver.find_element(*Locators.BUTTON_LOGIN_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.EMAIL_AUTOR).send_keys(User.email)
        driver.find_element(*Locators.PASS_AUTOR).send_keys(User.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.text_to_be_present_in_element((Locators.BUTTON_ORDER),"Оформить заказ"))
        driver.find_element(*Locators.ELEM_TOPPINGS).click()
        assert driver.find_element(*Locators.ACTIVE_ELEM).text == 'Начинки'