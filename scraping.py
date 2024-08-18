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
    hrefs = [link.get_attribute("href") for link in links_elements if link.get_attribute("href")]

    videos = []
    videos_titles = []
    for href_text in list(set(hrefs)):
        
        url_format = "https://www.youtube.com/watch?v="
        try:
            if url_format in href_text and href_text not in videos_titles:
                videos_titles.append(href_text)
                videos.append(href_text)
                print(videos_titles)
                #driver.get(href_text)
                print(driver.title)
        except TypeError:
            pass
    
    return videos
