# M&A Deal Screener

A Python tool that pulls live financial data for any two public companies, 
calculates standard M&A valuation multiples (EV/EBITDA, EV/Revenue, P/E), 
and uses Claude AI to generate a professional deal rationale memo.

Built to replicate the first-pass analysis an investment banking analyst 
would perform when evaluating a potential acquisition target.

## Features
- Live financial data via yfinance (no manual data entry)
- Calculates EV, EV/EBITDA, EV/Revenue, and P/E automatically
- AI-generated deal memo covering strategic fit, valuation, synergies, and risks
- Simple web UI built with Streamlit

## How to Run

1. Install dependencies:
   pip3 install -r requirements.txt

2. Set your Anthropic API key:
   export ANTHROPIC_API_KEY="your-key-here"

3. Launch the app:
   streamlit run app.py

## Example Use Case
Enter any two public company tickers (e.g. MSFT and ATVI) to generate 
a deal rationale memo in seconds.l Screener using AI metrics
