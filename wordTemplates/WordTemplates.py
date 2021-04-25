# coding: utf-8
import os
from docxtpl import DocxTemplate, InlineImage


class Docxtpl(object):
    @staticmethod
    def genarater(data):
        try:

            tpl = DocxTemplate('wordTemplates/实验报告模板.docx')
            for i in range(0, len(data["imgs"])):
                print(data["imgs"][i])
                data["imgs"][i] = InlineImage(tpl, data["imgs"][i])
            tpl.render(data)
            tpl.save("output/{}wlxfp.docx".format(data.get("school_num")))
            return True
        except:
            return False


