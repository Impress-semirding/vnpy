from __future__ import absolute_import
from time import sleep

from six.moves import input

from vnbinance import BinanceApi


if __name__ == '__main__':
    apiKey = '4pYrKcwH0euFSCXbpd9E1II0ItsN08vCdepB5BqEataJFUMaU2clx7KcivGT3RYX'
    secretKey = 'q7hnv6UwpDcHhCG2FUQvwgHKTuQam9bXzDnDL53djvjhfaciC1TipwrJMUfcltGh'
    
    api = BinanceApi()
    api.init(apiKey, secretKey)
    api.start()
    
    # api.queryPing()
    #api.queryTime()
    #api.queryExchangeInfo()
    
    # api.queryDepth('BTCUSDT')
    #api.queryDepth('BTCUSDT')
    #api.queryTrades('BTCUSDT')
    #api.queryAggTrades('BTCUSDT')
    api.queryKlines('BTCUSDT', '1m')
    #api.queryTicker24HR()
    #api.queryTickerPrice()
    #api.queryBookTicker()
    
    # api.queryAccount()
    #api.queryOrder('BTCUSDT', '1231231')
    #api.queryOpenOrders('BTCUSDT')
    #api.queryAllOrders('BTCUSDT')
    #api.queryMyTrades('BTCUSDT')
    
    #api.startStream()
    #api.keepaliveStream('12312312')
    #api.closeStream('123213')
    
    #api.newOrder('BTCUSDT', 'BUY', 'LIMIT', 3000, 1, 'GTC')
    #api.cancelOrder('BTCUSDT', '132213123')
    
    #api.initDataStream(['btcusdt@ticker', 'btcusdt@depth5'])
    #api.initUserStream('NXvaiFwZz2LuKqINVerKOnWaQQG1JhdQNejiZKY9Kmgk4lZgTvm3nRAnXJK7')
    
    input()
