from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


# Send HTTP request and retrieve HTML content
url = 'https://www.google.com'
response = requests.get(url)

# Create Beautiful Soup object
soup = BeautifulSoup(response.content, 'html.parser')
soup.find_next()
# Find all anchor tags (links) within the webpage
anchors = soup.find_all('a')

# Extract and process the internal links
for anchor in anchors:
    link = anchor.get('href')
    if link and not link.startswith('http'):  # Check if it's an internal link
        # Convert relative link to absolute link
        internal_link = urljoin(url, link)
        print(internal_link)
