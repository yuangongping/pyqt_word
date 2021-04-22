# coding: utf-8
from PyQt5.QtWidgets import QWidget, QTableWidget, QDesktopWidget, QAbstractItemView, QHeaderView, QLabel, QLineEdit, \
    QComboBox, QGridLayout, QTableWidgetItem
from PyQt5.QtCore import Qt
import os


class Result(QWidget):
    def __init__(self):
        super(Result, self).__init__()
        # 创建一个表格
        self.tableWidget = QTableWidget()
        self.available_geometry = QDesktopWidget().availableGeometry()
        init_height = self.available_geometry.height() * 0.44
        self.tableWidget.setMinimumHeight(init_height)
        # 设置表格行数
        self.tableWidget.setRowCount(1)
        # 设置表格的列数
        self.tableWidget.setColumnCount(4)
        # 设置水平方向的表头
        self.tableWidget.setHorizontalHeaderLabels(['姓名', '学号', '日期', '操作'])
        # 设置表头高度
        self.tableWidget.horizontalHeader().setFixedHeight(25)
        # 设置表头的背景色
        self.tableWidget.horizontalHeader().setStyleSheet('QHeaderView::section{background:silver}')
        # 设置表格不可更改
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置第二列宽度
        self.tableWidget.setColumnWidth(1, 300)
        # 设置第三列宽度
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 300)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        """-------                 筛选模块              -------------"""
        self.dataAddressLabel = QLabel('数据路径')
        self.dataAddressEdit = QLineEdit()
        self.dataAddressEdit.setFocusPolicy(Qt.NoFocus)

        self.collectDateLabel = QLabel('数据目录')
        self.cb = QComboBox()
        self.updateDataCombobox()
        self.cb.currentIndexChanged.connect(self.selectionchange)

        """--------------------------------------------------------------------------------"""
        self.gridLayout = QGridLayout()
        self.gridLayout.addWidget(self.dataAddressLabel, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.dataAddressEdit, 0, 1, 1, 9)
        self.gridLayout.addWidget(self.collectDateLabel, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.cb, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 10)
        self.main = QWidget()
        self.main.setLayout(self.gridLayout)
        self.selectionchange(0)

    def clearTable(self):
        rows = self.tableWidget.rowCount()
        for i in range(0, rows)[::-1]:
            self.tableWidget.removeRow(i)

    def selectionchange(self, i):
        # 首先清除表格中的数据
        self.clearTable()
        """    获取新的数据填充   """
        path = ''
        # 如果开始列表为空
        if not self.cb.currentText():
            return
        data = ""
        # 先填充表格，后续再在表格中添加数据
        self.tableWidget.setRowCount(len(data))
        for index, item in enumerate(data):
            # 设置表格内容(行， 列) 文字
            self.tableWidget.setItem(index, 0, QTableWidgetItem(item.get("name")))
            # 设置表格内容(行， 列) 文字
            self.tableWidget.setItem(index, 1, QTableWidgetItem(item.get("size")))
            # 设置表格内容(行， 列) 文字
            self.tableWidget.setItem(index, 2, QTableWidgetItem(item.get("date")))
            self.tableWidget.setItem(index, 3, QTableWidgetItem(item.get("num")))

        # 设置当前的数据路径
        self.dataAddressEdit.setText(path)

    def updateDataCombobox(self):
        """
        更新数据目录的下拉框
        :return:
        """
        # 填充前先清空
        self.cb.clear()
        path = ''
        try:
            dataList = os.listdir(path)
            if not dataList:
                # 添加多个项目
                self.cb.addItems([])
            else:
                dir_list = sorted(dataList, key=lambda x: os.path.getmtime(os.path.join(path, x)))
                dir_list.reverse()
                # 添加多个项目
                self.cb.addItems(dir_list)
                # 设置当前的数据路径
                self.dataAddressEdit.setText(path + "/" + dir_list[0])
        except Exception as e:
            # 设置当前的数据路径
            self.dataAddressEdit.setText(path)
            self.cb.addItems([])




