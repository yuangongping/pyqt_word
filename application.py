# coding: utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QStackedWidget, QDesktopWidget, QListWidget, QApplication, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from view.manager import Manager
from view.statusBar import StatusBar
from view.aboutMe import AboutMePanel


class MainWindowApp(QMainWindow, QWidget):
    def __init__(self, parent=None):
        # 执行当前函数的初始化函数
        super(MainWindowApp, self).__init__(parent)

        self.init_name()
        # 设置位置，以及显示大小
        self.init_size_position()

        # 状态栏
        self.statusbar = StatusBar()
        self.setStatusBar(self.statusbar.statusbar)

        # 设置整体容器的布局为水平布局
        self.main_layout = QHBoxLayout()
        # 设置容器的外边距
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.init_sidebar()

        """  右侧面--堆栈式组件  """
        self.right_widget = QStackedWidget()
        # *****************************        创建项目管理面板实例
        self.manager_panel = Manager()

        self.manager_panel = Manager()  # 创建线程
        self.manager_panel.signal.connect(self.updateStatusBarStatus)  # 连接信号
        self.manager_panel.start()  # 开始线程
        # 右侧面板中添加项目管理组件, !!!!! 注意， 一定要放置在监听start的后面， 否则不能起作用
        self.right_widget.addWidget(self.manager_panel.Qwidgetlayout)

        # ***************************  关于我们 面板
        self.aboutmepanel = AboutMePanel()
        self.right_widget.addWidget(self.aboutmepanel.main)

        # --------------------------------  整体布局容器中添加右侧面板
        self.main_layout.addWidget(self.right_widget)

        # -------------------------------  整体的布局容器
        self.main_frame = QWidget()
        self.main_frame.setLayout(self.main_layout)
        self.setCentralWidget(self.main_frame)
        # 界面创建函数
        self._setup_left_panel()

    def init_name(self):
        # 设置窗口名称
        self.setObjectName('智能实验报告生成工具')
        # 设置窗口图标
        self.setWindowIcon(QIcon('favicon.ico'))
        # 设置窗口显示的名称
        self.setWindowTitle('智能实验报告生成工具')

    def init_size_position(self):
        """
        获取电脑的尺寸，实现自适应宽度， 高度，以及位置
        :return:
        """
        self.available_geometry = QDesktopWidget().availableGeometry()
        # 设置窗口的宽度为电脑屏幕的0.45 倍
        init_width = self.available_geometry.width() * 0.8
        # 设置窗口的高度为电脑屏幕的0.45 倍
        init_height = self.available_geometry.height() * 0.8
        # 设置宽度与高度
        self.resize(init_width, init_height)

    def init_sidebar(self):
        """
        设置侧边栏
        :return:
        """
        with open('style/QListWidgetQss.qss', 'r') as f:
            list_style = f.read()
        # 创建列表组件
        self.left_widget = QListWidget()
        # 设置列表组件的css样式
        self.left_widget.setStyleSheet(list_style)
        self.left_widget.setFocus()
        # 将侧边栏组件添加到容器中
        self.main_layout.addWidget(self.left_widget)

    def leftsidebar_change(self):
        """
        左边侧边栏点击后响应事件
        :return:
        """
        # 获取当前点击的左侧侧边栏的序号
        i = self.left_widget.currentIndex().row()
        if i == 0:
            pass
        elif i == 1:
            # 当为采集结果显示面板时， 先清空面板，然后写入数据
            self.result_panel.clearTable()
            self.result_panel.selectionchange(0)
        elif i == 2:
            self.update()
        else:
            pass
        # # 更新ceche的配置参数
        # self.manager_panel.update_cache()
        # 右侧的堆叠面板的设置为第i个显示
        self.right_widget.setCurrentIndex(i)

    def _setup_left_panel(self):
        """
        构建左侧侧边栏QList面板
        :return:
        """
        # 去掉边框
        self.left_widget.setFrameShape(QListWidget.NoFrame)
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        nav_list = ['信息录入',  '关于我们']
        nav_list_icons = ["collection.png", "aboutme.png"]
        for nav, icon_name in zip(nav_list, nav_list_icons):
            # 左侧选项的添加
            self.item = QListWidgetItem(QIcon("./img/{}".format(icon_name)), nav, self.left_widget)
            self.item.setSizeHint(QSize(20, 60))
            # 居中显示
            # self.item.setTextAlignment(Qt.AlignCenter)
        self.left_widget.setIconSize(QSize(22, 22))
        self.left_widget.itemClicked.connect(self.leftsidebar_change)

    def updateStatusBarStatus(self, text):
        """
        更新状态栏
        :param text: 状态栏上显示的txt
        :return:
        """
        self.statusbar.statusbar.showMessage(text)
        self.statusbar.statusbar.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_wnd = MainWindowApp()
    main_wnd.show()
    sys.exit(app.exec())
