from fastapi import FastAPI
import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    wait = WebDriverWait(driver, 10)

    try:
        print("Navigating to Facebook...")
        driver.get("https://www.facebook.com/?_rdr")

        print("Opening registration form...")
        create_account_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Create new account"]')
            )
        )
        create_account_button.click()

        print("Clicking 'Get started' button...")
        get_started_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Get started"]'))
        )
        get_started_button.click()

        print("Filling out the form...")
        first_name_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@aria-label="First name"]')
            )
        )
        first_name_input.send_keys(first_name)

        last_name_input = driver.find_element(
            By.XPATH, '//input[@aria-label="Last name"]'
        )
        last_name_input.send_keys(last_name)

        print("Clicking 'Next' button...")
        next_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        next_button.click()

        print("Entering birthdate...")
        birthdate_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@aria-label="Birthday (2022 years old)"]')
            )
        )
        birthdate = f"{random.randint(1980, 2000)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
        birthdate_input.send_keys(birthdate)

        print("Clicking 'Next' button again...")
        next_button_final = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@role="button" and @aria-label="Next"]')
            )
        )
        next_button_final.click()

        print("Selecting gender option...")
        gender_option = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//span[text()="Select More options to choose another gender or if you\'d rather not say."]',
                )
            )
        )
        gender_option.click()

        print("Clicking 'Sign up with email' button...")
        sign_up_with_email_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Sign up with email"]')
            )
        )
        sign_up_with_email_button.click()

        print("Entering email...")
        email_input = wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Email"]'))
        )
        email_input.send_keys(email)

        print("Clicking 'Next' button...")
        next_button_after_email = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        next_button_after_email.click()

        print("Entering password...")
        password_input = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@aria-label="Password"]')
            )
        )
        password_input.send_keys(password)

        print("Clicking 'Next' button...")
        next_button_after_password = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
        )
        next_button_after_password.click()

        print("Clicking 'Save' button...")
        save_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Save"]'))
        )
        save_button.click()

        print("Clicking 'I agree' button...")
        agree_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="I agree"]'))
        )
        agree_button.click()

        print(
            "Neet confirmation code from mail"
        )  # TODO: add script to handle code from mail to enter here

        save_account_details(first_name, last_name, email, birthdate)

    except Exception as e:
        print(f"Error during Facebook interaction: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    register_account()
