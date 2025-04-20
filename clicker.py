from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://orteil.dashnet.org/cookieclicker/')

WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
).click()
driver.maximize_window()

#Scrolls the Right Div Section
r_scroll = driver.find_element(By.ID, 'sectionRight')
driver.execute_script("arguments[0].scrollTop +=200;", r_scroll)

#clicks Cookie Infinitely
while True:
    driver.find_element(By.ID, 'bigCookie').click()

    total = driver.find_element(By.ID, 'cookies').text.split()[0]
    total = int(total.replace(",", ""))

    for i in range(4):
        element_id = f"productPrice{i}"
        product_id = f"product{i}"
        try:
            product_price = driver.find_element(By.ID, element_id).text.replace(",", "")
            product_price = int(product_price)
            if total >= product_price:
                driver.find_element(By.ID, product_id).click()
                break
        except:
            print(f"[!] Element with ID '{element_id}' not found or not ready.")
            continue

