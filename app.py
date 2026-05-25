import streamlit as st
from financials import get_financials
from memo import generate_memo

st.markdown("<style>div[data-testid='stMetricLabel'] p {text-decoration: none;}</style>", unsafe_allow_html=True)
st.title("M&A Deal Screener")
st.caption("Enter two tickers to generate a deal rationale memo")

col1, col2 = st.columns(2)
with col1:
    acquirer_ticker = st.text_input("Acquirer Ticker", "MSFT")
with col2:
    target_ticker = st.text_input("Target Ticker", "ATVI")

if st.button("Generate Deal Memo"):
    with st.spinner("Pulling financials and generating memo..."):
        acquirer = get_financials(acquirer_ticker)
        target = get_financials(target_ticker)

        st.subheader("Financials Snapshot")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**{acquirer['name']}**")
            st.metric("EV/EBITDA", f"{acquirer['ev_ebitda']}x")
            st.metric("EV/Revenue", f"{acquirer['ev_revenue']}x")
            st.metric("P/E", acquirer['pe_ratio'])
        with col2:
            st.write(f"**{target['name']}**")
            st.metric("EV/EBITDA", f"{target['ev_ebitda']}x")
            st.metric("EV/Revenue", f"{target['ev_revenue']}x")
            st.metric("P/E", target['pe_ratio'])

        st.subheader("Deal Rationale Memo")
        memo = generate_memo(acquirer, target)
        st.write(memo)