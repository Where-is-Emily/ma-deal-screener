import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment

def generate_memo(acquirer: dict, target: dict) -> str:
    prompt = f"""
You are a senior M&A analyst. Based on the data below, write a concise 
deal rationale memo (3-4 paragraphs) for why {acquirer['name']} might 
acquire {target['name']}. Cover: strategic fit, valuation attractiveness, 
synergy potential, and key risks. Use professional banking language.

ACQUIRER — {acquirer['name']} ({acquirer['ticker']})
Sector: {acquirer['sector']}
Market Cap: ${acquirer['market_cap']:,}
EV/EBITDA: {acquirer['ev_ebitda']}x
EV/Revenue: {acquirer['ev_revenue']}x
P/E: {acquirer['pe_ratio']}

TARGET — {target['name']} ({target['ticker']})
Sector: {target['sector']}
Market Cap: ${target['market_cap']:,}
EV/EBITDA: {target['ev_ebitda']}x
EV/Revenue: {target['ev_revenue']}x
P/E: {target['pe_ratio']}
"""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text