from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
 


def get_videos(title):
    name = title.replace(" ", "+")
    driver.get("https://www.youtube.com/results?search_query={}".format(name))

    links_elements = driver.find_elements(By.TAG_NAME, "a")
    videos = []
    for link in links_elements:
        href_text = link.get_attribute("href")
        try:
            if "https://www.youtube.com/watch?v=" in href_text:
                videos.append(href_text)
        except TypeError:
            pass
    return videos