from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
import pymysql
import sys
from 团员管理系统.xtwh import setting
from 团员管理系统.service import service
from PyQt5.QtWidgets import *

class MyClass(setting.Ui_user):
    def __init__(self):
        super().__init__()
        self.InitUi()
        self.My_Sql()

    def InitUi(self):
        self.setupUi(self)

        self._translate = QtCore.QCoreApplication.translate
        self.find.clicked.connect(self.query)
        self.find_2.clicked.connect(self.query2)
        self.add.clicked.connect(self.addquery)
        self.delete_2.clicked.connect(self.deletequery)
        self.refresh.clicked.connect(self.refreshquery)
        self.change.clicked.connect(self.changequery)

    def Table_Data(self, i, j, data):

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(i, j, item)
        item = self.tableWidget.item(i, j)
        item.setText(self._translate("Form", str(data)))

    def My_Sql(self):  # 连接mysql数据库
        connection = pymysql.connect(host="localhost", user="cyi", password="cyi", database="db_cyi",charset="utf8")
        print('successfully connect')
        cur = connection.cursor()
        cur.execute('select * from tb_username')  # 将数据从数据库中拿出来
        total = cur.fetchall()
        col_result = cur.description
        self.row = cur.rowcount  # 取得记录个数，用于设置表格的行数
        self.vol = len(total[0])  # 取得字段数，用于设置表格的列数
        col_result = list(col_result)
        a = 0
        self.tableWidget.setColumnCount(self.vol)
        self.tableWidget.setRowCount(self.row)
        for i in col_result:  # 设置表头信息，将mysql数据表中的表头信息拿出来，放进TableWidget中
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(a, item)
            item = self.tableWidget.horizontalHeaderItem(a)
            item.setText(self._translate("Form", i[0]))
            a = a + 1

        total = list(total)  # 将数据格式改为列表形式，其是将数据库中取出的数据整体改为列表形式
        for i in range(len(total)):  # 将相关的数据
            total[i] = list(total[i])  # 将获取的数据转为列表形式
        for i in range(self.row):
            for j in range(self.vol):
                self.Table_Data(i, j, total[i][j])

    def refreshquery(self):
        self.tableWidget.setRowCount(0)
        connection = pymysql.connect(host="localhost", user="cyi", password="cyi", database="db_cyi", charset="utf8")
        print('successfully connect')
        cur = connection.cursor()
        cur.execute('select * from tb_username')  # 将数据从数据库中拿出来
        total = cur.fetchall()
        col_result = cur.description
        self.row = cur.rowcount  # 取得记录个数，用于设置表格的行数
        self.vol = len(total[0])  # 取得字段数，用于设置表格的列数
        col_result = list(col_result)
        a = 0
        self.tableWidget.setColumnCount(self.vol)
        self.tableWidget.setRowCount(self.row)
        for i in col_result:  # 设置表头信息，将mysql数据表中的表头信息拿出来，放进TableWidget中
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(a, item)
            item = self.tableWidget.horizontalHeaderItem(a)
            item.setText(self._translate("Form", i[0]))
            a = a + 1

        total = list(total)  # 将数据格式改为列表形式，其是将数据库中取出的数据整体改为列表形式
        for i in range(len(total)):  # 将相关的数据
            total[i] = list(total[i])  # 将获取的数据转为列表形式
        for i in range(self.row):
            for j in range(self.vol):
                self.Table_Data(i, j, total[i][j])

    #根据姓名查询
    def query(self):
        self.tableWidget.setRowCount(0)
        if self.findname.text()=="":
            result=service.query('select * from tb_username')
        else:
            key = self.findname.text()
            sql="select 用户名称,密码,类型 from tb_username where 用户名称 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(3)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['用户名称','密码','类型'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

    # 根据类型查询
    def query2(self):
        self.tableWidget.setRowCount(0)
        if self.findkind.text()=="":
            result=service.query('select * from tb_username')
        else:
            key = self.findkind.text()
            sql="select 用户名称,密码,类型 from tb_username where 类型 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(3)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['用户名称','密码','类型'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

    def addquery(self):
        print("1")
        name = self.addname.text()
        pwd = self.addpwd.text()
        index = self.comboBox.currentIndex()
        kind = self.comboBox.itemText(index)


        if name != "" and pwd != "":
            sql = "select 用户名称,密码,类型 from tb_username where 用户名称 like '%" + name + "%'"
            result = service.query2(sql)
            if len(result)>0:
                self.addname.setText("")
                QMessageBox.information(None, '提示', '您要添加的用户已经存在，请重新输入！', QMessageBox.Ok)
            else:
                # 执行添加语句
                result = service.exec("insert into tb_username(用户名称,密码,类型) values (%s,%s,%s)", (name, pwd,kind))
                if result > 0:  # 如果结果大于0，说明添加成功

                    QMessageBox.information(None, '提示', '信息添加成功！', QMessageBox.Ok)
        else:
            QMessageBox.warning(None, '警告', '请输入数据后，再执行相关操作！', QMessageBox.Ok)

    def deletequery(self):
        name=self.delname.text()
        if name != "":
            sql = "select 用户名称,密码,类型 from tb_username where 用户名称 like '%" + name + "%'"
            result = service.query2(sql)
            if len(result) > 0:
                result2 = service.exec("delete from tb_username where 用户名称= %s", (name,))
                if result2 > 0:  # 如果结果大于0，说明删除成功

                    QMessageBox.information(None, '提示', '信息删除成功！', QMessageBox.Ok)
                else:
                    QMessageBox.information(None, '提示', '信息删除失败！', QMessageBox.Ok)

            else:
                self.delname.setText("")
                QMessageBox.information(None, '提示', '您要删除的团员不存在，请重新输入！', QMessageBox.Ok)
        else:
            QMessageBox.information(None, '提示', '请重新输入要删除的团员姓名！', QMessageBox.Ok)

    def changequery(self):
        name = self.changename.text()
        if name != "":
            sql = "select 用户名称,密码,类型 from tb_username where 用户名称 like '%" + name + "%'"
            result = service.query2(sql)
            if len(result) > 0:
                result2 = service.exec("delete from tb_username where 用户名称= %s", (name,))
                name2 = self.aftername.text()
                pwd=self.addpwd.text()
                index = self.changeBox.currentIndex()
                kind = self.changeBox.itemText(index)

                if name2 != "" and pwd != "" :
                    sql = "select 用户名称,密码,类型 from tb_username where 用户名称 like '%" + name2 + "%'"
                    result = service.query2(sql)
                    if len(result) > 0:
                        self.aftername.setText("")
                        QMessageBox.information(None, '提示', '您要修改的用户已经存在，请重新输入！', QMessageBox.Ok)
                    else:
                        # 执行添加语句
                        result = service.exec(
                            "insert into tb_username(用户名称,密码,类型) values (%s,%s,%s)", (name2, pwd,kind))
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
                self.changename.setText("")
                QMessageBox.information(None, '提示', '您要修改的团员不存在，请重新输入！', QMessageBox.Ok)
        else:
            QMessageBox.information(None, '提示', '请重新输入要修改的团员姓名！', QMessageBox.Ok)




if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=MyClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
