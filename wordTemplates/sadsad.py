import re
aa = """ <img src='C:/Users/YGP/Desktop/1.jpeg'>
<img src='C:/Users/YGP/Desktop/1.jpeg'>
<img src='C:/Users/YGP/Desktop/1.jpeg'>
docxtpl  图片docxtpl  图片docxtpl  图片docxtpl  图片docxtpl  图片
"""

imgs = re.findall("<img src='(.+)'>", aa)


from docxtpl import DocxTemplate, InlineImage
tpl = DocxTemplate('实验报告模板.docx')

data = {
    "imgs": imgs
}
for i in range(0, len(data["imgs"])):
    print(data["imgs"][i])
    data["imgs"][i] = InlineImage(tpl, data["imgs"][i])
tpl.render(data)
tpl.save("1的劳动合同.docx")