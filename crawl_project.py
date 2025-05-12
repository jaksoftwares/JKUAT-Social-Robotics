import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET
from xml.dom import minidom
from datetime import datetime

# Starting URL (replace with your project URL)
BASE_URL = "https://www.jkuatsocialroboticslab.com"

# A set to hold all the unique URLs discovered
visited_urls = set()

# Crawl function to visit pages and gather URLs
def crawl(url):
    # If this URL has already been visited, skip it
    if url in visited_urls:
        return

    # Mark this URL as visited
    visited_urls.add(url)
    print(f"Visiting: {url}")

    try:
        # Send GET request to the page
        response = requests.get(url)
        
        # If the request is successful (status code 200), continue
        if response.status_code == 200:
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all anchor tags with href attributes
            for link in soup.find_all('a', href=True):
                href = link['href']

                # Make sure to resolve relative URLs to absolute URLs
                absolute_url = urljoin(url, href)

                # Check if the URL is part of the same domain
                if urlparse(absolute_url).netloc == urlparse(BASE_URL).netloc:
                    crawl(absolute_url)

    except Exception as e:
        print(f"Error while crawling {url}: {e}")

# Start crawling from the base URL
crawl(BASE_URL)

# Output all the discovered URLs
print("\nDiscovered URLs:")
for visited_url in visited_urls:
    print(visited_url)

# Function to prettify XML output
def prettify_xml(elem):
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Create a sitemap.xml file with lastmod, changefreq, and priority
def create_sitemap(urls):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for url in urls:
        url_elem = ET.SubElement(urlset, "url")
        
        loc = ET.SubElement(url_elem, "loc")
        loc.text = url
        
        # Add lastmod, changefreq, priority
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = datetime.now().strftime("%Y-%m-%d")

        changefreq = ET.SubElement(url_elem, "changefreq")
        changefreq.text = "monthly"

        priority = ET.SubElement(url_elem, "priority")
        priority.text = "0.8"

    # Prettify and write the XML to a file
    with open("sitemap.xml", "w", encoding="utf-8") as file:
        file.write(prettify_xml(urlset))
    print("Sitemap.xml generated successfully!")

# Create a robots.txt file
def create_robots_txt():
    with open('robots.txt', 'w') as file:
        file.write("User-agent: *\n")
        file.write("Disallow: /admin/\n")
        file.write("Sitemap: https://www.jkuatsocialroboticslab.com/sitemap.xml\n")
    print("Robots.txt generated successfully!")

# Generate the sitemap and robots.txt
create_sitemap(visited_urls)
create_robots_txt()
