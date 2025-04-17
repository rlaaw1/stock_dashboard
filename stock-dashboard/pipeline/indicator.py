
import ta,pandas as pd
from config import *
bars=db().execute("SELECT * FROM bars").df()
latest=bars.groupby("Ticker").last().reset_index()
latest["RSI14"]=ta.momentum.rsi(latest["Close"], window=14)
latest["SMA50"]=ta.trend.sma_indicator(latest["Close"], window=50)
latest.to_parquet(ROOT/"latest.parquet", index=False)
print("✓ indicator done")
