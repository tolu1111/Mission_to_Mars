
from splinter import Browser
# from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import requests
import pandas as pd
from pprint import pprint
# from datetime import datetime as dt



def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL for scraping
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Create Beautiful Soup object with html parser
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')


    # Scrape the latest news article title
    news_title = mars_news_soup.find('div', class_='content_title').text
    news_title

    # Scrape the latest news paragraph
    news_paragraph = mars_news_soup.find('div', class_='article_teaser_body').text
    news_paragraph


    # URL for scraping
    url_2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_2)


    # Go to 'FULL IMAGE'
    browser.click_link_by_partial_text('FULL IMAGE')


    # Go to 'more info'
    browser.click_link_by_partial_text('more info')

    # Create BeautifulSoup object with html parser
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')


    # Scrape the URL
    featured_image_url = image_soup.find('figure', class_='lede').a['href']
    featured_image_full_url = f'https://www.jpl.nasa.gov{featured_image_url}'
    featured_image_full_url




    # URL for scraping
    url_3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url_3)


    # Create Beautiful Soup object with html parser
    html = browser.html
    mars_weather_tweet_soup = BeautifulSoup(html, 'html.parser')


    # Scrape the mars weather tweet info
    tweet = mars_weather_tweet_soup.find('p', class_='TweetTextSize').text
    tweet


    # Scrape Mars facts and read into a dataframe
    url_4 = 'https://space-facts.com/mars/'
    Facts = pd.read_html(url_4)[0]
    Facts.columns = ['Attributes', 'Value']
    Facts


    # convert the data to a HTML table string
    Facts.to_html()

    # URL for scraping
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # Create Beautiful Soup object with html parser
    html = browser.html
    hemisphere_soup = BeautifulSoup(html, 'html.parser')


    # Populate a list with links for the hemispheres
    hemisphere_strings = []
    links = hemisphere_soup.find_all('h3')

    for hemisphere in links:
        hemisphere_strings.append(hemisphere.text)

    # create a list to put all the images
    hemisphere_image_urls = []

    # Loop through the hemisphere links to obtain the images
    for hemisphere in hemisphere_strings:
        # create a dictionary to put all the images
        hemisphere_dict = {}
        # use the links to find the text for each item
        try:
            browser.click_link_by_partial_text(hemisphere)

        # Scrape the image url string and store into the dictionary

            hemisphere_dict["img_url"] = browser.find_by_text('Sample')['href']
            hemisphere_dict["title"] = hemisphere

        # populate the dictionary with the urls
            hemisphere_image_urls.append(hemisphere_dict)
        except:
            continue
        # print the output to see results
        print(hemisphere_image_urls)
    browser.back()


    
    mars_data = {
        "title": news_title,
        "paragraph": news_paragraph,
        "mars_image": featured_image_full_url,
        "current_weather": tweet,
        "table": Facts.to_html(),
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_data

