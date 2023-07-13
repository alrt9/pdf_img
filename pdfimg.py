
#pip install PyMuPDF==1.19.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
import os
import sys
import fitz  # fitz就是pip install PyMuPDF
import win32api,win32con

def pdfzimg(dir_pdf,dir_name, pdf_name):
    '''
    dir_pdf: D:\\a\\test.pdf
    dir_name: D:\\a
    pdf_name:test.pdf
    '''
    #创建路径
    os.mkdir(dir_pdf[:-4])
    pdf = fitz.open(dir_pdf)
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]  # 获得每一页的对象
        zoom = 3 # 值越大，生成图像像素越高
        trans = fitz.Matrix(zoom, zoom).preRotate(0)
        pm = page.getPixmap(matrix=trans, alpha=False)  # 获得每一页的流对象
        #print(dir_pdf[:-4] + os.sep + pdf_name[:-4] + '_' + '{:0>3d}.{}'.format(pg+1, 'png'))
        pm.writePNG(dir_pdf[:-4] + os.sep + pdf_name[:-4] + '_' + '{:0>3d}.{}'.format(pg+1, 'png'))  # 保存图片
    pdf.close()
    win32api.MessageBox(0, "转换完成", "提示",win32con.MB_OK)



def edit_dir(dir_pdf):
    pdf_name = os.path.basename(dir_pdf)
    dir_name = os.path.dirname(dir_pdf)
    return dir_pdf,dir_name,pdf_name



if __name__ == "__main__":
    # 1、PDF地址
    filedir= sys.argv[1]
    suffix = os.path.splitext(filedir)[-1]
    if suffix == ".pdf":
        a,b,c = edit_dir(filedir)
        pdfzimg(a,b,c)
    else:
        win32api.MessageBox(0, "文件必须是PDF文件", "提示",win32con.MB_OK)
