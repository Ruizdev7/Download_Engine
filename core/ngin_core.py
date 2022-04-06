'''
#!/usr/bin/env Python 3.9.10
# -*- coding: utf-8 -*-
'''

''' 
Created By  : Joseph Ruiz
GitHub https://github.com/Ruizdev7
LinkedIn https://www.linkedin.com/in/ruizdev7/
Email jgalindo@plena.global
Created Date: 2022/03/16
version ='1.0'
---------------------------------------------------------------------------
SUMMARY MODULE
this module creates routines to automate the download of reports from the MJ Freeway analysis module using Selenium 4, 
and their post processing in order to feed POSTMAN
---------------------------------------------------------------------------
'''

#Importing the necessary modules
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Base_Generator():
    options = Options()
    options.add_argument('start-maximized')
    service = Service(executable_path='/home/ruizdev7/GitHub/Download_Engine/core/msedgedriver.exe')
    driver = webdriver.Edge(service=service, options=options)
    
    
    def __init__(self, analyticSection):
        self.sectionName = analyticSection
        

class Report_Generator(Base_Generator):
    
    def __init__(self, analyticSection):
        super().__init__(analyticSection)
        
    
    def logIn(self):
        
        driver = self.driver
        driver.get('https://app.mjplatform.com/login')
        driver.find_element_by_id('name').send_keys('jgalindo_pro')
        driver.find_element_by_id('password').send_keys('C9p5au8naa*')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/form/div[3]/button').click()
        
        
    def locateAnalyticsModule(self):
        
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="right-side-content"]/div/div/div/button[2]/address').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="right-side-content"]/div/div/div[2]/div[12]/div[2]/div[2]/a/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="filterTabs-tab-favorites"]').click()
        
        
    def downloadHarvestBatchDetails(self):
        
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="right-side-content"]/div/a[1]/span').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="container2"]/div/div[2]/pg-layout-frame/cmppkuwluodug/div/div/pg-layout-populated-frame/cmpcdwvy40cna/div/div[1]/section/cd-control-menu/div/button').click()
        
        
    def __rep__(self):
        return f"sectionName:{self.sectionName}"
    