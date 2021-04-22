# coding: utf-8
from PyQt5.QtWidgets import QMessageBox


class Message(object):
    @classmethod
    def tips(cls, content=None):
        # 创建一个问答框，注意是Question
        cls.box = QMessageBox(QMessageBox.Warning, 'Tips', content)

        # 设置消息框中内容前面的图标
        cls.box.setIcon(1)

        # 设置消息框的位置，大小无法设置
        cls.box.setGeometry(500, 500, 0, 0)
        # 显示该问答框
        cls.box.show()
