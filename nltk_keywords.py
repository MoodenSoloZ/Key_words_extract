# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:57:56 2019

@author: lenovo
"""
import re
import nltk
import codecs
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk.stem import PorterStemmer
import collections
from nltk.stem import WordNetLemmatizer

def clean_en_text(text):#文本正则化，去除文本中的符号类
    # 保留英文，数字和空格
    comp = re.compile('[^A-Z^a-z^0-9^ ]')
    return comp.sub(' ', text)

def key_words_extract(txt):#关键词提取
    stop_words = stopwords.words('english')
    txt=clean_en_text(txt)
    txt=nltk.word_tokenize(txt)#分词
    filtered_txt = [w for w in txt if not w in stop_words]#去停词（the,a,is之类的词）
    
    new_filtered_txt=[]
    for w in filtered_txt:#去复数形式
        lemmatizer = WordNetLemmatizer()
        new_filtered_txt.append(lemmatizer.lemmatize(w))
        
    tags = pos_tag(new_filtered_txt)#加标签
    
    NN_words=[]
    for i in range(len(tags)):
        if len(tags[i][0])>=3 and (tags[i][1]=='NN'):#选择标签为NN和NNP并且长度大于3的名词
            NN_words.append(tags[i][0])
    print(NN_words)
    NN_single_word=list(set(NN_words))#先集合化再列表化，将原名词集转变为只有不重复的列表形式
    NN_weight=[]#每个名词的权重
    
    for i in range(len(NN_single_word)):#注意range(x)表示从0到x-1的所有整数，包含x-1
        flag=0
        num=1
        for j in range(len(NN_words)):
            if flag==0:
                if NN_single_word[i]==NN_words[j]:
                    first=j
                    last=j
                    flag=1
            else:
                if NN_single_word[i]==NN_words[j]:
                    last=j
                    num=num+1
        NN_weight.append(10*num+last-first)
        
    
    '''for i in range(len(NN_single_word)):#注意range(x)表示从0到x-1的所有整数，包含x-1
        for j in range(len(NN_words)):        
            if NN_single_word[i]==NN_words[j]:
                NN_first.append(j)
                break
    for i in range(len(NN_single_word)):
        last=0
        num=0
        for j in range(len(NN_words)):        
            if NN_single_word[i]==NN_words[j]:
                last=j
                num=num+1
        NN_frq.append(num)
        NN_last.append(last)
    for i in range(len(NN_single_word)):
        NN_span.append(NN_last[i]-NN_first[i])
    for i in range(len(NN_single_word)):
        NN_weight.append(NN_span[i]+NN_frq[i]*10)'''




    for i in range(len(NN_single_word)):
        for j in range(len(NN_single_word)-1-i):
            if NN_weight[j]<=NN_weight[j+1]:
                x=NN_weight[j]
                NN_weight[j]=NN_weight[j+1]
                NN_weight[j+1]=x
            
                y=NN_single_word[j]
                NN_single_word[j]=NN_single_word[j+1]
                NN_single_word[j+1]=y
    dict_NN=dict(zip(NN_single_word,NN_weight))
    return NN_single_word[0:5]
    

if __name__ == "__main__":
    f=codecs.open('D:\\test2.txt','r','utf-8')
    t=f.read()
    print(key_words_extract(t))


            
    







