#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import inquirer
import time 
import pandas as pd


# In[4]:


import time 
from selenium.webdriver.common.keys import Keys

URL = input ("Please input the Youtube URL here: ")

brand = input ("Please input the brand name: ('apple','samsung','oneplus', 'google')")
model = input ("Please input the model name: ('xs', 's10', '6t', '3') etc")

gecko_path = '/Users/divyaj_podar/Downloads/geckodriver 2'

executable_path = gecko_path

driver = webdriver.Firefox(executable_path =  executable_path)

driver.get(URL)

src_updated = driver.page_source
src = ""

while src != src_updated: 
    
    src = src_updated
    
    
    body = driver.find_element_by_css_selector('body')

    # Simulate page down
    body.send_keys(Keys.PAGE_DOWN)
    
    time.sleep(2)
    
    src_updated = driver.page_source
    
#Scraping the youtuber's channel name
channel_name = driver.find_element_by_css_selector("yt-formatted-string#owner-name.style-scope.ytd-video-owner-renderer a").text
channel_name = channel_name.replace(' ', '_')
#Scraping the number of likes on the video
views = driver.find_element_by_css_selector('span.view-count.style-scope.yt-view-count-renderer').text

views = views.replace (" views","")

#Scraping the number of subscribers 
#subscribers = driver.find_elements_by_css_selector('yt-formatted-string.style-scope.ytd-subscribe-button-renderer span')

#Scraping the published date of the video
published_date = driver.find_element_by_css_selector('span.date.style-scope.ytd-video-secondary-info-renderer').text

published_date = published_date.replace("Published on " , "")


#Scraping the number of likes and dislikes on the video 
like_dislike = driver.find_elements_by_css_selector("yt-formatted-string#text.style-scope.ytd-toggle-button-renderer.style-text")

likes = like_dislike[0].text
dislikes = like_dislike[1].text

print ('likes = ', likes)
print ('dislikes = ', dislikes)
    
data = []

#Scraping the information on the comments 
comments = driver.find_elements_by_css_selector("yt-formatted-string#content-text.style-scope.ytd-comment-renderer")

comment_likes = driver.find_elements_by_css_selector("span#vote-count-middle.style-scope.ytd-comment-action-buttons-renderer")

print ("total comments: ", len(comments))


for idx in range(len(comments)):
    a = comments[idx].text
    b = comment_likes[idx].text
    
    data.append((channel_name,brand,model,URL,published_date,views,likes,dislikes,a,b))

df = pd.DataFrame(data, columns = ['Channel Name', 'Brand', 'Model', 'URL', 'Published_date', 'Views', 'Likes', 'Dislikes', 'Comment', 'Comment_likes']) 

print (df)

#df.to_csv(channel_name+'_'+brand+'_'+model+'.csv', header=True, index=True)


    


# In[ ]:




