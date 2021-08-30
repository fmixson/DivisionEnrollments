from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd



class TableWork:

    def __init__(self, html_table):
        self.html_table = html_table
        # print(self.table)

    def extract_row(self):
        row = self.html_table.find('tr', {'bgcolor':'lightgrey'})
        print('row', row)
        print('==========Text Result============')
        print('row text', row.get_text())
        print()
        print()


driver = webdriver.Chrome("C:/Users/fmixson/PycharmProjects/chromedriver.exe")
driver.get('https://secure.cerritos.edu/schedule/')
check_all = driver.find_element_by_xpath('/html/body/form/table/tbody/tr[1]/td[1]/label/input').click()
check_LA = driver.find_element_by_xpath('/html/body/form/b/b/table[4]/tbody/tr[5]/td[2]/label/input').click()
click_View = driver.find_element_by_xpath('/html/body/form/b/b/p[2]/input').click()
page_loading = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ASL110descs')))

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
# div_table = soup.find_all('div', {'name': 'desc'}).decompose()
# print(div_table)
tables = soup.find_all(['table', {'cellspacing': '0', 'class': 'class'}])
count = 0
for table in tables:
    t = TableWork(html_table=table)
    t.extract_row()


