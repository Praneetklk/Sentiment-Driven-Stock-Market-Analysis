import yfinance as yf

def fetch_stock_data(ticker='AAPL', period='5y'):
    data = yf.download(ticker, period=period)
    data.to_csv('data/stock_data.csv')
    print("Data saved.")

if __name__ == "__main__":
    fetch_stock_data()
