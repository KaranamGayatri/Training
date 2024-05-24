import requests
import bs4

res = requests.get("http://quotes.toscrape.com/")
print(res.text)

soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select(".author"))

authors = set()
for name in soup.select(".author"):
    authors.add(name.text)

print(authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print(quotes)

soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup.select('.tag-item'))

for item in soup.select(".tag-item"):
    print(item.text)

url = 'http://quotes.toscrape.com/page/'

authors = set()

for page in range(1,10):

    # Concatenate to get new page URL
    page_url = url+str(page)
    # Obtain Request
    res = requests.get(page_url)
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
# Choose some huge page number we know doesn't exist
page_url = url+str(9999999)
# Obtain Request
res = requests.get(page_url)
# Turn into Soup
soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)

print("No quotes found!" in res.text)

page_still_valid = True
authors = set()
page = 1

while page_still_valid:

    # Concatenate to get new page URL
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1

print(authors)