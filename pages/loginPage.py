from locators.page_elements import *
from utils import environment as env
from extensions.commands import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    def is_title_matches(self):
        return "Log in to Sell-In" in self.driver.title

    """Login creds for use in checkout flow"""
    def login_as_standard_user(self):
        username = self.driver.find_element(*LoginPageLocators.USN_INPUT)
        password = self.driver.find_element(*LoginPageLocators.PWD_INPUT)
        submit_login = self.driver.find_element(*LoginPageLocators.LOGIN_CTA)

        username.send_keys(env.user)
        password.send_keys(env.pwd)
        submit_login.click()

    def search_test(self):
        # search_field = self.driver.find_element(*Search.SEARCH_FIELD)
        # search_cta = self.driver.find_element(*Search.SEARCH_CTA)
        email = self.driver.find_element(*Search.FB_USERNAME)
        password = self.driver.find_element(*Search.FB_PASSWORD)
        login = self.driver.find_element(*Search.FB_CTA)

        assert login.get_attribute("value") == "Log In"
        email.send_keys("manoknapulaaaaaaaa")
        password.send_keys("Password123")
        login.click()

        # Commands.is_visible(search_cta)
        # Commands.if_visible_click(*Search.SEARCH_CTA)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Search.SEARCH_CTA)).click()
        # cta_test = '(// input[@ value="Google Search"])[2]'
        # Commands.if_visible_click_xpath(cta_test)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, cta_test))).click()

    def screenshot(self):
        Commands.take_screenshot(self.driver, test="search_test")