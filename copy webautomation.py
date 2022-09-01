import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class demo_explicit_wait():
    def test_explicit_wait_Value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.set_page_load_timeout(10)
        depart_form = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_form.click()
        time.sleep(5)
        depart_form.send_keys("Dhaka")
        time.sleep(5)
        depart_form.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New york")
        time.sleep(3)
        search_result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            if "New York (JFK)" in results.text:
                results.click()
                break

        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.ID, "BE_flight_origin_date"))).click()

        # origin_date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        # origin_date.click()
        all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' ]"))).find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' ]")
        # all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD' ]")
        for date in all_dates:
            if date.get_attribute("data-date") == "10/09/2022":
                time.sleep(6)
                date.click()
                time.sleep(6)
                break

        driver.find_element(By.ID, "BE_flight_flsearch_btn").click()


test_explicit_wait = demo_explicit_wait()
test_explicit_wait.test_explicit_wait_Value()

