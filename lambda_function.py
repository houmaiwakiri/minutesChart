import json

from modules.getStockData import getStockData

# Lambdaのハンドラ関数
def lambda_handler(event, context):
    # src配下をパスに追加
    
    # eventからsymbolを取得(デフォルトでAPPLE)
    # contextは、Lambda関数の実行環境に関する情報
    symbol = event.get('symbol', 'AAPL') 

    # getStockDataを呼び出し、symbolを渡す
    stock_data = getStockData(symbol)

    return {
        'statusCode': 200,
        'body': json.dumps(f'OK Lambda! {stock_data}')
    }
