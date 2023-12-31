"""This code is written by the Author Saif Chishti. It can be used by anyone who have access to it."""

# This code can  be used to grab specific items in the html content of the any webpage. Change it accordingly.
# Visit documentation of BeautifulSoup to get further assistance for using the code.
# Import required libraries
import requests
from bs4 import BeautifulSoup


def get_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    # For finding anchor tag in html. It will grab the first one
    print(soup.a)
    # For finding all anchor tags in html
    print(soup.findAll("a"))
    # Grabbing the title from a page
    print(soup.title.string)
    tag = soup.findAll("a")
    for t in tag:
        url2 = t.get("href")
        print(url2)


get_page(input("Enter URL to be scrapped: "))
