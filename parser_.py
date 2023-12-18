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
    for i in range(1, 11, 1):
        page_ref = 'p=' + str(i) + '&s=104'
#        URL = URL.replace('s=104', page_ref)
        pars_elements(page_ref)
    return print('COMPLETE')
def pars_elements(page_ref):
    driver = webdriver.Edge("Z:\\!GIT\\home_searcher_bot\\msedgedriver.exe")

    driver.minimize_window()
    URL.replace('s=104', page_ref)
    driver.get(URL)
    print(URL)

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
#        print(merge)
        add_row(merge)

    return driver.close()

#run_parser()