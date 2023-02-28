from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from time import sleep, time
import json

def createStore(storename,coordinate,storeaddress,storetel,storehour):
    return{
        'storename':storename,
        'coordinate':coordinate,
        'storeaddress':storeaddress,
        'storetel':storetel,
        'storehour':storehour
    }


dataset=[]

options=Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless') #模擬器不會彈出


driver=webdriver.Chrome(chrome_options=options)
driver.get('https://www.starbucks.com.tw/stores/storesearch.jspx')
selectCity=Select(driver.find_element_by_id('selCity'))
selectCity.select_by_visible_text('台南市')
sleep(1)
selectRegion=Select(driver.find_element_by_id('selRegion'))
selectRegion.select_by_visible_text('東區')
searchButtom=driver.find_element_by_id('sbForm:doFindByRegion')
searchButtom.click()
sleep(2)
all_results_in_region=driver.find_element_by_id('search_store').find_elements_by_tag_name('li')
print(all_results_in_region)
for result in all_results_in_region:
    storename=result.find_element_by_class_name('cn').text 
    hiddentext=result.find_elements_by_tag_name('span') 
    xy=hiddentext[1]
    coordinate_text=driver.execute_script('return arguments[0].textContent',xy)  #經緯度座標
    storeaddress=storetel=result.find_element_by_class_name('address').text
    storetel=result.find_element_by_class_name('tel').text
    storehour=result.find_element_by_class_name('hours').text
    print(storename) 
    print(coordinate_text)
    print(storeaddress)
    print(storetel)
    print(storehour)
    storeinfo=createStore(storename,coordinate_text,storeaddress,storetel,storehour)
    dataset.append(storeinfo)
'''
fi=open('apple.txt','w',encoding='utf-8') 
fi.colse()
'''
with open('starbucks_east_storeinfo.json','w',encoding='utf-8') as datafile:
    json.dump(dataset,datafile,indent=4,ensure_ascii=False)