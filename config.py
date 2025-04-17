
import os, duckdb, pathlib, datetime as dt
ROOT = pathlib.Path(__file__).parent
CACHE = ROOT / "cache.duckdb"
TICKERS = os.getenv("TICKERS","AAPL").split(",")
NOW = dt.datetime.now()
TOKEN = os.environ["NOTION_TOKEN"]
DB_PRICE = os.environ["NOTION_PRICE_DB_ID"]
DB_ALERT = os.environ["NOTION_ALERT_DB_ID"]
DB_NEWS  = os.environ.get("NOTION_NEWS_DB_ID","")
DB_REP   = os.environ["NOTION_REPORT_DB_ID"]
_duck=None
def db():
    global _duck
    if _duck is None:
        _duck=duckdb.connect(CACHE)
    return _duck
