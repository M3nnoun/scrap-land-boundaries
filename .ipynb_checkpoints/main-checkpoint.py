import requests
from bs4 import BeautifulSoup

def extract_information(div_element):
    country_info = {}

    # Extract country name
    country_name = div_element.find('a').text
    country_info['country_name'] = country_name

    # Extract total distance
    total_distance = div_element.find('strong', text='total:').find_next_sibling(text=True).strip()
    country_info['total_distance'] = total_distance

    # Extract bordering countries and their distances
    border_info = div_element.find('strong', text='border countries (6):').find_next_sibling(text=True).strip()
    border_info = border_info.split(';')
    border_countries = {}
    for border in border_info:
        border_parts = border.strip().split(' ')
        border_country = border_parts[0]
        border_distance = ' '.join(border_parts[1:]).strip()
        border_countries[border_country] = border_distance
    country_info['border_countries'] = border_countries

    return country_info

def scrape_webpage(url):
    contry_data=[]
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        selected_elements = soup.select('#index-content-section > div > div.col-lg-9.col-md-12.col-sm-12 div')
        for element in selected_elements:
            contry_data.append(extract_information(element))
        return contry_data
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return []
url = "https://www.cia.gov/the-world-factbook/field/land-boundaries/"

for element in scrape_webpage(url):
    print(element)
    print("--------------------")
