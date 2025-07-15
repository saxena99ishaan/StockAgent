import yfinance as yf


def getHistoricalData(symbol,period,interval):

    ticker = yf.Ticker(symbol)
    historical_data = ticker.history(period=period,interval=interval)
    
    return {
        "period":period,
        "interval":interval,
        "data":historical_data.to_json()
        }

def getStockAllData(symbol:str) -> dict:
    
    """
    Get the historical data of a stock symbol, for four different periods and intervals (1 day - 1 minute, 1 week - 60 minutes, 1 month - 1 day, 3 months - 1 day) with the provided symbol. The returned data is a list of key value pairs, where for each element, the keys are period, interval and the python dataframe representing the respective record
    """
    
    dataIntervals = {
        '3mo':'1d',
        '1mo':'1d',
        '1wk':'60m',
        '1d':'1m'
        }
    allData = []
    for period,interval in dataIntervals.items():
        allData.append(getHistoricalData(symbol,period,interval))
        
    return {"historical_data":allData}


print(getStockAllData('COCH'))