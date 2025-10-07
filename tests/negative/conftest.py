import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from dotenv import load_dotenv
import os

load_dotenv()  # loads .env into environment variables


@pytest.fixture
def driver():
    chrome_options = Options()
    # ✅ Uncomment this if you want headless mode for CI/CD
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get("https://demoblaze.com")
    yield driver
    driver.quit()