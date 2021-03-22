import requests #Requests ライブラリを使うとWebサイトの情報取得や画像の収集などを簡単に行うことができます。Python には標準で urllib というライブラリが存在しますが、 Requests はそれよりもシンプルに、人が見て分かりやすくプログラムを記述することができます。
from selenium import webdriver #動的サイトなどを動かすためのライブラリ,人間が動かしているのと同様な動きができるがその分重く,webを動かすための格webごとのdriverをダウンロードする必要がある。
from time import sleep #pythonに元々存在するライブラリ,時間関係に使用する。
from bs4 import BeautifulSoup    # bs4というパッケージを使いbeautiful soupを使用する
from urllib.parse import urljoin  #pythonに元々存在するurlを開くためのモジュール
import csv #pythonに既存に存在するcsvファイルを編集するためのモジュール

csv_file_name = "syllabus.csv"
f = open(csv_file_name, 'w', encoding='cp932', errors='ignore')
writer = csv.writer(f, lineterminator='\n') 
csv_header = ["0","授業タイトル","学部","科目ソート","科目名","分野","単位","学期","学期","時限","教員名","実施体型","言語","開講場所","授業形態","GIGA","授業詳細"]
writer.writerow(csv_header)


driver = webdriver.Chrome('クロームのwebdriver')
driver.get('シラバスサイト')
title = driver. find_element_by_name ("search[title]")
title.send_keys("")
sleep(5)
title.submit()
i=0
a=1
def find_url():
     syllabus_info_url = driver.find_elements_by_xpath('//li/div/a[@class="detail-btn"]')
     url_list = []
     for urls in syllabus_info_url:
      url_list.append(urls.get_attribute('href'))
     print(url_list)
     return url_list


while i<15:
 url_list = find_url()
 i=i+1
 if url_list :
    for to_urls in url_list :
        sleep(5)
        driver.get(to_urls)
        csvlist = []
        csvlist.append(str(a))
        subtitle = driver.find_element_by_class_name("title")
        detail_info = driver.find_element_by_xpath('//dl[@class="detail-info"]/dd/p')
        csvlist.append(subtitle.text)
        row_list = driver.find_elements_by_xpath('//dl[@class="row"]/dd') #elementでは単数しか取れない,elements
        for dd_list in row_list:
         print(dd_list.text)
         csvlist.append(dd_list.text)
        csvlist.append(detail_info.text)
        writer.writerow(csvlist)
        a=a+1
        sleep(5)
        driver.back()
 #次のリンクに移動
    next_link = driver.find_element_by_xpath("//span/a")
    print(next_link.get_attribute('href'))
    driver.get(next_link.get_attribute('href'))
 else :
 #次のリンクに移動
  sleep(5)
  next_link = driver.find_element_by_xpath('//span[@class="next"]/a')
  print(next_link.get_attribute('href'))
  driver.get(next_link.get_attribute('href'))




#syllabus_info_url.click()
driver.close()

