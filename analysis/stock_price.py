# coding:utf-8

import numpy as np


class TestNumpy:

    def __init__(self) -> None:
        self.fname = "sh600000.csv"

    # 读取文件
    def read_file(self, m, n):
        col, col_other = np.loadtxt(fname=self.fname, delimiter=',', skiprows=1, usecols=(m, n), unpack=True)
        return col, col_other

    # 计算最大值、最小值
    def max_min(self):
        hight, low = self.read_file(3, 4)
        print(f"最大值：{hight.max()}")
        print(f"最小值：{low.min()}")

    # 计算最高价的极差、最低价的极差
    def max_min_ptp(self):
        hight, low = self.read_file(3, 4)
        print("最高价的极差：", np.ptp(hight))
        print("最低价的极差：", np.ptp(low))

    # 计算成交量加权平均价格
    def vwap(self):
        close, volumn = self.read_file(5, 6)
        avg = np.average(close)
        vwap = np.average(close, weights=volumn)
        print("平均价格：", avg)
        print("成交量加权平均价格：", vwap)

    # 计算收盘价中位数
    def median(self):
        close, _ = self.read_file(5, 6)
        median = np.median(close)
        print("中位数：", median)

    # 计算收盘价方差
    def var(self):
        close, _ = self.read_file(5, 6)
        var = np.var(close)
        print("收盘价方差：", var)

    # 计算波动率
    def volatility(self):
        close, _ = self.read_file(5, 6)
        # 对数波动率
        log_return = np.diff(np.log(close))
        # 年化波动率
        annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250)
        # 月化波动率
        monthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12)
        print("对数波动率：", log_return)
        print("年化波动率：", annual_volatility)
        print("月化波动率：", monthly_volatility)


if __name__ == '__main__':
    t = TestNumpy()
    t.volatility()