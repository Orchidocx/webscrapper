from bs4 import BeautifulSoup
import requests, re, time, urllib.parse
# import time
# import 

def monitorSupply(url):
  html_text = requests.get(url)._content
  soup = BeautifulSoup(html_text, 'lxml')
  suppliers = soup.find_all('tr', {'id':re.compile('tr*')})

  for supplier in suppliers:
    name = supplier.find('td')
    stockStatus = supplier.find('td', {'class': 'stockStatus'})
    if(name.a['href'] != '#'):
      print(f'''
      {name.text}
      Status: {stockStatus.text}
      Link: {name.a["href"]}
      ''')

def welcomeMessage():
  print('Welcome to the Web Scrapping Project!')

def trackProduct():
  print('Enter the product you wish to track')
  return input('> ')

def verifyProduct(product):
  print(f'Checking for [{product}] in the system...')
  

if __name__ == "__main__":
  product = trackProduct()
  verifyProduct(product);
  urllib.parse.quote(product);
  # url = 'https://www.nowinstock.net/videogaming/consoles/nintendoswitch/'
  print(product)
  # print(urllib.parse.quote('rx 6800'))
  # url = 'https://www.nowinstock.net/computers/videocards/amd/rx6800xt/'
  # time_wait = 60
  # while True:
    # monitorSupply(url);
    # print(f'Waiting for {time_wait} seconds...')
    # time.sleep(time_wait)