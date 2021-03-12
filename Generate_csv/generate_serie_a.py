import csv
import requests
from bs4 import BeautifulSoup
from typing import List

URL = "https://www.campeoesdofutebol.com.br/brasileiro.html"
page = requests.get(url=URL)
soup = BeautifulSoup(page.content, 'html.parser')


def search_champions():
    table_champions_soup: List = soup.find_all(name="table")
    a_series_soup = table_champions_soup[1]
    champions_tables_soup = a_series_soup.find_all(name="tr")
    for t_body in champions_tables_soup:
        if len(t_body.find_all(name="td")) == 4:
            values = t_body.find_all(name="td")
            champion_dict = {
                'year': values[0].text,
                'champion': values[1].text,
                'vice': values[2].text,
                'final': values[3].text
            }
            yield champion_dict


def generate_csv_champions(champion_dict):
    with open('champions.csv', 'w', newline='') as file:
        w = csv.writer(file, delimiter=";")
        w.writerow(["Year", "Champion", "Vice", "Final"])

        for champion in champion_dict:
            w.writerow([champion['year'], champion['champion'], champion['vice'], champion['final']])
