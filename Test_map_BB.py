# import pytest, requests, json
import time

import requests, allure
from allure_commons.types import AttachmentType
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMapSearch:
    #Настройки тест кейса
    def setup(self):
        self.chrome = webdriver.Chrome()
        self.safari = webdriver.Safari()
        self.firefox = webdriver.Firefox()
        self.url = 'https://boxberry.ru/find_an_office'

    #"Убиваем" процессы
    def teardown(self):
        self.chrome.quit()
        self.safari.quit()
        self.firefox.quit()

    """Декораторы allure
    1. Заголовок функции
    2. Заголовок шага
    3. Важность"""

    @allure.feature('Поиск карты на странице')
    @allure.story("Браузер Safari")
    @allure.severity("Major")
    def test_find_map_safari(self):
        browser = self.safari
        browser.get(self.url)
        maps = browser.find_elements(By.CLASS_NAME, 'points-find-map')
        time.sleep(3)
        with allure.step('Скриншот страницы'):
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert requests.get(self.url).status_code == 200, "Page not found"
        assert len(maps) != 0

    @allure.feature('Поиск карты на странице')
    @allure.story("Браузер Chrome")
    @allure.severity("Major")
    def test_find_map_chrome(self):
        browser = self.chrome
        browser.get(self.url)
        maps = browser.find_elements(By.CLASS_NAME, 'points-find-map')
        time.sleep(3)
        with allure.step('Скриншот страницы'):
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert requests.get(self.url).status_code == 200, "Page not found"
        assert len(maps) != 0

    @allure.feature('Поиск карты на странице')
    @allure.story("Браузер Firefox")
    @allure.severity('Minor')

    def test_find_map_firefox(self):
        browser = self.firefox
        browser.get(self.url)
        maps = browser.find_elements(By.CLASS_NAME, 'points-find-map')
        time.sleep(3)
        with allure.step('Скриншот страницы'):
            allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        assert requests.get(self.url).status_code == 200, "Page not found"
        assert len(maps) != 0, "MAP NOT FOUND"
