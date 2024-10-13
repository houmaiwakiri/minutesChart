import json

import sys
import os

from modules.getStockData import getStockData

# Lambdaのハンドラ関数
def lambda_handler(event, context):
    # src配下をパスに追加
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
    
    # eventからsymbolを取得(デフォルトでAPPLE)
    # contextは、Lambda関数の実行環境に関する情報
    symbol = event.get('symbol', 'AAPL') 

    # getStockDataを呼び出し、symbolを渡す
    stock_data = getStockData(symbol)

    return {
        'statusCode': 200,
        'body': json.dumps(f'OK Lambda! {stock_data}')
    }
