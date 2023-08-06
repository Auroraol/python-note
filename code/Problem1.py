import warnings  # 忽略警告
warnings.filterwarnings('ignore')

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA

def run():
    #1. 导入数据并查看基本信息
    df = pd.read_csv('CL=F.csv')
    print(df.head())
    print(df.info())

    # 2. 将日期转换为时间序列索引，并绘制趋势图
    # 转换日期列的数据类型为日期时间
    df['Date'] = pd.to_datetime(df['Date'])
    # 设置日期列为索引
    df.set_index('Date', inplace=True)
    # 将Close列作为目标变量
    target_variable = df['Close']
    plt.plot(target_variable)
    plt.show()

    def test_stationarity(timeseries):
        # 计算移动平均和移动标准差
        rolmean = timeseries.rolling(window=12).mean()
        rolstd = timeseries.rolling(window=12).std()

        # 绘制移动平均和移动标准差图
        plt.plot(timeseries, color='blue', label='Original')
        plt.plot(rolmean, color='red', label='Rolling Mean')
        plt.plot(rolstd, color='black', label='Rolling Std')
        plt.legend(loc='best')
        plt.title('Rolling Mean & Standard Deviation')
        plt.show()

        # 进行ADF检验
        print('Results of ADF test:')
        dftest = adfuller(timeseries, autolag='AIC')
        dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
        for key, value in dftest[4].items():
            dfoutput['Critical Value ({})'.format(key)] = value
        print(dfoutput)

        # 绘制ACF和PACF图
        plot_acf(timeseries)
        plot_pacf(timeseries)
        plt.show()

    # 对Close变量进行平稳性检验
    test_stationarity(target_variable)

    # 从移动平均、移动标准差和ADF检验的结果中可以看出，数据不是完全平稳的。同时，ACF和PACF图上也存在明显的自相关性和偏自相关性。

    # 为了使数据平稳，我们可以对原数据进行差分处理。一般来说，如果一阶差分能够使数据平稳，则无需进行更高阶差分。
    # 对Close变量进行一阶差分
    df_diff = target_variable.diff().dropna()
    test_stationarity(df_diff)

    # 从移动平均、移动标准差和ADF检验的结果中可以看出，差分后的数据已经基本平稳了，同时ACF和PACF图上也不存在明显的自相关性和偏自相关性。

    # 确定模型参数
    # 在确定ARIMA模型的参数时，需要考虑以下三个因素：自回归项（AR）、差分项（I）和移动平均项（MA）。

    # 我们可以通过观察ACF和PACF图来确定模型参数。具体方法如下：
    #
    # ACF图上第一个超过置信区间的点为Q值，表示移动平均项的阶数（MA）；
    # PACF图上第一个超过置信区间的点为P值，表示自回归项的阶数（AR）；
    # 差分次数I可以通过观察差分后的数据是否平稳来确定。

    # 确定AR和MA的阶数
    fig, ax = plt.subplots(figsize=(12, 8))
    ax = plt.subplot(211)
    sm.graphics.tsa.plot_acf(df_diff, lags=40, ax=ax)
    ax = plt.subplot(212)
    sm.graphics.tsa.plot_pacf(df_diff, lags=40, ax=ax)
    plt.show()
    #从ACF和PACF图中可以看出，AR阶数可能是1或2，MA阶数可能是1或2。

    # 6. 拟合ARIMA模型并进行预测
    #拟合ARIMA模型
    target_variable = target_variable.asfreq('D')  # 将数据转换为每日频率
    model = ARIMA(target_variable, order=(2, 1, 1))
    model_fit = model.fit()

    # 预测未来30天的价格
    day = 30
    predictions = model_fit.predict(start=len(target_variable), end=len(target_variable)+day-1, dynamic=False)

    #  输出预测结果
    print(predictions)

    # 绘制实际观测值
    #plt.plot(df.index, target_variable, label='Actual')
    date_range = pd.date_range(start='2023-06-10', periods=len(predictions))
    # 绘制预测结果
    plt.plot(date_range, predictions, label='Predictions')

    # 设置图例和标签
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')

    # 显示图形
    plt.show()

    # 构建包含预测结果的DataFrame
    forecast_dates = pd.date_range(start=target_variable.index[-1], periods=day+1, freq='D')[1:]  # 构建预测日期范围
    predictions_df = pd.DataFrame({'Date': forecast_dates, 'Predicted Price': predictions})

    # 保存预测结果到CSV文件
    predictions_df.to_csv('predictions.csv', index=False)




