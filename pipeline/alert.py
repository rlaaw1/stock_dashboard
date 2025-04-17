from notion_client import Client
import pandas as pd
from config import *
notion=Client(auth=TOKEN)
last2=db().execute("SELECT * FROM bars ORDER BY Datetime DESC LIMIT 120").df()
prev=last2.groupby("Ticker").nth(1)["Close"]
curr=last2.groupby("Ticker").nth(0)["Close"]
change=((curr-prev)/prev*100).abs()
for t,pct in change.items():
    if pct>=3:
        notion.pages.create(parent={"database_id":DB_ALERT},properties={
            "종목":{"title":[{"text":{"content":t}}]},
            "DateTime":{"date":{"start":NOW.isoformat()}},
            "Price":{"number":float(curr[t])},
            "Change%":{"number":round(float(pct),2)}
        })
        print("ALERT",t,pct)
