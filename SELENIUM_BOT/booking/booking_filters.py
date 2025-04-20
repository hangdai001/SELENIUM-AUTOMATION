from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class booking_filters:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def star_rating(self, *star_values):
        close_map = self.driver.find_element(By.XPATH, '//button[@aria-label="Close map"]')
        close_map.click()

        for star_value in star_values:
            stars = self.driver.find_element(By.XPATH, f'//input[@name="class={star_value}"]')
            stars.click()

    def sort_by_filter(self):
        self.driver.find_element(By.XPATH, '//button[@data-testid="sorters-dropdown-trigger"]').click()
        sort = self.driver.find_element(By.XPATH, '//button[@data-id="price"]')
        sort.click()

        # sort_by_list = self.driver.find_elements(By.XPATH, '//ul[@class="ad7c39949a"]//button')
        # for sort in sort_by_list:
        #     daaa = sort.get_attribute("data-id")
        #     print(daaa)
