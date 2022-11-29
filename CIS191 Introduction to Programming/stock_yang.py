def top_prices(prices, n):
    prices_sorted = sorted(prices)
    prices_sorted = prices_sorted[0:n]
    return prices_sorted

def first_20_stock_prices(symbols, prices):
    for i in range(20):
        print('Symbols: %8s,       Stock Price: %10.2f' % (symbols[i], prices[i]))

def top_quartile_prices(prices):
    prices.sort(reverse=True)
    quartile = len(prices) // 4
    print('The top quartile prices are:', prices[0:quartile])

def visualize(prices):
    from matplotlib import pyplot
    import numpy
    # pyplot.ion()
    pyplot.plot(prices, 'bo', markersize=4)
    pyplot.xticks([])
    pyplot.yticks(numpy.arange(0, round(max(prices)) + 1, 20))
    pyplot.xlabel('')
    pyplot.ylabel('stock prices')
    pyplot.show()

def main():
    #a.
    prices_str = '   16.13\n32.2\n11.65\n39\n13.83\n25.33\n4.99\n13.1\n150\n37.81\n4.81\n4\n32.08\n12.66\n19.54\n48.52\n65.92\n18.2\n13.09\n19.32\n7.63\n2.23\n116.12\n3.66\n73.45\n54.71\n80.07\n15.99\n30.88\n10.91\n87.7\n6.34\n5.36\n20.66\n62.05\n88.98\n4.3\n63.42\n3.89\n34.01\n28.42\n4.69\n15.3\n55.22\n43.48\n11.73\n167.05\n11.17\n18.84\n44.31\n19.38\n29.38\n21.84\n57.59\n41.42\n23.91\n145.28\n14.76\n75.5\n2.32\n112.19\n38.87\n55.61\n13.35\n27.4\n6.49\n40.94\n8.66\n6.59\n45.73\n34.53\n8.47\n71.03\n108.39\n37.06 '
    prices_str[:]
    prices_str = prices_str.strip() # remove preceding and trailing whitespaces using string's 'strip' function
    prices_str
    prices_list = prices_str.split('\n') # use str.split() to convert string to a list, here "\n" is used as the "separator"
    # print(prices_list)
    prices = [eval(x) for x in prices_list] # convert elements in 'prices' from string to number (int or float)
    symbols_str = 'GE\nBAC\nF\nPFE\nPBR\nNWL\nSWN\nVALE\nVMW\nT\nNOK\nCHK\nFE\nPBR.A\nFCX\nKO\nWFC\nCTL\nBBD\nVRX\nCLF\nRAD\nJPM\nAUY\nCL\nVZ\nC\nKIM\nKR\nNLY\nPG\nAKS\nS\nTV\nMRK\nXOM\nWFT\nABT\nJCP\nTAL\nBSX\nGGB\nRRC\nDAL\nGM\nAES\nCAT\nRIG\nMRO\nSO\nRF\nEPD\nKEY\nMS\nJCI\nHPQ\nJNJ\nABX\nLVS\nCIG\nDIS\nEXC\nHAL\nECA\nM\nAG\nX\nMDR\nESV\nTSM\nPHM\nNBR\nMO\nWMT\nMGM'
    symbols = symbols_str.split() # "\n" is considered 'python whitespace', and split() uses any whitespace to split
    # print(symbols)

    #b.
    T5 = top_prices(prices, 5)
    T20 = top_prices(prices, 20)
    print("Top 5 stock prices are {}".format(T5))
    print(f"Top 20 stock prices are {T20}")

    #c.
    first_20_stock_prices(symbols, prices)

    #d.
    top_quartile_prices(prices)

    #e.
    visualize(prices)


if __name__ == '__main__':
    main()