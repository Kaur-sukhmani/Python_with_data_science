# ipl-data-2020
import requests
from bs4 import BeautifulSoup
url = "https://www.espncricinfo.com/series/ipl-2020-21-1210595/points-table-standings"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text)

teams = soup.findAll("span", class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.findAll("td", class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")

data = []
for idx in range(8):
    team_data = []
    data.append(team_data)
print(data)

idx = 0
for team in teams:
    title = team.text.strip()
    data[idx].append(title)
    idx += 1
print(data)

team_idx = 0
for win in wins:
    num = win.text.strip()
    print(num)

    data[team_idx].append(num)
    idx += 1

    if idx % 8 == 0:
        print("wow..")
        team_idx += 1
print("final data:", data)
file = open("ipl-data-2020.csv", "a")
header = "TEAMS, M, W, L, T, N/R, NRR, For, Against"
file.write(header)

for info in data:
    csv = "{}, {}, {}, {}, {}, {}, {}, {}\n".format(info[0], info[1], info[2], info[3], info[4], info[4], info[5], info[6], info[7])
    file.write(csv)
    print(csv)
print("Check the file....")

