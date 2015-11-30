from selenium import webdriver

browser = webdriver.Chrome("/Users/fedorovegor/Documents/Python_TDD/chromedriver")
browser.get("http://localhost:8000")

assert "Django" in browser.title
