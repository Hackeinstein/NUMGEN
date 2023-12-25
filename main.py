#import dependncies
import colorama
import requests
from bs4 import BeautifulSoup
from urllib.request  import urlopen
import lxml

#global variables
BASE_URL="https://www.wirefly.com/area-codes"
npa=[]
nxx=[]

# collect city to scrape
# state_needed=input("Enter state: ").lower()
# city_needed = input("Enter city to get area-codes: ").lower()
# gen_type = int(input("Generate type  1 for area-codes only 0 for phone numbers : "))


# load site as soup 
#url=f'{BASE_URL}/{state_needed}/{city_needed}'
url="https://www.wirefly.com/area-codes/north-carolina/apex"
page= urlopen(url)
html_source= page.read().decode("utf-8")
soup = BeautifulSoup(html_source, features="lxml")

with open("stuff.html", 'w') as file:
    file.write(html_source)

npa=soup.find_all("td", class_="views-field views-field-npa")
nxx=soup.find_all("td", class_="views-field views-field-nxx")
modes=soup.find_all("td", class_="views-field views-field-nxx-use-type")
carrier=soup.find_all("td", class_="views-field views-field-company-name")

if npa ==[] or nxx==[]:
    print("No data for selection")

#obtain interger data values
npa = [int(item.get_text().strip(" ")) for item in npa]
nxx = [int(item.get_text().strip(" ")) for item in nxx]
modes = [item.get_text().strip(" ") for item in modes]
carrier = [item.get_text().strip(" ") for item in carrier]
index=0


for mode in modes:
    if mode == "Wireless":
        print("Yes")
    index=index+1

#print(new)
#save values

# scrape city