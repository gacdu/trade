# coding:utf-8

import baostock as bs
import pandas as pd

# 从证券宝获取股票数据，地址http://baostock.com

# 登陆系统
lg = bs.login()

# 获取沪深A股历史K线数据 
rs = bs.query_history_k_data_plus("sh.600000",
    "code,date,open,high,low,close,volume",
    start_date='2022-01-01', end_date='2022-12-31',
    frequency="d", adjustflag="3")

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

# 结果集输出到csv文件
result.to_csv("sh600000.csv", index=False)

# 登出系统
bs.logout()