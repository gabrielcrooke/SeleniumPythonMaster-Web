
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element("id", "id-search-field")
elem.clear()
elem.send_keys("pycon")

time.sleep(10)

driver.close()