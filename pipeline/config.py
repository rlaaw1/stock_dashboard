import os, duckdb, pathlib, datetime as dt
ROOT = pathlib.Path(__file__).parent
CACHE = ROOT/'cache.duckdb'
TICKERS = os.getenv('TICKERS','AAPL').split(',')
NOW = dt.datetime.now()
TOKEN = os.environ['NOTION_TOKEN']
DB_PRICE = os.environ['NOTION_PRICE_DB_ID']
DB_ALERT = os.environ['NOTION_ALERT_DB_ID']
def db():
    if not hasattr(db,'_conn'):
        db._conn = duckdb.connect(CACHE)
    return db._conn
