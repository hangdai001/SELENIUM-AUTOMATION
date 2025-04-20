import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()

driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]').click()

#Iphone
driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/div[1]/h4/a').click()

driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/ul[1]/li[1]/a/img').click()

next_click = driver.find_element(By.XPATH, '//button[@title="Next (Right arrow key)"]')

for i in range(5):
    time.sleep(1)
    next_click.click()

# driver.save_screenshot('ScreenShot#' + str(random.randint(1,1000)) + '.png')

driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]').click()

#IPHONE's Quantity
quantity = driver.find_element(By.XPATH, '//*[@id="input-quantity"]')
quantity.clear()
quantity.send_keys("2")
time.sleep(2)

driver.find_element(By.XPATH, '//button[@id="button-cart"]').click()
time.sleep(2)

#HOVER OVER THE NAV
op = driver.find_element(By.LINK_TEXT, 'Laptops & Notebooks')

actions = ActionChains(driver)
actions.move_to_element(op).perform()

drp_item = driver.find_element(By.LINK_TEXT, 'Show AllLaptops & Notebooks')
drp_item.click()

#HP LAPTOP
driver.find_element(By.XPATH, "//a[text()='HP LP3065']").click()

#Date Customization
date_select = driver.find_element(By.XPATH, '//input[@id="input-option225"]')
date_select.clear()
date_select.send_keys("2022-12-31")

#Submit ADD to Cart
addto = driver.find_element(By.XPATH, '//button[@id="button-cart"]')
addto.location_once_scrolled_into_view
addto.click()

driver.find_element(By.XPATH, '//*[@id="cart"]/button').click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Checkout").click()
time.sleep(2)

driver.find_element(By.XPATH, '//button[@data-original-title="Remove"]').click()
time.sleep(1)

chkout = driver.find_element(By.XPATH, '//a[text()="Checkout"]')
chkout.location_once_scrolled_into_view
chkout.click()
time.sleep(1)
#CHECKOUT Page
guest = driver.find_element(By.XPATH, '//input[@value="guest"]')
guest.location_once_scrolled_into_view
guest.click()

continue_button = driver.find_element(By.XPATH, '//input[@id="button-account"]')
continue_button.click()
time.sleep(2)
#Billing Details
driver.find_element(By.ID, "input-payment-firstname").send_keys("Fhashow")
driver.find_element(By.ID, "input-payment-lastname").send_keys("Leemoo")
driver.find_element(By.ID, "input-payment-email").send_keys("hangfoshow@hanging.com")
driver.find_element(By.ID, "input-payment-telephone").send_keys("9800214367")
#ADDRESS
driver.find_element(By.ID, "input-payment-company").send_keys("NA")
driver.find_element(By.ID,"input-payment-address-1").send_keys("Nigeria Falls, CA")
driver.find_element(By.ID,"input-payment-address-2").send_keys("Past first junction to the left")
driver.find_element(By.ID,"input-payment-city").send_keys("KTM CT")
driver.find_element(By.ID,"input-payment-postcode").send_keys("666")
driver.find_element(By.XPATH, '//*[@id="input-payment-country"]/option[17]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="input-payment-zone"]/option[8]').click()

continue_button1 = driver.find_element(By.XPATH, '//input[@id="button-guest"]')
continue_button1.location_once_scrolled_into_view
continue_button1.click()

time.sleep(1)
#Delivery Method
order_comment = driver.find_element(By.XPATH, '//*[@id="collapse-shipping-method"]/div/p[4]/textarea')
order_comment.send_keys("HELLO WORLD")

continue_button2 = driver.find_element(By.XPATH, '//input[@id="button-shipping-method"]')
continue_button2.click()

time.sleep(1)
#Payment Method
payment_comment = driver.find_element(By.XPATH, '//*[@id="collapse-payment-method"]//textarea')
payment_comment.clear()
payment_comment.send_keys("Do you accept credit cards?")
#Terms and Condition
tc = driver.find_element(By.XPATH, '//input[@name="agree"]')
tc.click()
#Continue
continue_button3 = driver.find_element(By.XPATH,'//input[@id="button-payment-method"]')
continue_button3.click()
time.sleep(1)

driver.find_element(By.XPATH, '//input[@id="button-confirm"]').click()

time.sleep(1)
driver.find_element(By.XPATH,'//a[text()="Continue"]').click()


