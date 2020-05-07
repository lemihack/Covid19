#!/usr/bin/python3
import requests
import json
import pyfiglet 
  



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

response = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases', headers=headers)
data = json.loads(response.content.decode())
globalData = data['global']
nepalData = data['nepal']




text = pyfiglet.figlet_format("COVID19") 
print(text)

print('-'*80)
print("\n")


print(f'        Global Death        :       {globalData["deaths"]}')
print(f'        Nepal Death         :       {nepalData["deaths"]}')
print(f'        Samples Tested      :       {nepalData["samples_tested"]}')
print(f'        Total Positive      :       {nepalData["positive"]}')
print(f'        Total Negative      :       {nepalData["negative"]}')

print("\n")


print('-'*80)
