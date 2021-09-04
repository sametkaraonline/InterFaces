import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QFileDialog,QRadioButton,QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QHBoxLayout,QAction,qApp,QMainWindow,QLineEdit





class pencere (QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()

        self.liste = []

    def init_ui(self):
        self.yazi_alani = QLabel("Göndermek istediğiniz mail adreslerini girin:")
        self.mail_ekle = QLineEdit()
        self.buton = QPushButton("Ekle")
        self.buton2 = QPushButton("Gönder")
        self.yazi_alani2 = QLabel("")



        h_box = QHBoxLayout()

        h_box.addWidget(self.yazi_alani)
        h_box.addWidget(self.mail_ekle)
        h_box.addWidget(self.buton)
        h_box.addWidget(self.buton2)

        h_box2 = QHBoxLayout()

        h_box2.addWidget(self.yazi_alani2)

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addStretch()

        self.setLayout(v_box)
        self.setWindowTitle("Mail Gönderme Programı")

        self.buton.clicked.connect(self.ekle)

        self.buton2.clicked.connect(self.mail_gonder)

        self.show()

    def ekle(self):

        self.liste.append(self.mail_ekle.text())

        print(self.liste)

    def deneme(self):
        print("geldi")
        for i in self.liste:
            print(i)


    def mail_gonder(self):


        for i in self.liste:

            mesaj = MIMEMultipart()

            mesaj["From"] = "kendi mailinizi girin"

            mesaj["To"] = i

            mesaj["Subject"] = "Mail Gönderme Ödevi"

            yazi = "#Stmp Seni Seviyorum Python Programlama Dili"

            mesaj_gövdesi = MIMEText(yazi, "plain")

            mesaj.attach(mesaj_gövdesi)


            mail = smtplib.SMTP("smtp.gmail.com", 587)

            mail.ehlo()

            mail.starttls()

            mail.login("kendi mailiniz", "şifre")

            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

            mail.close()

            self.yazi_alani2.setText("Mail veya Mailler başarıyla gönderildi.")


app = QApplication(sys.argv)

pencere = pencere()

sys.exit(app.exec_())








