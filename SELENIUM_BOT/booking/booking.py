import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from booking.booking_filters import booking_filters


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super().__init__(options=chrome_options)
        self.teardown = teardown
        self.implicitly_wait(3)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://www.booking.com")

    def currency_change(self, currency):
        currency_button = self.find_element(By.XPATH, '//button[@data-testid="header-currency-picker-trigger"]')
        currency_button.click()

        choose_currency = self.find_element(
            By.XPATH, f'//button[.//div[contains(@class, "CurrencyPicker_currency") and text()="{currency}"]]'
        )
        choose_currency.click()

    def destination(self, place):
        destination_name = self.find_element(By.XPATH, '//*[@id=":rh:"]')
        destination_name.location_once_scrolled_into_view
        destination_name.send_keys(place)
        time.sleep(1)
        self.find_element(By.XPATH, '//li[@id="autocomplete-result-2"]').click()

    def booking_date(self, checkin, checkout):
        check_in_date = self.find_element(By.XPATH, f'//span[@data-date="{checkin}"]')
        check_in_date.click()

        check_out_date = self.find_element(By.XPATH, f'//span[@data-date="{checkout}"]')
        check_out_date.click()

    def no_of_passengers(self, numpass):
        passenger = self.find_element(By.XPATH,'//button[@data-testid="occupancy-config"]')
        passenger.click()

        while True:
            decrease_button = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[1]')
            decrease_button.click()
            passenger_num = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/span').text

            if int(passenger_num)==1:
                break

        for i in range(numpass-1):
            increase_button = self.find_element(By.XPATH, '//*[@id=":ri:"]/div/div[1]/div[2]/button[2]')
            increase_button.click()

    def search(self):
        self.find_element(By.XPATH,'//*[@id="indexsearch"]/div[2]/div/form/div/div[4]/button').click()

    def apply_filter(self):
        filter_t = booking_filters(driver=self)
        filter_t.star_rating(4, 5)
        filter_t.sort_by_filter()

    import pandas as pd

    def result(self):
        data = []  # List to store dictionaries of hotel data

        hotels_list = self.find_elements(By.CSS_SELECTOR, '[data-testid="property-card-container"]')
        for hotel in hotels_list:
            try:
                hotels_name = hotel.find_element(By.CSS_SELECTOR, '[data-testid="title"]').text
            except:
                hotels_name = None
            try:
                hotels_price = hotel.find_element(By.CSS_SELECTOR, '[data-testid="price-and-discounted-price"]').text
            except:
                hotels_price = None

            data.append({
                'Hotel Name': hotels_name,
                'Price': hotels_price
            })

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Export to CSV
        df.to_csv('hotels.csv', index=False)
        print("Data exported to hotels.csv")


