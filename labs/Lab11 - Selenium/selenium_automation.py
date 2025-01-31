from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.amazon.com')

driver.maximize_window()

# enter product name to the seachbar
search_bar = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.ID, 'twotabsearchtextbox'))
)
search_bar.send_keys('Laptop')
search_bar.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.s-main-slot .s-result-item'))
)


try:
    product_name = driver.find_element(By.XPATH, '/html/body//div[@class="product"]/h1').text
    print("Product Title:", product_name )

    product_url = driver.current_url
    print("URL:", product_url)

    try:
        product_rating = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]/div/div/div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/span[1]/a/i[1]').text
        print("Rating:", product_rating)
    except:
        print("Product Rating: Not available")

except Exception as e:
    print(f"Error extracting product details: {e}")

driver.save_screenshot('product_page.png')
print("Screenshot is successfully added")

time.sleep(5)

driver.quit()
