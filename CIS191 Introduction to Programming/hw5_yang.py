import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


#Part 1: Read Data & Understand Data
def read_data(file):
    f = open(file)
    f.seek(0)
    all_data = f.read()
    all_data_list = all_data.split('\n')
    data = [x.split(',') for x in all_data_list[1:] if x != '']
    price = [float(d[1]) for d in data]
    f.close()
    return price


def read_date(file):
    f = open(file)
    f.seek(0)
    all_data = f.read()
    all_data_list = all_data.split('\n')
    data = [x.split(',') for x in all_data_list[1:] if x != '']
    date = [d[0] for d in data]
    f.close()
    return date


#Part 2: Bookkeepings
def make_transaction(account, price, quantity, buy):
    if buy:
        if price * quantity > account['balance']: #buying more stock that values more than your balance
            trans_quantity = account['balance'] / price
        else:
            trans_quantity = quantity
        account['balance'] -= price * trans_quantity
        account['stock_quantity'] += trans_quantity
        print('Buy:buying: {} stock'.format(round(trans_quantity)))
        print('{}: {}, {}: {}, {}: {}'.format('Current balance', round(account['balance'], 2),
                                              'current stock', round(account['stock_quantity']),
                                              'current total', round(account['balance']+account['stock_quantity']*price, 2)))
    else:
        if quantity > account['stock_quantity']: #selling more stocks than you already have
            trans_quantity = account['stock_quantity']
        else:
            trans_quantity = quantity
        account['balance'] += price * trans_quantity
        account['stock_quantity'] -= trans_quantity
        print('Sell:selling: {} stock'.format(round(trans_quantity)))
        print('{}: {}, {}: {}, {}: {}'.format('Current balance', round(account['balance'], 2),
                                              'current stock', round(account['stock_quantity']),
                                              'current total', round(account['balance']+account['stock_quantity']*price, 2)))


#Part 3: Trading with Moving Average Algorithm
def get_sma(prices):
    nday = 10
    sma_data = [0] * len(prices)
    for i in range(nday, len(prices)):
        sma_data[i] = sum(prices[i - nday:i]) / nday
    return sma_data


def trade(prices, sma, account):
    quantity = 10
    trans_entry = [0] * len(prices)
    for i in range(10, len(prices)):
        if prices[i] <= (1-0.05) * sma[i]: #buy
            make_transaction(account, prices[i], quantity, True)
            trans_entry[i] = 1
        elif prices[i] >= (1+0.05) * sma[i]: #sell
            make_transaction(account, prices[i], quantity, False)
            trans_entry[i] = -1
        else:
            trans_entry[i] = 0
    return trans_entry


def buyorsell(entry, prices):
    buy = [0] * len(entry)
    sell = [0] * len(entry)
    for i in range(len(entry)):
        if entry[i] == 1:
            buy[i] = prices[i]
        if entry[i] == -1:
            sell[i] = prices[i]
    return buy, sell


#Part 4: Plotting
def make_plot(dates, prices, sma, sell, buy):
    dates = pd.to_datetime(dates)
    DF = pd.DataFrame()
    DF['prices'] = prices
    DF['sma'] = sma
    DF['sell'] = sell
    DF['buy'] = buy
    DF = DF.set_index(dates)

    plt.figure(figsize=(12, 5))
    plt.title('Facebook 1 Year Stock Price and SMA')
    plt.plot(DF['prices'], linestyle='-', color='black', linewidth=1.8, label='FB_Stockprice')
    plt.plot(DF['sma'], linestyle='--', color='blue', linewidth=1.8, label='FB_sma')
    plt.plot(DF['sell'], 'r.', markersize=6.8, label='Sell')
    plt.plot(DF['buy'], 'g.', markersize=6.8, label='Buy')
    plt.ylim(100, 400)
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    plt.show()


#Part 5: Main
def main():
    initial_value = 1000
    initial_quantity = 0
    account = {'balance': initial_value, 'stock_quantity': initial_quantity}
    prices = read_data('input.csv')
    dates = read_date('input.csv')
    sma = get_sma(prices)
    records = trade(prices, sma, account)
    print(records)
    buy, sell = buyorsell(records, prices)
    make_plot(dates, prices, sma, sell, buy)


main()