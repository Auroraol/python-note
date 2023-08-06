import numpy as np
import pandas as pd

def run():
    # 读取预测值
    df = pd.read_csv('predictions.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    start_date = '2023-06-12'
    end_date = '2023-06-16'
    data = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    predicted_values = data['Predicted Price']
    print(predicted_values)

    # 读取investing网站的实际数据
    df = pd.read_csv('WTI原油期货历史数据.csv')
    actual_values = df['收盘']        # 选择6/12到6/16日期范围的数据

    print(actual_values) # 打印收盘价格数据

    # 计算均方根误差（RMSE）
    rmse = np.sqrt(np.mean((predicted_values - actual_values) ** 2))

    # 计算平均绝对误差（MAE）
    mae = np.mean(np.abs(predicted_values - actual_values))

    # 计算平均绝对百分比误差（MAPE）
    mape = np.mean(np.abs((predicted_values - actual_values) / actual_values)) * 100

    # 输出评估结果
    print("RMSE:", rmse) #表示预测价格与真实价格之间的平均误差的平方根为
    print("MAE:", mae)   #表示预测价格与真实价格之间的平均绝对误差为
    print("MAPE:", mape) #表示预测价格与真实价格之间的平均绝对百分比误差为