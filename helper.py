from bs4 import BeautifulSoup
import requests, re, time, urllib.parse

def welcomeMessage():
  print('Welcome to the Web Scrapping Project!')

def trackProduct():
  print('Enter the product you wish to track')
  return input('> ')

def monitorSupply(url):
  html_text = requests.get(url)._content
  soup = BeautifulSoup(html_text, 'html.parser')
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

def verifyProduct(product):
  pass
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