from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_initbrowser():
    s=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=s)
    driver.get("http://www.fb.com")
    driver.maximize_window()
    driver.implicitly_wait(30)
    actual_title=driver.title
    assert actual_title=="Facebook – log in or sign up"
    driver.close()
