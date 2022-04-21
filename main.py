import requests
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui_imagedialog import Ui_Dialog
import pandas as pd

table1 = pd.DataFrame([['Лада', 'gg111g', '8.23']],
                      index=['Евгений Павлюченков'],
                      columns=['Модель автомобиля', 'Номер', 'Штраф'])
table1.to_csv('driver.csv')
# table1.to_excel('drivers.xlsx')
# headers = {
#      "accept": "*/*",
#      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/99.0.4844.74 Safari/537.36 "
#  }
# url = "https://auto.mail.ru/info/penalty/"
# req = requests.get(url, headers=headers)
# src = req.text
# with open("index.html", "w") as file:
#     file.write(src)

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)
window.show()
sys.exit(app.exec())
