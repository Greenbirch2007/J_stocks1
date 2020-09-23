# -*- coding:utf-8 -*-
import datetime
import re
import time
import os
import requests
from requests.exceptions import RequestException
from lxml import etree
from selenium import webdriver
import sys
import io
import xlrd


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a',encoding="utf-8")
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")



def get_first_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None





# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):


    selector = etree.HTML(html)
    name = selector.xpath('//*[@id="main"]/div[2]/h1/text()[2]')
    code_url =selector.xpath('//*[@id="main"]/div[2]/h1/a/@href')


    contents = name+code_url
    big_list.append(tuple(contents))
    return contents














#
if __name__ == '__main__':
    lpath = os.getcwd()
    big_list = []


    try:

        for num in range(1,41):
            url = 'https://kabutan.jp/themes/?industry={0}&stc=zenhiritsu&stm=0'.format(num)
            html = get_first_page(url)
            content = parse_stock_note(html)
            print(url)

    except:
        pass
    text_save('{0}\\js_dustry.xlsx'.format(lpath),big_list)









#name_cn,name_eg,assets,debts,mk
# create table nas100_det(
# id int not null primary key auto_increment,
# name_cn varchar(80),
# name_eg varchar(80),
# assets varchar(80),
# debts varchar(80),
# mk varchar(80)
#  ) engine=InnoDB default charset=utf8;

#
# drop table nas100_det;


