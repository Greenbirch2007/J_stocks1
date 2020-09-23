import time

from selenium import webdriver
import pyautogui

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





if __name__ == '__main__':
    big_list = []
    driver = webdriver.Chrome()
    full_items = read_xlrd(excelFile='js_dustry.xlsx')
    for item in full_items:
        code_num =item[1]
        name =item[0]
        pic_name =code_num+name
        print(code_num)

    #     url = 'https://kabutan.jp/stock/chart?code={0}'.format(code_num)   # 直接到登录界面！
    #
    #     driver.get(url)
    #     pyautogui.keyDown("pagedown")  # 按下往下
    #
    #     time.sleep(1)  # 每三秒往下翻一页
    #     ele = driver.find_element_by_id("kc_area")
    #     ele.screenshot('{0}.png'.format(pic_name))  # 元素截图
    # driver.quit()
    #
    #
