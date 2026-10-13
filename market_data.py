import yfinance as yf


def get_market_data(symbols: list[str]) -> dict:

    market_data = {}

    for symbol in symbols:

        try:

            stock = yf.Ticker(symbol)
            info = stock.info

            market_data[symbol] = {
                "company": info.get("longName"),
                "symbol": symbol,
                "current_price": info.get("currentPrice"),
                "market_cap": info.get("marketCap"),
                "pe_ratio": info.get("trailingPE"),
                "dividend_yield": info.get("dividendYield"),
                "sector": info.get("sector"),
                "industry": info.get("industry"),
                "currency": info.get("currency")
            }

        except Exception as e:

            market_data[symbol] = {
                "error": str(e)
            }

    return market_data