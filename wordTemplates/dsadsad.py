from docxtpl import DocxTemplate
tpl = DocxTemplate('实验报告模板.docx')
#这些字段从csv中获取
context = {
   "name": "172.16.1818"
}
tpl.render(context)
tpl.save("的劳动合同.docx")
