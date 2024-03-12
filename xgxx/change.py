# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
import sys
from 团员管理系统.service import service
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_change(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, change):
        change.setObjectName("change")
        change.resize(474, 298)
        self.centralwidget = QtWidgets.QWidget(change)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label.setObjectName("label")
        self.name1 = QtWidgets.QLineEdit(self.centralwidget)
        self.name1.setGeometry(QtCore.QRect(120, 30, 113, 31))
        self.name1.setObjectName("name1")
        self.name2 = QtWidgets.QLineEdit(self.centralwidget)
        self.name2.setGeometry(QtCore.QRect(120, 70, 113, 31))
        self.name2.setObjectName("name2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 111, 31))
        self.label_3.setObjectName("label_3")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(350, 70, 113, 31))
        self.sex.setObjectName("sex")
        self.org = QtWidgets.QLineEdit(self.centralwidget)
        self.org.setGeometry(QtCore.QRect(350, 110, 113, 31))
        self.org.setObjectName("org")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 111, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(240, 110, 111, 31))
        self.label_5.setObjectName("label_5")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(120, 110, 113, 31))
        self.age.setObjectName("age")
        self.time = QtWidgets.QLineEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(120, 150, 113, 31))
        self.time.setObjectName("time")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 111, 31))
        self.label_6.setObjectName("label_6")
        self.job = QtWidgets.QLineEdit(self.centralwidget)
        self.job.setGeometry(QtCore.QRect(350, 150, 113, 31))
        self.job.setObjectName("job")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(240, 150, 111, 31))
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 200, 131, 51))
        self.pushButton.setObjectName("pushButton")
        change.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(change)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 474, 23))
        self.menubar.setObjectName("menubar")
        change.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(change)
        self.statusbar.setObjectName("statusbar")
        change.setStatusBar(self.statusbar)

        self.retranslateUi(change)
        QtCore.QMetaObject.connectSlotsByName(change)

        self.pushButton.clicked.connect(self.change)

    def retranslateUi(self, change):
        _translate = QtCore.QCoreApplication.translate
        change.setWindowTitle(_translate("change", "修改团员信息"))
        self.label.setText(_translate("change", "要修改的团员姓名："))
        self.label_2.setText(_translate("change", "修改后团员姓名："))
        self.label_3.setText(_translate("change", "修改后团员性别："))
        self.label_4.setText(_translate("change", "修改后团员年龄："))
        self.label_5.setText(_translate("change", "修改后所属团组织："))
        self.label_6.setText(_translate("change", "修改后入团时间："))
        self.label_7.setText(_translate("change", "修改后职位："))
        self.pushButton.setText(_translate("change", "修改"))

    def change(self):
        name = self.name1.text()
        if name != "":
            sql = "select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员姓名 like '%" + name + "%'"
            result = service.query2(sql)
            if len(result) > 0:
                result2 = service.exec("delete from tb_tg where 团员姓名= %s", (name,))
                name2 = self.name2.text()
                sex = self.sex.text()
                age = self.age.text()
                job = self.job.text()
                time = self.time.text()
                organization = self.org.text()
                if name2 != "" and sex != "" and age != "" and job != "" and time != "" and organization != "":
                    sql = "select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员姓名 like '%" + name2 + "%'"
                    result = service.query2(sql)
                    if len(result) > 0:
                        self.name2.setText("")
                        QMessageBox.information(None, '提示', '您要修改的团员已经存在，请重新输入！', QMessageBox.Ok)
                    else:
                        # 执行添加语句
                        result = service.exec(
                            "insert into tb_tg(团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位) values (%s,%s,%s,%s,%s,%s)",
                            (name2, sex, age, organization, time, job))
                        if result > 0:  # 如果结果大于0，说明添加成功

                            QMessageBox.information(None, '提示', '修改成功！', QMessageBox.Ok)
                else:
                    QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)
                # if result2 > 0:  # 如果结果大于0，说明删除成功
                #
                #     QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
                # else:
                #     QMessageBox.information(None, '提示', '信息删除失败！', QMessageBox.Ok)

            else:
                self.name1.setText("")
                QMessageBox.information(None, '提示', '您要修改的团员不存在，请重新输入！', QMessageBox.Ok)
        else:
            QMessageBox.information(None, '提示', '请重新输入要修改的团员姓名！', QMessageBox.Ok)

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_change()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())