import yfinance as yf
stocks = {
    "WIPRO.BO": {"avg_price": 249.60, "quantity": 20},
    "TATASTEEL.BO": {"avg_price": 171.62, "quantity": 5}
}
metals = {
    "GOLDINR=X": {"avg_price": 12000, "grams": 0.294},
}
invested = 0
total = 0
for stock in stocks:
    print(stocks[stock]["avg_price"])
    total += yf.Ticker(stock).fast_info['lastPrice'] * stocks[stock]["quantity"]
    invested += stocks[stock]["avg_price"] * stocks[stock]["quantity"]
print('TOTAL:',total, 'INVESTED:', invested)
for metal in metals:
    print(yf.Ticker(metal))

