# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_user(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, user):
        user.setObjectName("user")
        user.resize(511, 610)
        self.centralwidget = QtWidgets.QWidget(user)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 491, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 230, 491, 71))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.find = QtWidgets.QPushButton(self.groupBox)
        self.find.setGeometry(QtCore.QRect(240, 20, 75, 21))
        self.find.setObjectName("find")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 81, 16))
        self.label_2.setObjectName("label_2")
        self.findname = QtWidgets.QLineEdit(self.groupBox)
        self.findname.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.findname.setObjectName("findname")
        self.findkind = QtWidgets.QLineEdit(self.groupBox)
        self.findkind.setGeometry(QtCore.QRect(100, 40, 121, 20))
        self.findkind.setObjectName("findkind")
        self.find_2 = QtWidgets.QPushButton(self.groupBox)
        self.find_2.setGeometry(QtCore.QRect(240, 40, 75, 21))
        self.find_2.setObjectName("find_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 300, 491, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.add = QtWidgets.QPushButton(self.groupBox_2)
        self.add.setGeometry(QtCore.QRect(240, 30, 75, 41))
        self.add.setObjectName("add")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 20, 71, 16))
        self.label_4.setObjectName("label_4")
        self.addname = QtWidgets.QLineEdit(self.groupBox_2)
        self.addname.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.addname.setObjectName("addname")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(40, 60, 71, 16))
        self.label_6.setObjectName("label_6")
        self.addpwd = QtWidgets.QLineEdit(self.groupBox_2)
        self.addpwd.setGeometry(QtCore.QRect(100, 40, 121, 20))
        self.addpwd.setObjectName("addpwd")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 71, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(100, 60, 121, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 491, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.delete_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.delete_2.setGeometry(QtCore.QRect(240, 10, 75, 23))
        self.delete_2.setObjectName("delete_2")
        self.delname = QtWidgets.QLineEdit(self.groupBox_3)
        self.delname.setGeometry(QtCore.QRect(100, 10, 121, 20))
        self.delname.setObjectName("delname")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label_7.setObjectName("label_7")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(420, 210, 75, 23))
        self.refresh.setObjectName("refresh")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 450, 491, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.change = QtWidgets.QPushButton(self.groupBox_4)
        self.change.setGeometry(QtCore.QRect(240, 30, 75, 41))
        self.change.setObjectName("change")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 101, 20))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.label_8.setObjectName("label_8")
        self.changename = QtWidgets.QLineEdit(self.groupBox_4)
        self.changename.setGeometry(QtCore.QRect(100, 10, 121, 20))
        self.changename.setText("")
        self.changename.setObjectName("changename")
        self.aftername = QtWidgets.QLineEdit(self.groupBox_4)
        self.aftername.setGeometry(QtCore.QRect(100, 30, 121, 20))
        self.aftername.setText("")
        self.aftername.setObjectName("aftername")
        self.changeBox = QtWidgets.QComboBox(self.groupBox_4)
        self.changeBox.setGeometry(QtCore.QRect(100, 70, 121, 22))
        self.changeBox.setObjectName("changeBox")
        self.changeBox.addItem("")
        self.changeBox.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 20))
        self.label_3.setObjectName("label_3")
        self.changepwd = QtWidgets.QLineEdit(self.groupBox_4)
        self.changepwd.setGeometry(QtCore.QRect(100, 50, 121, 20))
        self.changepwd.setText("")
        self.changepwd.setObjectName("changepwd")
        user.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 23))
        self.menubar.setObjectName("menubar")
        user.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user)
        self.statusbar.setObjectName("statusbar")
        user.setStatusBar(self.statusbar)

        self.retranslateUi(user)
        QtCore.QMetaObject.connectSlotsByName(user)
        # 表格禁止编辑
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def retranslateUi(self, user):
        _translate = QtCore.QCoreApplication.translate
        user.setWindowTitle(_translate("user", "用户设置"))
        self.groupBox.setTitle(_translate("user", "查询用户"))
        self.label.setText(_translate("user", "输入用户名称："))
        self.find.setText(_translate("user", "查询"))
        self.label_2.setText(_translate("user", "输入用户类型："))
        self.find_2.setText(_translate("user", "查询"))
        self.groupBox_2.setTitle(_translate("user", "添加用户"))
        self.add.setText(_translate("user", "添加"))
        self.label_4.setText(_translate("user", "输入名称："))
        self.label_6.setText(_translate("user", "输入类型："))
        self.label_5.setText(_translate("user", "输入密码："))
        self.comboBox.setItemText(0, _translate("user", "普通用户"))
        self.comboBox.setItemText(1, _translate("user", "管理员"))
        self.groupBox_3.setTitle(_translate("user", "删除用户"))
        self.delete_2.setText(_translate("user", "删除"))
        self.label_7.setText(_translate("user", "输入用户名称："))
        self.refresh.setText(_translate("user", "刷新"))
        self.groupBox_4.setTitle(_translate("user", "修改用户"))
        self.change.setText(_translate("user", "修改"))
        self.label_10.setText(_translate("user", "输入修改后密码："))
        self.label_9.setText(_translate("user", "输入修改后类型："))
        self.label_8.setText(_translate("user", "输入修改后名称："))
        self.changeBox.setItemText(0, _translate("user", "普通用户"))
        self.changeBox.setItemText(1, _translate("user", "管理员"))
        self.label_3.setText(_translate("user", "输入原用户名称："))
