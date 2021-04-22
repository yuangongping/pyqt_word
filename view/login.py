# # coding: utf-8
from PyQt5.QtWidgets import QFormLayout, QWidget, QLabel, QRadioButton, QHBoxLayout, QPushButton, QSpinBox
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.Qt import QLineEdit
from PyQt5.QtCore import pyqtSignal

from init import session


class Manager(QtCore.QThread):
    signal = pyqtSignal(str)

    def __del__(self):
        self.wait()

    def __init__(self):
        # 执行当前类的初始化方法
        super(Manager, self).__init__()
        # 表单组件
        self.manager_layout = QFormLayout()
        # 设置垂直方向的间隙
        self.manager_layout.setVerticalSpacing(20)
        # 容器组件
        self.Qwidgetlayout = QWidget()
        # 设置容器布局为表单布局
        self.Qwidgetlayout.setLayout(self.manager_layout)
        # 这是组件名称
        self.Qwidgetlayout.setObjectName("Qwidgetlayout")
        # 设置容器的外边距
        self.Qwidgetlayout.setContentsMargins(0, 15, 0, 0)

        self.username_label = QLabel("用  户  名：")
        self.username_label.setFont(QFont("Microsoft YaHei"))
        self.username_input = QLineEdit()
        self.username_input.setText(session.get("username"))
        self.username_input.setFixedWidth(250)
        self.username_input.setFixedHeight(25)

        self.manager_layout.addRow(self.username_label, self.username_input)
        self.password_label = QLabel("用户密码：")
        self.password_label.setFont(QFont("Microsoft YaHei"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setText(session.get("password"))
        self.password_input.setFixedWidth(250)
        self.password_input.setFixedHeight(25)
        self.manager_layout.addRow(self.password_label, self.password_input)
        self.btn_login = QPushButton("登录")
        self.btn_login.setFixedWidth(100)
        self.btn_login.setFixedHeight(30)
        self.btn_login.setFont(QFont("Microsoft YaHei"))
        self.btn_login.setObjectName("login_btn")
        self.manager_layout.addRow(self.btn_login)
