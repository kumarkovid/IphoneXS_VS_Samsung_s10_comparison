#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import inquirer
import time 
import pandas as pd


# In[23]:


import time 
from selenium.webdriver.common.keys import Keys

URL = input ("Please input the Youtube URL here: ")

brand = (input ("Please input the brand name ('apple','samsung','oneplus', 'google'): ")).strip()
model = (input ("Please input the model name ('xs', 's10', '6t', '3') etc: ")).strip()

gecko_path = '/Users/divyaj_podar/Downloads/geckodriver 2'

executable_path = gecko_path

driver = webdriver.Firefox(executable_path =  executable_path)

driver.get(URL)

body = driver.find_element_by_css_selector('body')
body.send_keys(Keys.PAGE_DOWN)

time.sleep(3)
     

# Scraping the youtuber's channel name
channel_name = driver.find_element_by_css_selector("yt-formatted-string#owner-name.style-scope.ytd-video-owner-renderer a").text
channel_name = channel_name.replace(' ', '_')

#Scraping the number of likes on the video
views = driver.find_element_by_css_selector('span.view-count.style-scope.yt-view-count-renderer').text

views = views.replace (" views","")

#Scraping the published date of the video
published_date = driver.find_element_by_css_selector('span.date.style-scope.ytd-video-secondary-info-renderer').text

published_date = published_date.replace("Published on " , "")


#Scraping the number of likes and dislikes on the video 
like_dislike = driver.find_elements_by_css_selector("yt-formatted-string#text.style-scope.ytd-toggle-button-renderer.style-text")

#converting the data to integers format

likes = like_dislike[0].text


if likes[-1] == 'K':
    likes = likes[:-1]
    likes = int(float(likes)*1000)
elif likes[-1] == 'M':
    likes = likes[:-1]
    likes = int(float(likes)*1000000)

dislikes = like_dislike[1].text

if dislikes[-1] == 'K':
    dislikes = dislikes[:-1]
    dislikes = int(float(dislikes)*1000)
elif dislikes[-1] == 'M':
    dislikes = dislikes[:-1]
    dislikes = int(float(dislikes)*1000000)
    
#getting the unique code 
video_code = URL.split("=")[1][:12].strip()
if video_code[-1] == '&':
    video_code = video_code[:-1]

#importing the other data set scraped using online scraper
    
df2 = pd.read_csv('/Users/divyaj_podar/Desktop/Scraped_data/comments-' + video_code + '.csv')

data = [channel_name, brand, model, URL, published_date, views, likes, dislikes]

new_data = []

for i in range(len(df2)):
    new_data.append(data)

df1 = pd.DataFrame (new_data, columns = ['Channel Name', 'Brand', 'Model', 'URL', 'Published_date', 'Views', 'Likes', 'Dislikes'])


#joining the data collected from online as well as this scraper 

df3 = pd.concat([df1,df2], axis = 1, sort = False)

print (df3)

#saving the file in csv format
df3.to_csv('/Users/divyaj_podar/Desktop/URL_all_data/'+ video_code + '.csv', header=True, index=False)


# In[ ]:





# In[ ]:




