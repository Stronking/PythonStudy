
# -*- coding: utf-8 -*-
#
#
# import sys
# import importlib
# importlib.reload(sys)
#
# from pdfminer.pdfparser import PDFParser,PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import *
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
#
# '''
# 解析pdf文件，获取文件中包含的各种对象
# '''
#
#
# # 解析pdf文件函数
# def parse(pdf_path):
#     fp = open(pdf_path, 'rb')  # 以二进制读模式打开
#     # 用文件对象来创建一个pdf文档分析器
#     parser = PDFParser(fp)
#     # 创建一个PDF文档
#     doc = PDFDocument()
#     # 连接分析器 与文档对象
#     parser.set_document(doc)
#     doc.set_parser(parser)
#
#     # 提供初始化密码
#     # 如果没有密码 就创建一个空的字符串
#     doc.initialize()
#
#     # 检测文档是否提供txt转换，不提供就忽略
#     if not doc.is_extractable:
#         raise PDFTextExtractionNotAllowed
#     else:
#         # 创建PDf 资源管理器 来管理共享资源
#         rsrcmgr = PDFResourceManager()
#         # 创建一个PDF设备对象
#         laparams = LAParams()
#         device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#         # 创建一个PDF解释器对象
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#
#         # 用来计数页面，图片，曲线，figure，水平文本框等对象的数量
#         num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0
#
#         # 循环遍历列表，每次处理一个page的内容
#         for page in doc.get_pages(): # doc.get_pages() 获取page列表
#             num_page += 1  # 页面增一
#             interpreter.process_page(page)
#             # 接受该页面的LTPage对象
#             layout = device.get_result()
#             for x in layout:
#                 if isinstance(x,LTImage):  # 图片对象
#                     print("图片",x)
#                     num_image += 1
#                 if isinstance(x,LTCurve):  # 曲线对象
#                     print("曲线",x)
#                     num_curve += 1
#                 if isinstance(x,LTFigure):  # figure对象
#                     print("figure",x)
#                     num_figure += 1
#                 if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
#                     print("文本框",x)
#                     num_TextBoxHorizontal += 1  # 水平文本框对象增一
#                     # 保存文本内容
#                     with open(r'test.txt', 'a') as f:
#                         results = x.get_text()
#                         f.write(results + '\n')
#         print('对象数量：\n','页面数：%s\n'%num_page,'图片数：%s\n'%num_image,'曲线数：%s\n'%num_curve,'水平文本框：%s\n'
#               %num_TextBoxHorizontal)


# if __name__ == '__main__':
#     pdf_path = r'C:\Users\fanyu\Desktop\pdf\test.pdf'
#     parse(pdf_path)

# if __name__ == '__main__':
#     path = r'D:\新建文件夹\01758 博骏教育董事名单与其角色和职能.pdf'
#     # path = r'https://www.tencent.com/zh-cn/articles/8003451510737482.pdf'
#     parse(path)


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def pdf2doc(input, output):
    # try:
        with open(input, 'rb') as f:
            parser = PDFParser(f)
            doc = PDFDocument()
            parser.set_document(doc)
            doc.set_parser(parser)
            # 设置初始化密码
            doc.initialize()

            if not doc.is_printable:
                print('2222222222')
                if not doc.is_extractable:
                    print('1111111111')
                    raise PDFTextExtractionNotAllowed
            else:
                rsrcmgr = PDFResourceManager()
                laparams = LAParams()
                device = PDFPageAggregator(rsrcmgr, laparams=laparams)
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in doc.get_pages():
                    interpreter.process_page(page)
                    layout = device.get_result()
                    for x in layout:
                        if isinstance(x, LTTextBoxHorizontal):
                            with open(output, 'a', encoding='utf-8') as f1:
                                # print("aaaaaaaaaa",x)
                                a = x.get_writing_mode()
                                results = x.get_text().replace('\n','')
                                print(a,"\n\n\n\n\n\n",results,"\n\n\n\n\n\n\n")
                                # print(results)
                                # f1.write(results+' ')
        return True
    # except Exception as e:
        # print(e)
        # return False
if __name__ == '__main__':
    input = r'D:\新建文件夹\1.pdf'
    output = r'D:\新建文件夹\519931 长信上证港股通指数更新招募说明书（2018年第2号）.doc'
    rc = pdf2doc(input, output)
    if rc:
        print('转换成功')
    else:
        print('转换失败')



# import tabula
# import chardet
#
# import os
# # f = open(r"D:\新建文件夹\1.pdf",'r',encoding='utf-8')
# l = os.listdir('D:\新建文件夹')
# for x in l:
#     try:
#         p ="D:\新建文件夹\\"+x
#         print(p)
#         pdf = tabula.read_pdf(p,pages="1",encoding='utf-8')
#         # fenc = chardet.detect(f.read())
#         # print(f.read())
#         # print(pdf)
#         print(x,p)
#         for i in pdf.index:
#             print(pdf.loc[i].values[1].strip())
#         # pdf.close()
#     except Exception as e:
#         print(e)
#         continue
