import sys
import requests

from bs4 import BeautifulSoup

from PyQt5 import QtGui

from PyQt5.QtWidgets import QFileDialog,QRadioButton,QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QAction,qApp,QMainWindow,QLineEdit



class pencere(QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.dolar = QRadioButton("Dolar")
        self.euro = QRadioButton("Euro")
        self.sterlin = QRadioButton("Sterlin")
        self.gümüş = QRadioButton("Gümüş")
        self.gram_altın =QRadioButton("Gram Altın")
        self.yazi_alani = QLabel("Miktar giriniz:")
        self.miktar = QLineEdit()
        self.yazi_alani_2 = QLabel("Döviz Seçiniz:")
        self.gorsel = QLabel()
        self.buton = QPushButton("Dönüştür")
        self.yazi_alani3 = QLabel("")

        self.gorsel.setPixmap(QtGui.QPixmap("images.png"))


        h_box = QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.yazi_alani)
        h_box.addWidget(self.miktar)
        h_box.addWidget(self.yazi_alani_2)
        h_box.addWidget(self.dolar)
        h_box.addWidget(self.euro)
        h_box.addWidget(self.sterlin)
        h_box.addWidget(self.gümüş)
        h_box.addWidget(self.gram_altın)
        h_box.addStretch()

        h_box2 = QHBoxLayout()

        h_box2.addStretch()
        h_box2.addWidget(self.gorsel)
        h_box2.addStretch()

        h_box3 = QHBoxLayout()

        h_box3.addStretch()
        h_box3.addWidget(self.buton)
        h_box3.addStretch()

        h_box4 = QHBoxLayout()

        h_box4.addStretch()
        h_box4.addWidget(self.yazi_alani3)
        h_box4.addStretch()

        v_box = QVBoxLayout()

        v_box.addLayout(h_box2)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)


        self.buton.clicked.connect(lambda: self.click(self.dolar.isChecked(),self.euro.isChecked(),self.sterlin.isChecked(),self.gümüş.isChecked(),self.gram_altın.isChecked()))

        self.setLayout(v_box)

        self.setWindowTitle("Döviz Dönüştürme Programı")

        self.show()

    def click(self,dolar,euro,sterlin,gümüş,gram_altın):

        tane = int(self.miktar.text())

        if dolar:
            deger = self.hesapla("USD",tane)
            self.yazi_alani3.setText(deger + " TL yapmaktadır.")
        if euro:
            deger = self.hesapla("EUR",tane)
            self.yazi_alani3.setText(deger + " TL yapmaktadır.")
        if sterlin:
            deger = self.hesapla("GBP",tane)
            self.yazi_alani3.setText(deger + " TL yapmaktadır.")
        if gümüş:
            deger = self.hesapla("gumus",tane)
            self.yazi_alani3.setText(deger + " TL yapmaktadır.")
        if gram_altın:
            deger = self.hesapla("gram-altin",tane)
            self.yazi_alani3.setText(deger + " TL yapmaktadır.")

    def hesapla(self,dovız, miktar):

        url = "https://www.doviz.com/"

        response = requests.get(url)

        html_icerigi = response.content

        soup = BeautifulSoup(html_icerigi, "html.parser")

        deger = soup.find("span", {"class": "value", "data-socket-key": dovız})

        deger = deger.text

        deger = deger.replace(",", ".")

        return str(round(miktar * float(deger),2))


app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())











