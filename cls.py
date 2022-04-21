import pandas as pd
import re
from bs4 import BeautifulSoup


class Human:
    def __init__(self, name, second_name, car, number, fines):
        self.name = name
        self.second_name = second_name
        self.car = car
        self.fines = fines
        self.number = number

    def append_fine(self, number_fine):
        self.fines.append(number_fine)
        return self.fines

    def remove_fine(self, number_file):
        self.fines.remove(number_file)
        return self.fines

    def print_fines(self):
        for s in self.fines:
            print(s)


def creator_df():
    with open('index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    t_headers = soup.find(class_='p-penalties').find_all('th')
    t_body = soup.find(class_='p-penalties').find_all('tr')

    column_1 = []
    column_2 = []
    column_3 = []
    for item in t_body:
        t_cell = item.find_all('td')
        try:
            if re.search(r'\d+', t_cell[0].text) is not None:
                column_1.append(t_cell[0].text)
            else:
                continue
        except IndexError:
            continue

    for item in t_body:
        t_cell = item.find_all('td')
        try:
            if re.search(r'\d+', t_cell[0].text) is not None:
                column_2.append(t_cell[1].text)
            else:
                continue
        except IndexError:
            continue

    for item in t_body:
        t_cell = item.find_all('td')
        try:
            if re.search(r'\d+', t_cell[0].text) is not None:
                column_3.append(t_cell[2].text)
            else:
                continue
        except IndexError:
            continue

    table = pd.DataFrame({t_headers[0].text: column_1, t_headers[1].text: column_2, t_headers[2].text: column_3},
                         index=column_1)
    # table.to_excel('cars.xlsx', index=False)
    return table



