# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:10:59 2020

@author: Administrator
"""
#Thư viện thao tác với tập tin và thư mục: os
import os
print(dir(os))
#Các hàm cơ bản:
#os.getcwd() trả về thư mục đang hiện hành
os.getcwd()
#os.listdir(), trong dấu () là đường dẫn có thể dẫn đến các thư mục khác
os.listdir()
#os.chdir(), chuyển đến các thư mục khác bằng đường dẫn trong dấu ()
os.chdir("D:\\bt_c4\C4.b13_os_file")
