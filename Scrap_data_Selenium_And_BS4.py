from bs4 import BeautifulSoup
from selenium import webdriver
import re
import pandas as pd
from pathlib import Path
PATH="C:\Program Files (x86)\chromedriver.exe"
url = 'https://www.youtube.com/channel/UCzSeVpD8AKKyWRz1HtW0kkw/videos'
browser = webdriver.Chrome(PATH)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
titles = []
mylist1 = []
views = []
date = []
listall = []
dates = []
href = []
hrefs = []
title_list = soup.find_all("ytd-grid-video-renderer",attrs={"class":"style-scope ytd-grid-renderer"})
for x in title_list:
    all_titles = x.find("a",attrs={"class":"yt-simple-endpoint style-scope ytd-grid-video-renderer"})
    titles.append(all_titles.text)
    hrefs_all = x.find("a",attrs={"class":"yt-simple-endpoint inline-block style-scope ytd-thumbnail"})['href']
    hrefs.append(hrefs_all)
views_list = soup.find_all("div",attrs={"id":"metadata-line"})
for y in views_list:
    all_dates = y
    date.append(all_dates.text)
for i in range(len(date)):
    new = re.sub("views","%",date[i])
    listall.append(new.split('%'))
for i in range(len(listall)):
    views.append(listall[i][0])
    dates.append(listall[i][1])
for x in hrefs:
    href.append("https://www.youtube.com/"+x)
print("This is our data:")
print(titles)
print(views)
print(dates)
print(href)
