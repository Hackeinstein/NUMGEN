#import dependncies
from colorama import Fore, init
from bs4 import BeautifulSoup
from urllib.request  import urlopen
import lxml
import os 
import sys
#global variables
BASE_URL="https://www.wirefly.com/area-codes"
npa=[]
nxx=[]
init()
#collect city to scrape
print(Fore.YELLOW+"WELCOME TO AREA CODE SCRAPER")
print("")
state =input(Fore.BLUE+"Enter state: ").lower()
state=state.replace(" ","-")
print("")
city = input("Enter city to get area-codes: ").lower()
city=city.replace(" ","-")
print("")
print(Fore.YELLOW+"Extracting.......................")
#full = int(input("Generate type  0 for area-codes only, 1 for phone numbers : "))


# path variables 

landline_code_path=f"./results/landline/{city}/area-codes"
landline_num_path=f"./results/landline/{city}/phone-numbers"
wireless_code_path=f"./results/wireless/{city}/area-codes"
wireless_num_path=f"./results/wireless/{city}/phone-numbers"
# load site as soup 
#url=f'{BASE_URL}/{state_needed}/{city_needed}'
url=f"https://www.wirefly.com/area-codes/{state}/{city}"
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
modes = [item.get_text().strip(" ").lower() for item in modes]
carrier = [item.get_text().strip(" ") for item in carrier]

# print(nxx)
# print(carrier)

# create a super list
numbers =[]
index=0
for mode in modes:
    numbers.append([f'{npa[index]}{nxx[index]}',mode,carrier[index]])
    index=index+1



#make and check directories
if True:
    if not os.path.exists(landline_num_path):
        os.makedirs(landline_num_path)
    if not os.path.exists(wireless_num_path):
        os.makedirs(wireless_num_path)

if not os.path.exists(landline_code_path):
    os.makedirs(landline_code_path)
if not os.path.exists(wireless_code_path):
    os.makedirs(wireless_code_path)

#save all area codes
for number in numbers:
    #write into file
    with open(f"results/{number[1]}/{city}/area-codes/{number[2]}.txt", "a") as file:
        file.write(f"{number[0]}\n")
print(" ")
print(Fore.GREEN+"DONE.................")
print("")
cont=input(Fore.RED+"Would you like to generate for new city Y/N: ").lower()
if cont == "y":
    os.system("cls")
    os.execv(sys.executable, ['python']+sys.argv)
else:
    exit()

# scrape city