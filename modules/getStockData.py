import yfinance as yf

def getStockData(symbol):
    # 銘柄コードに「.T」を付ける（日本株の場合）
    ticker_symbol = symbol + '.T'  # 例: '7203.T'
    
    # yfinanceを使って株価データを取得
    stock_data = yf.Ticker(ticker_symbol)

    # 1分足の履歴データを取得（期間を指定して取得）
    data = stock_data.history(period="1d", interval="1m")  # 1日の1分足データを取得

    return data
