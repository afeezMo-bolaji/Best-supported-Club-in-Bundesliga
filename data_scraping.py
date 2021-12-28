from bs4 import BeautifulSoup
from numpy.lib.utils import source
from pandas.io import excel
import requests, re, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Bundesliga Spectator Statistics"
sheet.append(["Season", "Overall Spectators", "Average Spectators", "Best supported club"])

try:
    source = requests.get("https://en.wikipedia.org/wiki/Bundesliga")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, "html.parser")
    totalRanking = soup.find_all("table", class_ = "wikitable")[2].find('tbody').find_all('tr')

    iterRanking  = iter(totalRanking)
    next(iterRanking)
    for ranking in iterRanking:
        rankingTarget = ranking.find_all("td")
        season = rankingTarget[0].text[0:7]
        overallSpectators = rankingTarget[1].get_text(strip = True)
        averageSpectators = rankingTarget[2].get_text(strip = True)
        bestSupportedClub = rankingTarget[3].get_text(strip = True)
        
        sheet.append([season, overallSpectators, averageSpectators, bestSupportedClub])

except Exception as err:
    print(err)

excel.save("Bundesliga Spectator Statistics.xlsx")