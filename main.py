import io
import sys
import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from enrty_db import *
from templates import *


class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        template2 = io.StringIO(registration_form)
        uic.loadUi(template2, self)
        self.button_reg.clicked.connect(self.get_registration)
        self.label_5.hide()

    def displayInfo(self):
        self.show()

    def get_registration(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        correct = False
        if login and password:
            if this_uniqe_login(login):
                correct = add_new_user(login, password)
            else:
                self.label_5.show()
        if correct:
            self.hide()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        template1 = io.StringIO(auth_form)
        uic.loadUi(template1, self)
        self.label_5.hide()
        self.RegistrationWindow = RegistrationWindow()
        self.btn_registration.clicked.connect(lambda: self.RegistrationWindow.displayInfo())
        self.btn_enter.clicked.connect(self.get_enter)

    def get_enter(self):
        login = self.loginEdit.text()
        password = self.passwordEdit.text()
        if login and password:
            id_player = get_user_id(login, password)
            if id_player:
                change_selected_user(id_player)
                os.system('python menu.py')
                self.close()
        self.label_5.show()

    def pull_id(self):
        return self.id_player


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())

