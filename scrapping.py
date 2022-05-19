from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings('ignore')


website = "https://www.bancolombia.com/personas/productos-servicios/inversiones/fondos-inversion-colectiva/aplicacion-fondos"
path = "/Users/melvinmol/Python/chromedriver" 



driver = webdriver.Chrome(path)
driver.get(website)


#Variables declaration
profit_007 = []
profit_030 = []
profit_180 = []
profit_ytd = []
profit_l1y = []
profit_l2y = []
profit_l3y = []



dropdown_list = driver.find_element_by_name("nmSelectFondo")
option_list = dropdown_list.find_elements_by_tag_name("option")
option_elements = []
for el in option_list:
    option_elements.append(el.get_attribute("value"))



#option_elements = ['0', '1']


def get_profit(lst):
    profit_007.append(list_profit[17])
    profit_030.append(list_profit[18])
    profit_180.append(list_profit[19])
    profit_ytd.append(list_profit[25])
    profit_l1y.append(list_profit[26])
    profit_l2y.append(list_profit[27])
    profit_l3y.append(list_profit[28])
    return profit_007, profit_030, profit_180, profit_ytd, profit_l1y, profit_l2y, profit_l3y

list_element = Select(driver.find_element_by_name("nmSelectFondo"))
for op in option_elements:
    visible_name = list_element.select_by_value(op)
    time.sleep(3)
    profit_info = driver.find_elements_by_class_name("ng-binding")
    list_profit = []
    for el in profit_info:
        list_profit.append(el.get_attribute("innerHTML"))
    get_profit(list_profit)
    

print(profit_007)
print(profit_030)
driver.quit()