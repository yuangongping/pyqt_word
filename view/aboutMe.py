# coding: utf-8
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PyQt5.QtCore import Qt


class AboutMePanel(QWidget):
    """
    关于我们面板
    """
    def __init__(self):
        super(AboutMePanel, self).__init__()
        self.textEdit = QTextEdit()
        # 设置为只读模式
        self.textEdit.setReadOnly(True)
        self.textEdit.setAlignment(Qt.AlignVCenter|Qt.AlignBottom)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textEdit)
        self.main = QWidget()
        self.main.setLayout(self.layout)
        self.setText()

    def setText(self):
        """
        获取最新的日志文件数据展示
        :return:
        """
        text = ""
        try:
                text = "学习使我快乐！"
        except Exception as e:
            print(e)
        finally:
            self.textEdit.setPlainText(text)
