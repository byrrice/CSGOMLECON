from bs4 import BeautifulSoup
import urllib2
import json

#Set up jupyter notebook for this, testing becomes much easier and quicker


# need to scrape with own match profile, remember to get it
url = "https://csgo-stats.com/match/CSGO-Ry32F-HW2D2-RTe5i-AuPNZ-JuiTL/economy"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
data = soup.find('script', type="text/javascript")
data = str(data).split('var playerTotalCashEarned =')[1]
data = str(data).splitlines()
data = str(data[0]).split("},{")

# data = soup.find('script', type="text/javascript")
# data = str(data)
# json_string = data.split('var playerTotalCashEarned =')[1]
# json_string = str(json_string).splitlines()
# new = str(json_string[0]).split("(},{)")
# print(new[0])
# myJson = json.loads(new[0])
# d = myJson['data']
# print(d)

#String manipulation to get the desired data for the json scraping
data[0] = data[0][2:] + "}"
for i in range(1, 9):
    data[i] = "{" + data[i] + "}"
data[9] = "{" + data[9][:-2]
print(data[9])
for j in range(0, len(data)):
    myJson = json.loads(data[j])
    d = myJson['data']
    print(d)