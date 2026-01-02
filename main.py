from fastapi import FastAPI
import yfinance
import pandas as pd
app = FastAPI()

@app.get("/search/")
async def root(name: str):
    tickersdf = pd.DataFrame(yfinance.Lookup(name).all)
    if tickersdf.to_dict() == {}:
        return {"tickers": []}
    else:
        tickersdict = tickersdf.to_dict()['shortName']
        tickerlist = list(tickersdict.values())
        return {"tickers": cleanTickerList(tickerlist)}

def cleanTickerList(tickerlist):
    return [key for key in tickerlist if not pd.isna(key)]
