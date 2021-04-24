# coding: utf-8
import os
from docxtpl import DocxTemplate, InlineImage


class Docxtpl(object):
    @staticmethod
    def genarater(data):
        try:
            tpl = DocxTemplate('wordTemplates/实验报告模板.docx')
            tpl.render(data)
            tpl.save("output/的劳动合同.docx")
            print("aaaaaaaaaaaaaaaaaaaaaaaa")
            return True
        except:
            return False


