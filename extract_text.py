# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:43:54 2019

@author: lenovo
"""
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
from PIL import Image
import pytesseract
import codecs



def easy_text_extract(imagefile):#使用pytesseract检测图像中的文字
    num=0
    txt=" "
    for filename in os.listdir(imagefile+"\\"):              #listdir的参数是图像文件夹的路径   
        num=num+1
    for i in range(1,num+1):
        print (i) 
        ad="D:\\result2\\result{}.jpg".format(num+1-i)
        image=Image.open(ad)
         
        #result=pytesseract.image_to_string(image,lang='chi_sim')#变图片为字符串
        result=pytesseract.image_to_string(image)#变图片为字符串（默认识别为英文）
        txt=result+txt
       # with open('D:\\test2.txt','a') as f:
        #    f.write("{}{}".format(result,"\n")) 
        f=codecs.open('D:\\test2.txt','a','utf-8')
        f.write("{}{}".format(result,' ')) 
    return txt
    

if __name__ == "__main__":
    txt=easy_text_extract("D:\\result2")
    



























