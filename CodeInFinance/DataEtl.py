import pandas as pd
import urllib2 as ul
import datetime
import matplotlib.pyplot as plt


def download_yahoo_stock(ticker):
    print('starting download: ' + ticker)
    try:
        assert isinstance(ticker, basestring)
        url = 'http://ichart.yahoo.com/table.csv?s=' + ticker
        response = ul.urlopen(url)
        text = response.read()
        return text
    except:
        print('ticker not found: ' + ticker)


def load_yahoo_stock(response_string):
    assert isinstance(response_string, basestring)
    date = []
    openquote = []
    high = []
    low = []
    close = []
    volume = []
    adjclose = []
    for line in response_string.splitlines():
        data = line.split(',')
        if data[0]=="Date":
            continue
        year = int(data[0][0:4])
        month = int(data[0][5:7])
        day = int(data[0][8:10])
        date.append(datetime.datetime(year, month, day))
        openquote.append(float(data[1]))
        high.append(float(data[2]))
        low.append(float(data[3]))
        close.append(float(data[4]))
        volume.append(float(data[5]))
        adjclose.append(float(data[6]))
    openquote.reverse()
    high.reverse()
    low.reverse()
    close.reverse()
    volume.reverse()
    adjclose.reverse()
    date.reverse()
    return date, openquote, high, low, close, volume, adjclose


def calc_daily_returns(closequote):
    assert isinstance(closequote, list)
    daily_returns = [0]
    for i in range(1, len(closequote)):
        daily_returns.append((closequote[i]-closequote[i-1])/closequote[i-1])
    return daily_returns


if __name__ == "__main__":
    t = download_yahoo_stock("nflx")
    date, openq, h, l, c, v, a = load_yahoo_stock(t)
    ret = calc_daily_returns(c)
    print (len(ret), len(date))
    plt.plot(date, ret)
    plt.show()
