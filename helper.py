from bs4 import BeautifulSoup
import requests, re, urllib.parse

class bcolors:
  HEADER = '\x1b[6;30;42m'
  END = '\x1b[0m'

def welcomeMessage():
  print('Welcome to the Web Scrapping Project!')

def trackProduct():
  print('Enter the product you wish to track')
  return input('> ')

def monitorSupply(url, captureNoStock):
  html_text = requests.get(url)._content
  soup = BeautifulSoup(html_text, 'html.parser')
  suppliers = soup.find_all('tr', {'id':re.compile('tr*')})

  for supplier in suppliers:
    name = supplier.find('td')
    stockStatus = supplier.find('td', {'class': 'stockStatus'})
    if(captureNoStock):
      if(name.a['href'] != '#'):
        print(f'Name: {name.text}')
        
        if(stockStatus.text == "Out of Stock"):
          print(f'Status: ***{stockStatus.text}***')
        else:
          print(f'Status: >>>>>{stockStatus.text}<<<<<')
        print(f'Link: {name.a["href"]}\n')

# def verifyProduct(product):
  # print(f'Checking for [{product}] in the system...')
  # url = f'https://www.nowinstock.net/search.php?q={urllib.parse.quote(product)}'
  # driver = webdriver.Firefox()
  # driver.get(url)
  # time.sleep(5)
  # htmlSource = driver.page_source
  # print(htmlSource)
  # first_link = driver.find_element_by_class_name(class_='gs-title')
  # print(first_link.text)
  # html_text = requests.get(url)._content
  # soup = BeautifulSoup(html_text, 'lxml')
  # print(soup)
  # link = soup.find('div', {'id': 'content'})
  # print(link)

def printFixedList(arr):
  for index, item in enumerate(arr):
    print(f'{index+1}) {list(item.keys())[0]}')