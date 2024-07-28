from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def get_temp_email():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get("https://tempail.com/")
        time.sleep(15)  # CAPTCHA

        copy_button = driver.find_element(By.CSS_SELECTOR, "a.kopyala-link")
        copy_button.click()

        email_element = driver.find_element(By.ID, "eposta_adres")
        email = email_element.get_attribute("value")
    except Exception as e:
        print(f"Error fetching email: {e}")
        email = None
    finally:
        driver.quit()

    return email
