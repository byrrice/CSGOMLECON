from bs4 import BeautifulSoup
import urllib2
import re

#Set up jupyter notebook for this, testing becomes much easier and quicker

#Case where there are more than 10 players or player leaves midway through, maybe take only pro matches?

# need to scrape with own match profile, remember to get it
url = "https://csgo-stats.com/match/CSGO-Ry32F-HW2D2-RTe5i-AuPNZ-JuiTL/rounds"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "html.parser")
parsedsoup = re.findall(r"\bForce\b|\bFull\b|\bEco\b|\bPistol\b", str(soup))

#remove last 8 characters due to Force,Full,Eco,Pistol stats showing up 8 times later on
parsedsoup = parsedsoup[:-8]

#These are the two buys 
team1buy = parsedsoup[::2]
team2buy = parsedsoup[1::2]

