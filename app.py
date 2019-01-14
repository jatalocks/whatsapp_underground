from selenium import webdriver
import time
from git import Repo
import datetime



repo_dir = '.'
repo = Repo(repo_dir)
file_list = [
    'screenshot.png'
]




checkIn2 = """ return document.getElementsByTagName("BODY")[0].innerHTML.includes("Keep your phone connected") """
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
state = 1
while (True):
    if state == 1:
        if driver.execute_script(checkIn2):
            screenshot = driver.save_screenshot('screenshot.png')
            commit_message = 'Updated' + datetime.datetime.now()
            repo.index.add(file_list)
            repo.index.commit(commit_message)
            origin = repo.remote('origin')
            origin.push()
            time.sleep(10)
    else:
        time.sleep(0.5)
            






