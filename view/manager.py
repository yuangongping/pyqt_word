# # coding: utf-8
from PyQt5.QtWidgets import QFormLayout, QWidget, QLabel, QRadioButton, QHBoxLayout, QPushButton, QSpinBox
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from PyQt5.Qt import QLineEdit
from PyQt5.QtCore import pyqtSignal


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
        self.username_input.setText('')
        self.username_input.setFixedWidth(250)
        self.username_input.setFixedHeight(25)
        # 值监听函数
        self.username_input.editingFinished.connect(
            lambda: self.value_changed(
                item={"key": "username", "value": self.username_input.text(), "comment": "用户名"}
            )
        )
        self.manager_layout.addRow(self.username_label, self.username_input)

        self.password_label = QLabel("用户密码：")
        self.password_label.setFont(QFont("Microsoft YaHei"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setText('')
        self.password_input.setFixedWidth(250)
        self.password_input.setFixedHeight(25)

        # 值监听函数
        self.password_input.editingFinished.connect(
            lambda: self.value_changed(
                item={"key": "password", "value": self.password_input.text(), "comment": "密码"}
            )
        )
        self.password_input.installEventFilter(self)
        self.manager_layout.addRow(self.password_label, self.password_input)

        self.host_label = QLabel("采集域名：")
        self.host_label.setFont(QFont("Microsoft YaHei"))
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("多个域名, 使用英文逗号（,）隔开")
        self.host_input.setText('')
        self.host_input.setFixedWidth(450)
        self.host_input.setFixedHeight(25)
        # 值监听函数
        self.host_input.editingFinished.connect(
            lambda: self.value_changed(
                item={"key": "host", "value": self.host_input.text(), "comment": "域名"}
            )
        )
        self.manager_layout.addRow(self.host_label, self.host_input)

        # 标签
        self.collect_type_label = QLabel("采集类型：")
        # 单选框
        self.ridio_zengliang = QRadioButton()
        # 单选框的文字
        self.ridio_zengliang.setText('增量采集')
        # 设置宽度
        self.ridio_zengliang.setFixedWidth(100)
        self.ridio_zengliang.toggled.connect(lambda: self.collection_select(self.ridio_zengliang))

        # 单选框
        self.ridio_quanliang = QRadioButton()
        # 设置文字
        self.ridio_quanliang.setText('全量采集')
        self.ridio_quanliang.setChecked(True)
        # 设置宽度
        self.ridio_quanliang.setFixedWidth(100)
        self.ridio_zengliang.toggled.connect(lambda: self.collection_select(self.ridio_quanliang))

        # 创建水平方向的box布局
        item = QHBoxLayout()
        # 添加单选框组件-增量
        item.addWidget(self.ridio_zengliang)
        # 添加单选框组件-全量
        item.addWidget(self.ridio_quanliang)
        # 行添加
        self.manager_layout.addRow(self.collect_type_label, item)
        label_async_nm = QLabel("同步线程：")
        spinbox = QSpinBox()
        spinbox.setFixedWidth(100)
        spinbox.setFixedHeight(25)
        spinbox.setRange(1, 8)
        spinbox.setSingleStep(1)
        spinbox.setValue(2)
        self.manager_layout.addRow(label_async_nm, spinbox)

        self.network_status_label = QLabel("网络状态：")
        self.network_status_label.setFont(QFont("Microsoft YaHei"))
        self.network_status = QLabel()
        self.manager_layout.addRow(self.network_status_label, self.network_status)

        self.btn_login = QPushButton("启动")
        self.btn_login.setFixedWidth(100)
        self.btn_login.setFixedHeight(30)
        self.btn_login.setFont(QFont("Microsoft YaHei"))
        self.btn_login.setObjectName("login_btn")
        self.manager_layout.addRow(self.btn_login)


    def eventFilter(self, obj, event):
        """
        事件监听函数
        :param obj:
        :param event:
        :return:
        """
        try:
            # 如果为密码输入框的事件
            if obj == self.password_input:
                # 如果事件类型为焦点进入函数
                if event.type() == QEvent.FocusIn:
                    # 将密码输入框的类型改为普通的输入框的类型，达到密码可见的功能
                    self.password_input.setEchoMode(QLineEdit.Normal)
                elif event.type() == QEvent.FocusOut:
                    self.password_input.setEchoMode(QLineEdit.Password)
            else:
                pass
        except:
            pass
        finally:
            return QWidget.eventFilter(self, obj, event)
