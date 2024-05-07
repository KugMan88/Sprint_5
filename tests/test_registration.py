from user import RandomUser
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators



class TestBurgersRegistration:
    def test_registration_registered(self, driver):
        name = RandomUser.user_name
        email = RandomUser.email
        password = RandomUser.password
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.REG_CARD_NAME)))
        driver.find_element(*Locators.REG_NAME).click()
        driver.find_element(*Locators.ACTIVE_REG_POLE).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).click()
        driver.find_element(*Locators.ACTIVE_REG_POLE).send_keys(email)
        driver.find_element(*Locators.REG_PASS).send_keys(password)
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        text = driver.find_element(*Locators.LOG_CARD_NAME).text
        assert text == 'Вход'

    def test_registration_registration_error(self, driver):
        name = RandomUser.user_name
        email = RandomUser.email
        driver.find_element(*Locators.PERS_AREA).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.BUTTON_LOGIN)))
        driver.find_element(*Locators.REG_LINK).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((Locators.REG_CARD_NAME)))
        driver.find_element(*Locators.REG_NAME).click()
        driver.find_element(*Locators.ACTIVE_REG_POLE).send_keys(name)
        driver.find_element(*Locators.REG_EMAIL).click()
        driver.find_element(*Locators.ACTIVE_REG_POLE).send_keys(email)
        driver.find_element(*Locators.REG_PASS).send_keys('12345')
        driver.find_element(*Locators.REG_BUTTON).click()
        text = driver.find_element(*Locators.UNCORRECT_PASS).text
        assert text == 'Некорректный пароль'