import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Define the URL to scrape
url = "https://www.wg-gesucht.de/wg-zimmer-in-Frankfurt-am-Main.41.0.1.1.html"

# Send a GET request to the URL
response = requests.get(url)


#%% Step 1: Scrape the listings

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the listing details
    listings = soup.find_all('div', class_='wgg_card offer_list_item')


    data = {}
    # Iterate through each listing and extract the required information
    for listing in listings:
        # Extract the link
        link= listing.find('a', href=True)['href']
        full_link = "https://www.wg-gesucht.de" + link
        print(link)
        
        # Create a sub dictionary for this entry
        data[link] = {}
        data[link]["full_link"] = full_link
        
        # Extract the title
        title = listing.find('h3', class_='truncate_title').text.strip()
        data[link]["title"] = title
        
        # Extract the WG type and location
        details = listing.find('div', class_='col-xs-11').text.strip()
        data[link]["details"] = details
        
        # Extract the price
        price = listing.find('div', class_='col-xs-3').text.strip()
        data[link]["price"] = price
        
        # Extract the availability dates
        availability = listing.find('div', class_='col-xs-5 text-center').text.strip()
        data[link]["availability"] = availability
        
        # Extract the size
        size = listing.find('div', class_='col-xs-3 text-right').text.strip()
        data[link]["size"] = size
        
        # Extract the landlord's name
        landlord = listing.find('span', class_='ml5').text.strip()
        data[link]["landlord"] = landlord
        
        # Extract the online status
        online_status = listing.find('span', style="color: #218700;").text.strip()
        data[link]["online_status"] = online_status
        
        

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


#%% Step 2: get details for each listing in data


def get_listing_details(url):
    # Send a GET request to the listing URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract additional details like descriptions
        descriptions = {}
        # Extracting descriptions for "Zimmer", "Lage", "WG-Leben", "Sonstiges"
        tabs = ["freitext_0", "freitext_1", "freitext_2", "freitext_3"]
        labels = ["Zimmer", "Lage", "WG-Leben", "Sonstiges"]
        for tab, label in zip(tabs, labels):
            content = soup.find('div', id=tab)
            if content:
                descriptions[label] = content.text.strip()
            else:
                descriptions[label] = "No description available"

        return {"descriptions": descriptions}
    
    else:
        print(f"Failed to retrieve the listing page. Status code: {response.status_code}")
        return {}

# Iterate over each listing and get additional details
for link, info in data.items():
    full_link = info["full_link"]
    details = get_listing_details(full_link)
    data[link].update(details)
    
    # To prevent overwhelming the server with requests, add a delay
    time.sleep(2)  # sleep for 2 seconds


# Save data
df = pd.DataFrame.from_dict(data, orient='index')
df.to_excel("wggesucht_scraped.xlsx")


