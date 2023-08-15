# web scrapping
# pip install beautifulsoup4
#  pip install requests
import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/indian-premier-league-2022-1298423/points-table-standings"
# url = "https://www.indiatoday.in/sports"

response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print( type(soup), id(soup))
# print(soup.prettify())

# tags = soup.findAll("h3")
teams = soup.findAll("span", class_="ds-text-tight-s ds-font-bold ds-uppercase ds-text-left ds-text-typo")
wins = soup.findAll("td", class_="ds-w-0 ds-whitespace-nowrap ds-min-w-max")

# list of dictionaries
# for idx in range(10):
#     team_data = {}
#     team_data['name'] = ""
#     team_data['stats'] = []
#     data.append(team_data)
#
# print(data)
# idx = 0
# for team in teams:
#     title = team.text.strip()
#     data[idx]['name'] = title
#     # data[idx]['stats'] = []
#     idx += 1
#     # print(title)
# print(data)
#
# idx = 0
# team_idx = 0
# for win in wins:
#     num = win.text.strip()
#     print(num)
#
#     # identify and fix
#
#     data[team_idx]['stats'].append(num)
#     idx += 1
#
#     if idx % 8 == 0:
#         print("wow..")
#         data[team_idx]['stats'] = data[team_idx]['stats'][:5]
#         team_idx += 1
# # this data is having a dictionary and a list
# for info in data:
#     print(info)
#
#
# #
# print("data finally :", data)
"""to create a list of list"""

data = []
for idx in range(10):
    team_data = []
    data.append(team_data)  # list of 10 list

print("data", data)

idx = 0
for team in teams:
    title = team.text.strip()
    data[idx].append(title)
    idx += 1

print("data", data)

idx = 0
team_idx = 0

for win in wins:
    num = win.text.strip()
    print(num)

    # identify and fix

    data[team_idx].append(num)
    idx += 1

    if idx % 8 == 0:
        print("wow..")
        team_idx += 1
# this data is having a list and a list


print("data finally :", data)

file = open("ipl-data-2022.csv", "a")
# here a is append mode -> data usmain append karta rahe
# csv -> excel file
header = "TEAMS, M, W, L, T, N/R, NRR, For, Against"
file.write(header)

for info in data:
    csv = "{},{},{},{},{},{},{},{}\n".format(info[0],info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
    file.write(csv)
    print(csv)
print("Check the file....")
# info is list
# coma seperated vaues -10, 20, 30, 40 ->values seperated by comaas
# to save all the data in a file

# last 5 years data ->HW
