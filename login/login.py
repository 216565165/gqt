# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(622, 290)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.UserNameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.UserNameEdit.setGeometry(QtCore.QRect(330, 90, 201, 31))
        self.UserNameEdit.setObjectName("UserNameEdit")
        self.PassWordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PassWordEdit.setGeometry(QtCore.QRect(330, 130, 201, 31))
        self.PassWordEdit.setObjectName("PassWordEdit")
        self.Username = QtWidgets.QLabel(self.centralwidget)
        self.Username.setGeometry(QtCore.QRect(280, 90, 54, 31))
        self.Username.setObjectName("Username")
        self.PassWord = QtWidgets.QLabel(self.centralwidget)
        self.PassWord.setGeometry(QtCore.QRect(280, 130, 54, 31))
        self.PassWord.setObjectName("PassWord")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 10, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.AdministratorButton = QtWidgets.QRadioButton(self.centralwidget)
        self.AdministratorButton.setGeometry(QtCore.QRect(330, 170, 89, 21))
        self.AdministratorButton.setObjectName("AdministratorButton")
        self.UserButton = QtWidgets.QRadioButton(self.centralwidget)
        self.UserButton.setGeometry(QtCore.QRect(420, 170, 89, 21))
        self.UserButton.setObjectName("UserButton")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(330, 200, 75, 23))
        self.LoginButton.setObjectName("LoginButton")
        self.QuitButton = QtWidgets.QPushButton(self.centralwidget)
        self.QuitButton.setGeometry(QtCore.QRect(420, 200, 75, 23))
        self.QuitButton.setObjectName("QuitButton")
        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setEnabled(True)
        self.Logo.setGeometry(QtCore.QRect(110, 80, 151, 121))
        self.Logo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Logo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Logo.setAutoFillBackground(False)
        self.Logo.setStyleSheet("background-image: url(:/logo/logo.jpg);")
        self.Logo.setText("")
        self.Logo.setWordWrap(False)
        self.Logo.setOpenExternalLinks(False)
        self.Logo.setObjectName("Logo")
        login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 23))
        self.menubar.setObjectName("menubar")
        login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登录"))
        self.Username.setText(_translate("login", "用户名："))
        self.PassWord.setText(_translate("login", "密码："))
        self.label_3.setText(_translate("login", "高校学生团员管理信息系统登录页面"))
        self.AdministratorButton.setText(_translate("login", "管理员"))
        self.UserButton.setText(_translate("login", "普通用户"))
        self.LoginButton.setText(_translate("login", "登录"))
        self.QuitButton.setText(_translate("login", "退出"))
import logo_rc

import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())