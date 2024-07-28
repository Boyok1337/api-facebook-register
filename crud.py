from fastapi import FastAPI
import csv
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from fake_useragent import UserAgent
from dotenv import load_dotenv
import os
from email_generator import get_temp_email
from utils import first_name, last_name

load_dotenv()

password = os.getenv("PASSWORD")

app = FastAPI()


def save_account_details(first_name, last_name, email, birthdate):
    with open("accounts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([first_name, last_name, email, birthdate])


def register_account():
    ua = UserAgent()
    headers = {"User-Agent": ua.random}

    email = get_temp_email()
    print(f"Received temporary email: {email}")

    if not email:
        print("Failed to get temporary email.")
        return

    firefox_options = Options()
    firefox_options.add_argument("--ignore-certificate-errors")
    firefox_options.set_preference("general.useragent.override", headers["User-Agent"])

    driver = webdriver.Firefox(options=firefox_options)

    try:
        print("Navigating to Facebook...")
        driver.get(
            "https://www.facebook.com/?_rdr"
        )  # TODO: need to handle different facebook interface
        time.sleep(5)

        print("Opening registration form...")
        driver.find_element(
            By.XPATH, '//a[@data-testid="open-registration-form-button"]'
        ).click()
        time.sleep(random.uniform(1, 3))

        print("Filling out the form...")
        driver.find_element(By.NAME, "firstname").send_keys(first_name)
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.NAME, "lastname").send_keys(last_name)
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.NAME, "reg_email__").send_keys(email)
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.NAME, "reg_email_confirmation__").send_keys(email)
        time.sleep(random.uniform(1, 3))
        driver.find_element(By.NAME, "reg_passwd__").send_keys(password)
        time.sleep(random.uniform(1, 3))

        day = random.randint(1, 28)
        day_select = Select(driver.find_element(By.NAME, "birthday_day"))
        day_select.select_by_value(str(day))
        time.sleep(random.uniform(1, 3))

        month = random.randint(1, 12)
        month_select = Select(driver.find_element(By.NAME, "birthday_month"))
        month_select.select_by_value(str(month))
        time.sleep(random.uniform(1, 3))

        year = random.randint(1980, 2000)
        year_select = Select(driver.find_element(By.NAME, "birthday_year"))
        year_select.select_by_value(str(year))
        time.sleep(random.uniform(1, 3))

        driver.find_element(By.XPATH, f'//input[@name="sex" and @value="-1"]').click()
        time.sleep(random.uniform(1, 3))

        pronoun_select = Select(driver.find_element(By.NAME, "preferred_pronoun"))
        pronoun_select.select_by_value("6")

        print("Submitting the form...")
        driver.find_element(By.NAME, "websubmit").click()
        time.sleep(5)

        save_account_details(first_name, last_name, email, f"{day}/{month}/{year}")

    except Exception as e:
        print(f"Error during Facebook interaction: {e}")

    finally:
        driver.quit()
