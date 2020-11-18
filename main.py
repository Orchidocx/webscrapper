import helper

# import time
# import 
PRODUCT_URLS = [
  {"RX 6800": "https://www.nowinstock.net/computers/videocards/amd/rx6800/"},
  {"RX 6800 XT": "https://www.nowinstock.net/computers/videocards/amd/rx6800xt/"},
  {"RX 6900 XT": "https://www.nowinstock.net/computers/videocards/amd/rx6900xt/"},
  {"Nintendo Switch": "https://www.nowinstock.net/videogaming/consoles/nintendoswitch/"}
  ]
if __name__ == "__main__":
  # print(PRODUCT_URLS[0].keys())
  helper.welcomeMessage()
  print('Select a product to track (enter a number between 1 to 4):')
  for index, item in enumerate(PRODUCT_URLS):
    print(f'{index+1}) {list(item.keys())[0]}')
  # product = helper.trackProduct()
  selected_product = input('> ')
  while True:
    try:
      int(selected_product)
      break
    except:
      print('Invalid input')
      selected_product = input('> ')
  # helper.verifyProduct(product)
  
  # url = 'https://www.nowinstock.net/videogaming/consoles/nintendoswitch/'
  # print(urllib.parse.quote('rx 6800'))
  # url = 'https://www.nowinstock.net/computers/videocards/amd/rx6800xt/'
  # time_wait = 60
  # while True:
    # monitorSupply(url);
    # print(f'Waiting for {time_wait} seconds...')
    # time.sleep(time_wait)