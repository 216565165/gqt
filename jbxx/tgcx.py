from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem
import pymysql
import sys
from 团员管理系统.jbxx import tgcx_ui
from 团员管理系统.service import service


class MyClass(tgcx_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.InitUi()
        self.My_Sql()

    def InitUi(self):
        self.setupUi(self)
        # self.setWindowTitle("团组织查询")
        # self.show()
        self._translate = QtCore.QCoreApplication.translate
        self.pushButton.clicked.connect(self.query)
        self.pushButton_2.clicked.connect(self.query2)
        self.pushButton_3.clicked.connect(self.query3)
        self.pushButton_4.clicked.connect(self.query4)

    def Table_Data(self, i, j, data):

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(i, j, item)
        item = self.tableWidget.item(i, j)
        item.setText(self._translate("Form", str(data)))

    def My_Sql(self):  # 连接mysql数据库
        connection = pymysql.connect(host="localhost", user="cyi", password="cyi", database="db_cyi",charset="utf8")
        print('successfully connect')
        cur = connection.cursor()
        cur.execute('select * from tb_tg')  # 将数据从数据库中拿出来
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


    #根据团员姓名查询
    def query(self):
        self.tableWidget.setRowCount(0)
        if self.lineEdit.text()=="":
            result=service.query('select * from tb_tg')
        else:
            key = self.lineEdit.text()
            sql="select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员姓名 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['团员姓名', '团员性别', '团员年龄', '团员所属组织', '入团时间', '团员职位'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

    # 根据团员所属组织查询
    def query2(self):
        self.tableWidget.setRowCount(0)
        if self.lineEdit_2.text()=="":
            result=service.query('select * from tb_tg')
        else:
            key = self.lineEdit_2.text()
            sql="select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员所属组织 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['团员姓名', '团员性别', '团员年龄', '团员所属组织', '入团时间', '团员职位'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

    # 根据团员性别查询
    def query3(self):
        self.tableWidget.setRowCount(0)
        if self.lineEdit_3.text()=="":
            result=service.query('select * from tb_tg')
        else:
            key = self.lineEdit_3.text()
            sql="select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员性别 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['团员姓名', '团员性别', '团员年龄', '团员所属组织', '入团时间', '团员职位'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)

# 根据团员职位查询
    def query4(self):
        self.tableWidget.setRowCount(0)
        if self.lineEdit_4.text()=="":
            result=service.query('select * from tb_tg')
        else:
            key = self.lineEdit_4.text()
            sql="select 团员姓名,团员性别,团员年龄,团员所属组织,入团时间,团员职位 from tb_tg where 团员职位 like '%" + key + "%'"
            result=service.query2(sql)
        row = len(result)  # 取得记录个数，用于设置表格的行数
        self.tableWidget.setRowCount(row)  # 设置表格行数
        self.tableWidget.setColumnCount(6)  # 设置表格列数
        # 设置表格的标题名称
        self.tableWidget.setHorizontalHeaderLabels(
            ['团员姓名', '团员性别', '团员年龄', '团员所属组织', '入团时间', '团员职位'])
        for i in range(row):  # 遍历行
            for j in range(self.tableWidget.columnCount()):  # 遍历列
                data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                self.tableWidget.setItem(i, j, data)


if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=MyClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
