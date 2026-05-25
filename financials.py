import yfinance as yf

def get_financials(ticker):
    co = yf.Ticker(ticker)
    info = co.info

    market_cap = info.get("marketCap", 0)
    total_debt = info.get("totalDebt", 0)
    cash = info.get("totalCash", 0)
    ebitda = info.get("ebitda", 0)
    revenue = info.get("totalRevenue", 0)
    net_income = info.get("netIncomeToCommon", 0)
    pe_ratio = info.get("trailingPE", None)
    name = info.get("longName", ticker)
    sector = info.get("sector", "Unknown")

    ev = market_cap + total_debt - cash
    ev_ebitda = round(ev / ebitda, 2) if ebitda else None
    ev_revenue = round(ev / revenue, 2) if revenue else None

    return {
        "name": name,
        "ticker": ticker.upper(),
        "sector": sector,
        "market_cap": market_cap,
        "enterprise_value": ev,
        "ebitda": ebitda,
        "revenue": revenue,
        "ev_ebitda": ev_ebitda,
        "ev_revenue": ev_revenue,
        "pe_ratio": pe_ratio,
    }