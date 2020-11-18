import helper
import time

PRODUCT_URLS = [
  {"RX 6800": "https://www.nowinstock.net/computers/videocards/amd/rx6800/"},
  {"RX 6800 XT": "https://www.nowinstock.net/computers/videocards/amd/rx6800xt/"},
  {"RX 6900 XT": "https://www.nowinstock.net/computers/videocards/amd/rx6900xt/"},
  {"Nintendo Switch": "https://www.nowinstock.net/videogaming/consoles/nintendoswitch/"}
  ]

if __name__ == "__main__":
  helper.welcomeMessage()
  print('Select a product to track (enter a number between 1 to 4):')
  helper.printFixedList(PRODUCT_URLS)
  product_name, product_url, refresh_time = ['','','']
  selected_product = input('> ')
  while True:
    try:
      selected_product = int(selected_product)
      if selected_product <= 4 and selected_product >= 1:
        product_name = list(PRODUCT_URLS[selected_product-1].keys())[0]
        product_url = list(PRODUCT_URLS[selected_product-1].values())[0]
        print(f'You selected {product_name}')
        print('How frequent do you want to update status? (5 to 60 seconds)\n[DEFAULT: 15]')
        refresh_time = input('Press [ENTER] for default\n> ')
        try:
          if refresh_time == '':
            refresh_time = 15
          else:
            refresh_time = int(refresh_time)
            if refresh_time >= 5 and refresh_time <= 60:
              pass
            else:
              print('Invalid input')
              refresh_time = input('> ')
        except:
          print('Invalid input')
          refresh_time = input('> ')
        
        print(product_name, product_url, refresh_time)
        break
      else:
        print('Invalid input')
        selected_product = input('> ')
    except:
      print('Invalid input')
      selected_product = input('> ')
  while True:
    helper.monitorSupply(product_url, True)
    print(f'Refreshing in {refresh_time} seconds...')
    time.sleep(refresh_time)