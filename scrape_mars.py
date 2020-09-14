from splinter import Browser
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import pandas as pd

def init_browser():
    executable_path={"execuatable_path":'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser=init_browser()
    mars_web={}
    hemisphere_image_urls=[]

    url=
    browser.visit(url)

    html=broswer.html
    soup=BeautifulSoup(html, "html.parser")

    


