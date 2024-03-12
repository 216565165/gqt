# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from 团员管理系统.service import service


class Ui_add(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, add):
        add.setObjectName("add")
        add.resize(772, 257)
        self.centralwidget = QtWidgets.QWidget(add)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(23, 51, 61, 31))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 50, 161, 31))
        self.name.setObjectName("name")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(330, 50, 161, 31))
        self.sex.setObjectName("sex")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 61, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 50, 61, 31))
        self.label_3.setObjectName("label_3")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(580, 50, 161, 31))
        self.age.setObjectName("age")
        self.job = QtWidgets.QLineEdit(self.centralwidget)
        self.job.setGeometry(QtCore.QRect(580, 90, 161, 31))
        self.job.setObjectName("job")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(23, 90, 61, 31))
        self.label_4.setObjectName("label_4")
        self.organization = QtWidgets.QLineEdit(self.centralwidget)
        self.organization.setGeometry(QtCore.QRect(80, 90, 161, 31))
        self.organization.setObjectName("organization")
        self.time = QtWidgets.QLineEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(330, 90, 161, 31))
        self.time.setObjectName("time")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 90, 61, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 90, 61, 31))
        self.label_6.setObjectName("label_6")
        self.add_2 = QtWidgets.QPushButton(self.centralwidget)
        self.add_2.setGeometry(QtCore.QRect(330, 150, 161, 51))
        self.add_2.setObjectName("add_2")
        add.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(add)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 23))
        self.menubar.setObjectName("menubar")
        add.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(add)
        self.statusbar.setObjectName("statusbar")
        add.setStatusBar(self.statusbar)

        self.retranslateUi(add)
        QtCore.QMetaObject.connectSlotsByName(add)
        self.add_2.clicked.connect(self.add)

    def retranslateUi(self, add):
        _translate = QtCore.QCoreApplication.translate
        add.setWindowTitle(_translate("add", "登记新团员"))
        self.label.setText(_translate("add", "团员姓名："))
        self.label_2.setText(_translate("add", "团员性别："))
        self.label_3.setText(_translate("add", "团员年龄："))
        self.label_4.setText(_translate("add", "所属组织："))
        self.label_5.setText(_translate("add", "入团时间："))
        self.label_6.setText(_translate("add", "团员职位："))
        self.add_2.setText(_translate("add", "添加"))

    def add(self):
        name = self.name.text()
        sex = self.sex.text()
        age = self.age.text()
        job = self.job.text()
        time = self.time.text()
        organization=self.organization.text()
        if name != "" and sex != ""and age != ""and job != ""and time != ""and organization != "":
            sql = "select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员姓名 like '%" + name + "%'"
            result = service.query2(sql)
            if len(result)>0:
                self.name.setText("")
                QMessageBox.information(None, '提示', '您要添加的团员已经存在，请重新输入！', QMessageBox.Ok)
            else:
                # 执行添加语句
                result = service.exec("insert into tb_tg(团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位) values (%s,%s,%s,%s,%s,%s)", (name, sex,age,organization,time,job))
                if result > 0:  # 如果结果大于0，说明添加成功

                    QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_add()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())