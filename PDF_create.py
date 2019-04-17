# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:51:51 2019

@author: lenovo
"""

from reportlab.platypus import SimpleDocTemplate,Image,Spacer
import os
import nltk_keywords
import extract_text

#import codecs

#f=codecs.open('D:\\test2.txt','r','utf-8')
#t=f.read()
t=extract_text.easy_text_extract("D:\\result3")
key_words=nltk_keywords.key_words_extract(t)
story=[]#建立空白的list
num=0
for filename in os.listdir("D:\\result3\\"):              #listdir的参数是文件夹的路径   
    num=num+1
for i in range(1,num+1):
    print (i) 
    ad="D:\\result3\\result{}.jpg".format(i)
    img = Image(ad) # 读取特定路径的图片
    img.drawHeight =300 #设置读取后图片的高
    img.drawWidth = 530 #设置读取后图片的宽
    story.append(img)# 将图片存储到list中
    story.append(Spacer(240, 10))#添加空白，长度240，宽10

doc = SimpleDocTemplate("D:\\{}{}{}{}{}{}{}{}{}.pdf".format(key_words[0],' ',key_words[1],' ',key_words[2],' ',key_words[3],' ',key_words[4]))
doc.build(story)
