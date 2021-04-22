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
                text = """    中电太极（集团）有限公司（简称 “中电太极集团” ） 是国有大型高科技企业集团，是我国“自主可控技术的排头兵、\
软件与信息服务业旗手、信息系统总体的主力军“，多次获得国家科技进步特等奖、 ”全国五一劳动奖章“等国家荣誉。\n
    中电太极集团率属于中国电子科技集团有限公司（十大军工央企之一）， 总部位于北京，旗下拥有中国电子科技集团公司第十五研究所、太极计算股份有限公司等优质产、学、研资源，设有博士后工作站\
和国家重点实验室，在职员工7000余人，服务客户遍及国防、政府、公用事业、公共安全、国民经济重点行业，以及东非、中欧为代表的”一路一带“沿线国家。
                \n地址：北京市海淀区北四环中路211号  电话：010-62162755 邮编： 100083\n管理者邮箱：xxxxxx.cetc.com.cn 版权所有：中国电子科技集团公司 备案序号：京ICP备20031529号"""

        except Exception as e:
            print(e)
        finally:
            self.textEdit.setPlainText(text)
