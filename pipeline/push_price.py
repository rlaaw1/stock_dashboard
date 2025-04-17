from notion_client import Client
from config import *
import pandas as pd

notion = Client(auth=TOKEN)

# 최신 5분 OHLC 한 행 가져오기
df = db().execute("SELECT * FROM bars ORDER BY Datetime DESC").df()
latest = df.groupby("Ticker").first().reset_index()  # 가장 최근값만

for _, row in latest.iterrows():
    notion.pages.create(
        parent={"database_id": DB_PRICE},
        properties={
            "종목":   {"title":[{"text":{"content": row["Ticker"]}}]},
            "Date":  {"date": {"start": str(row["Datetime"]).replace(" ", "T")}},
            "Close": {"number": float(row["Close"])}
        }
    )
print("✓ pushed", len(latest), "rows to Price DB")
