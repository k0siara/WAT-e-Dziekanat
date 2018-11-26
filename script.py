from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
import sys
import os

def enable_download_in_headless_chrome(driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

def get_login_data(filename):
    with open(filename, "r") as f:
        username = f.readline().replace("\n","").replace("\r","").split("=")[1]
        password = f.readline().replace("\n","").replace("\r","").split("=")[1]

    if not username:
        print("\nBrak nazwy użytownika w pliku", filename)
        exit(None)

    if not password:
        print("\nBrak hasła w pliku", filename)
        exit(None)

    return username, password


def login(driver, username, password):
    try :
        driver.get("https://s1.wcy.wat.edu.pl/ed")
    except TimeoutException as e:
        print("Nie udało się załadować strony e-dziekanatu, spróbuj ponownie później")
        exit(driver)

    driver.find_element_by_name("userid").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_class_name("inputLogL").click()

    if "logged_in" in driver.current_url:
        print("\nZalogowano pomyślnie")
    else:
        print("\nBłąd logowania, spróbuj ponownie później")
        exit(driver)

def open_schedule(driver, group):
    url = driver.current_url + "&mid=328&iid=20184&exv=" + group + "&pos=0&rdo=1"
    driver.get(url)

    try:
        myElem = WebDriverWait(driver, timeout = 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'trObj1SheTeaGrpHTM')))
    except TimeoutException:
        print("Nie udało się załadować planu lekcji, spróbuj ponownie później")
        exit(driver)

def download_schedule(driver):
    url = driver.current_url + "&opr=DTXT"
    driver.get(url)

    sleep(3);

def exit(driver):
    print()

    if not (driver is None):
        driver.quit()

    sys.exit()

def main():
    print (r"""    
  _       _____  ______   ____        _      __                     __ 
 | |     / /   |/_  __/  / __ \____  (_)__  / /______ _____  ____ _/ /_
 | | /| / / /| | / /    / / / /_  / / / _ \/ //_/ __ `/ __ \/ __ `/ __/
 | |/ |/ / ___ |/ /    / /_/ / / /_/ /  __/ ,< / /_/ / / / / /_/ / /_  
 |__/|__/_/  |_/_/    /_____/ /___/_/\___/_/|_|\__,_/_/ /_/\__,_/\__/""", end = "\n\n")

    current_dir = os.path.dirname(os.path.realpath(__file__))

    filename = "login_data.txt"
    username, password = get_login_data(os.path.join(current_dir, filename))
    
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1024x1400")

    chrome_driver = os.path.join(current_dir, "chromedriver.exe")
    if not os.path.isfile(chrome_driver):
        print("\nBrak sterownika chromedriver, pobierz z https://sites.google.com/a/chromium.org/chromedriver/downloads")
        exit(None)

    driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
    enable_download_in_headless_chrome(driver, current_dir)
    driver.set_page_load_timeout(10)

    login(driver, username, password)
    open_schedule(driver, "I7Y4S1")
    download_schedule(driver)
    
    exit(driver)


if __name__ == '__main__' : main()