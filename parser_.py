from selenium import webdriver
from config import URL
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dbase import add_row

to_db_title = str
to_db_cost = str
to_db_url = str
def run_parser():
    driver = webdriver.Edge("Z:\\!GIT\\home_searcher_simple_bot\\msedgedriver.exe")

    driver.minimize_window()
    driver.get(URL)

    # ToDo переключение страницы и выполнение тех же инструкций

    # блок с объявлениями
    app = driver.find_element(By.XPATH, "//*[contains(@class,'items-items-')]")

    # ToDo поиск года постройки, времени публикации

    ref_list = app.find_elements(By.XPATH, "//div[contains(@class,'iva-item-root')]")

    for ref in ref_list:
        title = ref.find_element(By.XPATH, ".//a")
        cost = ref.find_element(By.XPATH, ".//div/div/div[2]/div[3]/span/div/p/meta[2]")

        to_db_title = str(title.get_attribute('title')).replace('"', '')
        to_db_cost = str(cost.get_attribute('content'))
        to_db_url = str(title.get_attribute('href'))
        merge = to_db_cost + ",'" + to_db_title + "','" + to_db_url + "'"
        print(merge)
        add_row(merge)

    return driver.close()

#run_parser()
