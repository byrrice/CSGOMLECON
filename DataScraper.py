from bs4 import BeautifulSoup
import urllib2
import json
import numpy as np
import matplotlib.pyplot as plt

#Set up jupyter notebook for this, testing becomes much easier and quicker

#Case where there are more than 10 players or player leaves midway through, maybe take only pro matches?

# need to scrape with own match profile, remember to get it
url = "https://csgo-stats.com/match/CSGO-Ry32F-HW2D2-RTe5i-AuPNZ-JuiTL/economy"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")

# Basic data manipulation to get into json readable format
data = soup.find('script', type="text/javascript")
data = str(data).split('var playerTotalCashEarned =')[1]
data = str(data).splitlines()
data = str(data[0]).split("},{")
data[0] = data[0][2:] + "}"
for i in range(1, 9):
    data[i] = "{" + data[i] + "}"
data[9] = "{" + data[9][:-2]


totalEconomy = []
for j in range(0, len(data)):
    myJson = json.loads(data[j])
    totalEconomy.append(myJson['data'])

numberofrounds = len(totalEconomy[0])
for k in range(0, len(totalEconomy)):
    for l in range(0, len(totalEconomy[0])):
        totalEconomy[k][l] = totalEconomy[k][l][1]

# team1economy = []
# team2economy = []
# for i in range(0, 4):
#     for j in range(0, numberofrounds):
#         totalEconomy[i] = totalEconomy[i] + totalEconomy[i][j]
#         totalEconomy[i] = totalEconomy[i] + totalEconomy[i+5][j]
print(totalEconomy)
Economy1 = np.add(totalEconomy[0], totalEconomy[1])
Economy1 = np.add(Economy1, totalEconomy[2])
Economy1 = np.add(Economy1, totalEconomy[3])
Economy1 = np.add(Economy1, totalEconomy[4])
Economy2 = np.add(totalEconomy[5], totalEconomy[6])
Economy2 = np.add(Economy2, totalEconomy[7])
Economy2 = np.add(Economy2, totalEconomy[8])
Economy2 = np.add(Economy2, totalEconomy[9])
Economy1 = np.divide(Economy1, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) 
Economy1 = np.divide(Economy1, 5) 
Economy2 = np.divide(Economy2, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]) 
print(Economy1)
# def addEconomy(list, num):
#     if num == 0:
#         return list
#     else:
#         return np.add(list[num], addEconomy(list[num-1], num - 1)