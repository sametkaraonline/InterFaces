import sys

from PyQt5 import QtGui

from PyQt5.QtWidgets import QFileDialog,QRadioButton,QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QAction,qApp,QMainWindow,QLineEdit

import requests

from bs4 import BeautifulSoup

class Pencere(QWidget):

    def __init__(self):

        super().__init__()
        self.hesapla()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani =QLabel("Filmin ismini girerek ratigini ve sırasını öğrenebilirsiniz.")
        self.yazi = QLabel("Film ismi:")
        self.isim = QLineEdit()
        self.gorsel  = QLabel()
        self.ara =  QPushButton("Ara")
        self.yazi_alani2= QLabel("")

        self.gorsel.setPixmap(QtGui.QPixmap("download2.png"))

        h_box = QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.gorsel)
        h_box.addStretch()

        h_box2 = QHBoxLayout()

        h_box2.addWidget(self.yazi)
        h_box2.addWidget(self.isim)

        h_box3 = QHBoxLayout()

        h_box3.addStretch()
        h_box3.addWidget(self.ara)
        h_box3.addStretch()

        v_box = QVBoxLayout()

        v_box.addLayout(h_box)
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addWidget(self.yazi_alani2)

        self.setLayout(v_box)
        self.setWindowTitle("Imdb Top 250")


        self.ara.clicked.connect(self.click)

        self.show()

    def click(self):
        if self.isim.text() in self.sıra_sozluk and self.isim.text() in self.rating_sozluk :
            print("geldi")
            self.yazi_alani2.setText("Film ismi: {} Film sıralaması: {} Film ratingi: {}".format(self.isim.text(),self.sıra_sozluk[self.isim.text()],self.rating_sozluk[self.isim.text()]))

    def hesapla(self):

        url = "https://www.imdb.com/chart/top/"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        baslıklar = soup.find_all("td", {"class": "titleColumn"})

        ratingler = soup.find_all("td", {"class": "ratingColumn imdbRating"})

        self.sıra_sozluk = dict()
        self.rating_sozluk = dict()

        for baslık, rating in zip(baslıklar, ratingler):


            baslık = baslık.text
            rating = rating.text

            baslık = baslık.strip()
            baslık = baslık.replace("\n", "")
            baslık = baslık.replace(" ","")

            rating = rating.strip()
            rating = rating.replace("\n", "")

            string = str()
            sıra = str()
            for i in baslık:
                string +=i
                if i ==".":
                    if len(sıra) ==0:
                        sıra = string
                        string = ""
            sıra = sıra.replace(".","")

            self.sıra_sozluk[string] = sıra
            self.rating_sozluk[string] = rating

app = QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())