# -*- coding: utf-8 -*-
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        #self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://demoqa.com/automation-practice-form")
        driver.find_element('id', "firstName").click()
        driver.find_element('id', "firstName").clear()
        driver.find_element('id', "firstName").send_keys("Gabriel")
        driver.find_element('id', "lastName").click()
        driver.find_element('id', "lastName").clear()
        driver.find_element('id', "lastName").send_keys("Crooke")
        driver.find_element('id', "userEmail").click()
        driver.find_element('id', "userEmail").clear()
        driver.find_element('id', "userEmail").send_keys("prueba01@gmail.com")
        driver.find_element('xpath', "//div[@id='genterWrapper']/div[2]/div/label").click()
        driver.find_element('id', "userNumber").click()
        driver.find_element('id', "userNumber").clear()
        driver.find_element('id', "userNumber").send_keys("8968774642")
        driver.find_element('xpath', "//div[@id='subjectsContainer']/div/div").click()
        driver.find_element('id', "subjectsInput").clear()
        driver.find_element('id', "subjectsInput").send_keys("Prueba 01")
        driver.find_element('xpath', "//div[@id='hobbiesWrapper']/div[2]/div[3]/label").click()
        driver.find_element('id', "currentAddress").click()
        driver.find_element('id', "currentAddress").clear()
        driver.find_element('id', "currentAddress").send_keys("Call 25")
        driver.find_element('id', 'react-select-3-input').send_keys('NCR' + Keys.ENTER + Keys.TAB)
        driver.find_element('id', 'react-select-4-input').send_keys('Noida' + Keys.ENTER)
        driver.find_element('id', 'submit').click()




    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
