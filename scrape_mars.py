
# coding: utf-8

# In[24]:


from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import requests


# In[36]:


def scrape_all():

    # Initiate headless driver for deployment
browser = Browser("chrome", executable_path="chromedriver.exe", headless=True)
#news_title, news_paragraph = mars_news(browser)
browser.visit("https://mars.nasa.gov/news/")

    
soup = BeautifulSoup(browser.html, 'html.parser')
#print(soup.prettify)
results = soup.find("div", class_="content_title").get_text()
print(results)
    # Stop webdriver and return data
    #browser.quit()
    # return data


# In[26]:


def featured_image(browser):

    # Find and click the full image button
    browser = Browser("chrome", executable_path="chromedriver.exe", headless=True)

    try:
       pass

    except AttributeError:
        pass

    # Use the base url to create an absolute url
   

    # return img_url


# In[27]:


def hemispheres(browser):


    browser.visit(url)

    # Click the link, find the sample anchor, return the href
   
        # Finally, we navigate backwards
    browser.back()

    # return hemisphere_image_urls



# In[37]:


def twitter_weather(browser):
    browser = Browser("chrome", executable_path="chromedriver.exe", headless=True)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit("url")
    soup = BeautifulSoup(browser.html, 'html.parser')
    # return mars_weather
    results = soup.find("div", class_="tweet")
    print("results")


# In[29]:


soup.prettify


# In[7]:


def scrape_hemisphere(html_text):

    # Soupify the html text
    
    # Try to get href and text except if error.
    try:
        pass

    except AttributeError:
        pass


    # return hemisphere



# In[ ]:


def mars_facts():

    try:
        pass
    except BaseException:
        pass
       
    # Add some bootstrap styling to <table>
    # return df


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())