import matplotlib.pyplot as plt
import numpy as np
from pandas import read_csv

# pred = np.load('./data/pred.npy')
# label = np.load('./data/label.npy')
#
# plt.figure(figsize=(10, 5))  # 设置图形的大小
# plt.plot(pred, label='Pred')  # 绘制输出Y的走向曲线（假设Y是收盘价）
# plt.plot(label, label='True')
# plt.xlabel('Day')  # 设置x轴标签
# plt.ylabel('Price')  # 设置y轴标签
# plt.title('Stock Price Trend')  # 设置图形标题
# plt.legend()  # 添加图例
# plt.grid(True)  # 显示网格线
# plt.show()  # 显示图形
stock_data = read_csv('data/000001SH_index.csv')

plt.plot(stock_data['close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Close Price')
plt.show()