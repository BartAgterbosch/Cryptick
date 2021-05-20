import os
import time
from typing import Text
import yfinance as price_graph
import cursor


if os.name == 'nt':
    refresh = 'cls'
else:
    refresh = 'clear'
print("\n")
print("  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗██╗  ██╗")
time.sleep(0.2)
print(" ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔════╝██║ ██╔╝")
time.sleep(0.2)
print(" ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║     █████╔╝ ")
time.sleep(0.2)
print(" ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║     ██╔═██╗ ")
time.sleep(0.2)
print(" ╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╗██║  ██╗")
time.sleep(0.2)
print("  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝")
time.sleep(2)

def current_crypto_price(symbol):
    ticker = price_graph.Ticker(symbol)
    crypto_data = ticker.history(period='1m')
    return crypto_data['Close'][0]

symbol_dict = {'Ethereum': 'ETH-USD', 'Bitcoin': 'BTC-USD', 'Cardano': 'ADA-USD', 'Polkadot': 'DOT1-USD', 'Monero': 'XMR-USD', 'Dogecoin': 'DOGE-USD', 'Uniswap': 'UNI3-USD', 'Vechain': 'VET-USD'}

sanity_bool = False
while sanity_bool == False:
    crypto_symbol = input("Check price of which crypto?\nAvailable: Ethereum, Bitcoin, Cardano, Polkadot, Monero, Dogecoin, Uniswap, Vechain.\n").lower().capitalize()
    if crypto_symbol in symbol_dict:
        sanity_bool = True
    else:
        print("That is not how you spell it, try again!")
        
while True:        
    cursor.hide()
    os.system(refresh)   
    price = current_crypto_price(symbol_dict[crypto_symbol])
    print("\n")
    print("  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗██╗ ██████╗██╗  ██╗\n"
" ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██║██╔════╝██║ ██╔╝\n"
" ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║██║     █████╔╝ \n"
" ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║██║     ██╔═██╗ \n"
" ╚██████╗██║  ██║   ██║   ██║        ██║   ██║╚██████╗██║  ██╗\n"
"  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚═╝ ╚═════╝╚═╝  ╚═╝\n")
    print(f"{crypto_symbol}: ${price:.2f}")
    time.sleep(5)