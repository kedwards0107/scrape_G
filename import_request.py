import requests
from bs4 import BeautifulSoup
import pdfkit

# URL of the web page you want to extract the element from
url = 'https://www.google.com/search?q=starbucks+decaf+verona+ground&rlz=1C5CHFA_enUS892US893&oq=starbucks+decaf+verona+ground'

# https://www.google.com/search?q=starbucks+decaf+verona+ground&rlz=1C5CHFA_enUS892US893&oq=starbucks+decaf+verona+ground

# https://www.google.com/search?q=goldfish+crackers+30oz
# Fetch the HTML content from the URL
response = requests.get(url)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
links = soup.get_text(separator="\n", strip=True)
print(links)
