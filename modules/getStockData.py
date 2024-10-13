import requests

def getStockData(symbol):
    API_KEY = '50YZFP26MACWA5BG'
    BASE_URL = 'https://www.alphavantage.co/query'
    
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY,
        "datatype": "json"
    }
    
    response = requests.get(BASE_URL, params=parameters)
    data = response.json()
    
    return data
