from django.shortcuts import render
from selenium import webdriver

import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv
import os

load_dotenv()
# Configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
)


def take_screenshot(url):
    """Function to take a screenshot of the website"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)

    browser.get(url)

    total_height = browser.execute_script(
        "return document.body.parentNode.scrollHeight")
    browser.set_window_size(1200, total_height)
    screenshot = browser.get_screenshot_as_png()
    browser.quit()

    sanitized_url = url.replace(
        "http://", "").replace(
        "https://", "").replace(
        "/", "_").replace(":", "_")

    upload_response = cloudinary.uploader.upload(
        screenshot,
        folder="screenshots",
        public_id=f"{sanitized_url}.png",
        resource_type="image"
    )

    return upload_response["url"]


def index(request):
    take_screenshot("https://github.com/prakharpratap20/website-review")
    return render(request, "index.html")
