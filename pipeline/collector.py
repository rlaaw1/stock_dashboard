from yfinance import download
from config import *
import pandas as pd
raw = download(TICKERS, period="1d", interval="1m", group_by="ticker", progress=False)
bars=[]
for t in TICKERS:
    try:
        df=raw[t].dropna()
        df5=df.resample("5min").agg({"Open":"first","High":"max","Low":"min","Close":"last","Volume":"sum"})
        df5["Ticker"]=t
        bars.append(df5.tail(1))
    except KeyError:
        continue
out = pd.concat(bars).reset_index() 
conn = db()
conn.execute("CREATE TABLE IF NOT EXISTS bars AS SELECT * FROM out LIMIT 0")
conn.append("bars", out)
print("✓ collector saved", len(out))
