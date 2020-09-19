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

    # Visit the mars nasa news site
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)

    # Convert the browser html to a soup object
    html=broswer.html
    soup=BeautifulSoup(html, "html.parser")

    #Collect the latest News Title
    news_title=soup.find('li', class_='slide').find('div',class_='content_title').text

    #Collect the latest Paragraph Text
    news_p=soup.find('li', class_='slide').find('div', class_="article_teaser_body").text

    # Visit the url for JPL Featured Space Image
    image_url='https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    time.sleep(.1)

    # Navigate site and save full size url string of image to variable

    # Click "Full Image" button on page
    browser.click_link_by_partial_text("FULL IMAGE")

    # Click "More Info" button to get to full size image
    browser.click_link_by_partial_text("more info")

    html = browser.html
    soup = bs(html, "html.parser")

    # Scrape for full image 
    base_url="https://www.jpl.nasa.gov"
    img_url = soup.find('figure', class_='lede').find('a').find('img')['src']

    #add image url to base url
    featured_image_url=base_url + img_url

    #Mars Facts
    # Have pandas read any tables on mars facts page
    facts_url = 'https://space-facts.com/mars/'

    fact_table = pd.read_html(facts_url

    # Filter to table I want to work with
    fact_df = fact_table[0]

    # Rename columns
    fact_df.columns = ["Description", "Mars"]

    # Remove Index/set new
    facts = fact_df.set_index("Description")

    # Convert to html string & clean
    html_fact = facts.to_html()
    html_fact = html_fact.replace('\n', '')

    ##Mars Hemispheres
    # Define and retrieve the page
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hemisphere_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    # Blank list to contain the dictionaries
    hemisphere_image_urls = []

    # Base image url
    baseimg_url="https://astrogeology.usgs.gov/"

    # Soup object
    hemisheres = soup.find_all('div', class_='item')

    # Loop to get each title & url
    for hemi in hemisheres:
        title = hemi.find('h3').text
        
        browser.click_link_by_partial_text("Hemisphere Enhanced")
        img_html = browser.html
        img_soup = bs(img_html, "html.parser")
        imgs_url = img_soup.find("img", class_="wide-image")["src"]
        
        image_url = baseimg_url+imgs_url
        hemisphere_image_urls.append({"title": title, "img_url": image_url})