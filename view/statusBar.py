# coding: utf-8
from PyQt5.QtWidgets import QWidget, QStatusBar


class StatusBar(QWidget):
    def __init__(self):
        super(StatusBar, self).__init__()
        self.statusbar = QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet(
            "#statusbar{background-color:white;color:black;border:none;border-radius:2px;font-weight: bloder }")
        self.statusbar.showMessage("空闲")
