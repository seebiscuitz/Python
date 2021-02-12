from colorama import init
from colorama import Fore
from lxml import html
import website
import requests
import time
import os

init(autoreset=True)
cwd = os.path.dirname(os.path.abspath(__file__))
websites=[]
text_files = [f for f in os.listdir(cwd) if f.endswith('.txt')]

tempitems=[]
for wfile in text_files:
    cwfile = open(cwd + "\\" + wfile,'r')
    cwfile_name = cwfile.readline().strip('\n')
    cwfile_url = cwfile.readline().strip('\n')
    cwfile_status = cwfile.readline().strip('\n')
    while line := cwfile.readline():
        line = line.strip('\n')
        arr = line.split(',')
        tempitems.append([arr[0],arr[1]])
    nwebsite = website.website(cwfile_name, cwfile_url, cwfile_status, tempitems)
    websites.append(nwebsite)
    cwfile.close

print(websites[0].get_name(),websites[0].items[0],websites[0].get_status())

while True:
    for cwebsite in websites:
        for item in cwebsite.get_items():
            page = requests.get(item[-1])
            doc = html.fromstring(page.content)
            XPATH_AVAILABILITY = '//div[@id ="availability"]//text()'
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY) 
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
            if AVAILABILITY is None:
                print(time.strftime('%X %x'), Fore.GREEN + 'info ::',Fore.BLUE + '[' + cwebsite.get_url() + ']','[',item[0],']', Fore.RED +':: OUT OF STOCK')
            else:
                print(time.strftime('%X %x'), Fore.GREEN + 'info ::', Fore.BLUE + '[' + cwebsite.get_url() + ']','[',item[0],']', Fore.GREEN +':: IN STOCK')
            time.sleep(1)
