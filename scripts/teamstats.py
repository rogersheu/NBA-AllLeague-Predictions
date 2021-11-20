from bs4 import BeautifulSoup
import requests
from csv_functions import write_to_csv
from csv_functions import reset_csv

fileName = 'baseData/teamadvancedstats.csv'

def scrape_teamstats(fileName, year):
    yearURL = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '.html'
    yearPage = requests.get(yearURL)
    yearSoup = BeautifulSoup(yearPage.content, 'html.parser', from_encoding = 'utf-8')

    teamTable = yearSoup.find('table', id="per_game-team")
    leagueAvg = teamTable.find('tfoot').find_all('td')
    
    averages = []
    for col in leagueAvg:
        averages.append(col.text)
    
    averages.insert(2, year)
    write_to_csv(fileName, averages)


def scrape_teamadvanced(fileName, year):
    yearURL = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '.html'
    yearPage = requests.get(yearURL)
    yearSoup = BeautifulSoup(yearPage.content, 'html.parser', from_encoding = 'utf-8')

    teamTable = yearSoup.find('table', id="advanced-team")
    leagueAvg = teamTable.find('tfoot').find_all('td')
    
    write_to_csv(fileName, ['Pace', 'Year', 'FTr', '3PAr', 'TS%'])

    averages = []
    for col in leagueAvg:
        averages.append(col.text)
    
    averages = averages[12:16]

    averages.insert(1, year)
    write_to_csv(fileName, averages)




def scrape_allyears(fileName):
    yearList = range(1980, 2023)
    reset_csv(fileName)
    for year in yearList:
        # scrape_teamstats(fileName, year)
        scrape_teamadvanced(fileName, year)


scrape_allyears(fileName)