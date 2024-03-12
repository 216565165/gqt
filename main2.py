# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from service import service
import sys
from jbxx import tzzcx,tgcx,tycx
from xgxx import add,delete,change
from xtwh import user
import login

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 700)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(./img/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tzzxx = QtWidgets.QAction(MainWindow)
        self.tzzxx.setObjectName("tzzxx")
        self.tgxx = QtWidgets.QAction(MainWindow)
        self.tgxx.setObjectName("tgxx")
        # self.tycx = QtWidgets.QAction(MainWindow)
        # self.tycx.setObjectName("tycx")

        self.djxry = QtWidgets.QAction(MainWindow)
        self.djxry.setObjectName("djxry")
        self.scty = QtWidgets.QAction(MainWindow)
        self.scty.setObjectName("scty")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.tcdl = QtWidgets.QAction(MainWindow)
        self.tcdl.setObjectName("tcdl")
        self.tcxt = QtWidgets.QAction(MainWindow)
        self.tcxt.setObjectName("tcxt")
        # self.glgly = QtWidgets.QAction(MainWindow)
        # self.glgly.setObjectName("glgly")
        self.glyh = QtWidgets.QAction(MainWindow)
        self.glyh.setObjectName("glyh")
        self.menu.addAction(self.tzzxx)
        self.menu.addAction(self.tgxx)
        # self.menu.addAction(self.tycx)

        self.menu_2.addAction(self.djxry)
        self.menu_2.addAction(self.scty)
        self.menu_2.addAction(self.action_7)
        self.menu_3.addAction(self.tcdl)
        self.menu_3.addAction(self.tcxt)
        # self.menu_4.addAction(self.glgly)
        self.menu_4.addAction(self.glyh)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        datetime = QtCore.QDateTime.currentDateTime()  # 获取当前日期时间
        time = datetime.toString("yyyy-MM-dd HH:mm:ss")  # 对日期时间进行格式化
        # 状态栏中显示登录用户、登录时间，以及版权信息
        self.statusbar.showMessage(
            "当前登录用户：" + login.service.UserNameEdit + " | 登录时间：" + time + '  | ', 0)
        # 为基础设置菜单中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.openSet)
        #为基本信息管理菜单中的QAction绑定triggered信号

        # # 为系统管理菜单中的QAction绑定triggered信号
        self.menu_3.triggered[QtWidgets.QAction].connect(self.openQuit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "共青团员管理系统"))
        self.menu.setTitle(_translate("MainWindow", "基本信息"))

        self.menu_3.setTitle(_translate("MainWindow", "退出"))

        self.tzzxx.setText(_translate("MainWindow", "团组织查询"))
        self.tgxx.setText(_translate("MainWindow", "团员查询"))
        # self.tycx.setText(_translate("MainWindow", "团员查询"))


        self.tcdl.setText(_translate("MainWindow", "退出登录"))
        self.tcxt.setText(_translate("MainWindow", "退出系统"))

    # def show(self):
    #     self.m=print("1234")
    def openSet(self,m):
        if m.text()=="团组织查询":
            self.m = tzzcx.MyClass()
            self.m.show()
        elif  m.text()=="团员查询":
            self.m = tgcx.MyClass()
            self.m.show()
        # elif m.text() == "团员查询":
        #     self.m = tycx.MyClass()
        #     self.m.show()




    def openQuit(self,m):
        if m.text()=="退出登录":
            self.m = login.Ui_login()
            self.m.show()
            Ui_MainWindow.close(MainWindow)
        elif m.text()=="退出系统":
            Ui_MainWindow.close(MainWindow)




if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())