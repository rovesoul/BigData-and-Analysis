"""
首先升级你的pip
    终端输入:pip install --upgrade pip
其次安装akshare 库
    终端输入:pip install akshare
然后就能运行这段代码了.

撰写时间:20200202
"""

import akshare as ak
import pandas as pd
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)


def wangyi():
    # 网易数据接口
    while True:
        eye=input('查看实时数据输入1; 查看历史输入2,输入其他退出')
        if eye==str(1):
            epidemic_163_df_now= ak.epidemic_163(indicator="实时")
            print(epidemic_163_df_now,'\n')
        elif eye==str(2):
            epidemic_163_df_history = ak.epidemic_163(indicator="历史")
            print(epidemic_163_df_history, '\n')
        else:
            break
        # print(type(epidemic_163_df_now), type(epidemic_163_df_history))

def dxy():
    # 丁香园接口
    while True:
        eye = input('查看全国统计数据输入1; 查看各省市2,输入其他退出')
        if eye==str(1):
            epidemic_dxy_df_info = ak.epidemic_dxy(indicator="info")
            print(epidemic_dxy_df_info, '\n')
        elif eye==str(2):
            epidemic_dxy_df_china = ak.epidemic_dxy(indicator="全国")
            print(epidemic_dxy_df_china, '\n')
        else:
            break

def city():
    # 输入城市/省份查询
    while True:
        city = input("请输入查询城市/省份:")
        try:
            epidemic_dxy_df_beijing= ak.epidemic_dxy(indicator=city)
            print(epidemic_dxy_df_beijing, '\n')
        except Exception as e :
            pass
        break

def news():
    # 最新新闻
    epidemic_dxy_news=ak.epidemic_dxy(indicator='news')
    print(epidemic_dxy_news, '\n')

def phone():
    # 发热门诊电话
    epidemic_dxy_phones = ak.epidemic_dxy(indicator='hospital')
    print(epidemic_dxy_phones, '\n')

def plot():
    # 丁香园的三张图
    ak.epidemic_dxy(indicator='plot')


while True:
    eye = input("------------------------\n查看网易数据输入1;\n查看丁香园数据输入2;\n直接查询某省市的输入3;\n查询最新新闻输入4;\n查询发热门诊输入5;\n查看数据地图发送6;\n输入其他则[退出]\n请输入:")
    if eye==str(1):
        wangyi()
    elif eye == str(2):
        dxy()
    elif eye == str(3):
        city()
    elif eye == str(4):
        news()
    elif eye == str(5):
        phone()
    elif eye == str(6):
        plot()
    else:break
        
