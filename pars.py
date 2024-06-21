import requests
from bs4 import BeautifulSoup



def get_html(url):
    house = requests.get(url)
    return house.text

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    rooms = soup.find_all('div', class_='card')
    print(rooms)

def main():
    url = 'https://kaliningrad.sutochno.ru/'
    print(get_data(get_html(url)))

if __name__ == '__main__':
    main()

