import yfinance as yf
from datetime import date

df = yf.download(
    "^GSPC",
    start="2010-01-01",
    end=date.today().strftime("%Y-%m-%d"),
    auto_adjust=True
)

# Remove ticker level from columns
if hasattr(df.columns, "droplevel"):
    df.columns = df.columns.droplevel(1)

df.to_csv("sp500_2010_historical.csv")