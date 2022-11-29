def sma(prices, nday):
    sma_data = [0] * len(prices)
    for i in range(nday, len(prices)):
        sma_data[i] = sum(prices[i - nday:i]) / nday
    return sma_data


def read_data(file):
    f = open(file)
    f.seek(0)
    all_data = f.read()
    all_data_list = all_data.split('\n')
    data = [x.split(',') for x in all_data_list[1:] if x != '']
    dates = [d[0] for d in data]
    prices = [float(d[5]) for d in data]
    f.close()
    return dates, prices


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def makeplot(dates, prices, data_sma1, data_sma2):
    dates = pd.to_datetime(dates)
    DF = pd.DataFrame()
    DF['prices'] = prices
    DF['sma1'] = data_sma1
    DF['sma2'] = data_sma2
    DF = DF.set_index(dates)

    plt.figure(figsize=(12, 5))
    plt.title('Costco Wholesale Corporation (COST) 1 Year Data and SMA')
    plt.plot(DF['prices'], linestyle='--', color='red', linewidth=2.0, label='COST')
    plt.plot(DF['sma1'], color='green', linestyle='-.', linewidth=3.0, label='COST_sma10')
    plt.plot(DF['sma2'], 'bo', markersize=1.2, label='COST_sma50')
    plt.ylim(250, 400)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.savefig('cost_sma10_sma50.png')
    plt.show()


def zero_to_nan(values):
    return [float('nan') if x == 0 else x for x in values]


def main():
    dates, prices = read_data('COST.csv')
    data_sma1 = zero_to_nan(sma(prices, 10))
    data_sma2 = zero_to_nan(sma(prices, 50))
    makeplot(dates, prices, data_sma1, data_sma2)


main()