#!/usr/bin/env python
# coding: utf-8

# In[5]:
print("hello")


import os
import sys
import time
#import tweepy
import chromedriver_binary 
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# In[20]:


#word = os.environ("test")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options = options
)
word = os.environ["test"]
def demo():
    driver.get(word)
demo()


# In[17]:
