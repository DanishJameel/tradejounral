import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Excel file path
FILE_PATH = "US100_Trade_Journal_Entries.xlsx"

# Load or create DataFrame
def load_data():
    if os.path.exists(FILE_PATH):
        return pd.read_excel(FILE_PATH)
    else:
        columns = [
            "Trade ID", "Date/Time", "Market Bias", "Trade Type", "Setup/Strategy Name",
            "Entry Price", "Exit Price", "Stop Loss (SL)", "Take Profit (TP)", "Lot Size",
            "Risk ($ or %)", "Reward ($ or %)", "Result (Win/Loss/BE)", "P/L ($)", "R Multiple",
            "Emotional State (Before)", "Emotional State (During)", "Emotional State (After)",
            "Execution Grade", "Screenshot (Entry/Exit)", "Mistake Made? (Yes/No + What?)",
            "Lesson Learned", "Next Action Plan",
            "Session", "News Impact (Yes/No)", "Slippage", "Volatility Measure",
            "Market Conditions", "Time in Trade", "Confidence Rating (1–10)"
        ]
        return pd.DataFrame(columns=columns)

# Save DataFrame

def save_data(df):
    df.to_excel(FILE_PATH, index=False)

# Streamlit UI
st.set_page_config(page_title="US100 Trade Journal", layout="wide")
st.title("📈 US100 Trade Journal")

st.markdown("Enter your trade details below. All data will be saved to an Excel file.")

with st.form("trade_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        trade_id = st.text_input("Trade ID")
        market_bias = st.selectbox("Market Bias", ["Bullish", "Bearish", "Neutral"])
        trade_type = st.selectbox("Trade Type", ["Buy", "Sell"])
        setup = st.text_input("Setup/Strategy Name")
        session = st.selectbox("Session", ["London", "New York", "Asia"])
        news_impact = st.selectbox("News Impact", ["Yes", "No"])
        volatility = st.text_input("Volatility Measure (e.g. ATR/VIX)")
    with col2:
        entry_price = st.number_input("Entry Price", step=0.1)
        exit_price = st.number_input("Exit Price", step=0.1)
        sl = st.number_input("Stop Loss (SL)", step=0.1)
        tp = st.number_input("Take Profit (TP)", step=0.1)
        lot_size = st.number_input("Lot Size", step=0.1)
        slippage = st.text_input("Slippage")
        market_condition = st.text_input("Market Conditions")
    with col3:
        risk = st.text_input("Risk ($ or %)")
        reward = st.text_input("Reward ($ or %)")
        result = st.selectbox("Result", ["Win", "Loss", "Break Even"])
        pl = st.number_input("Profit/Loss ($)", step=0.1)
        r_multiple = st.number_input("R Multiple", step=0.1)
        time_in_trade = st.text_input("Time in Trade")
        confidence = st.slider("Confidence Rating (1–10)", 1, 10)

    st.markdown("### Emotional & Execution Notes")
    em_before = st.text_input("Emotional State (Before)")
    em_during = st.text_input("Emotional State (During)")
    em_after = st.text_input("Emotional State (After)")
    execution_grade = st.selectbox("Execution Grade", ["A", "B", "C"])
    screenshot_note = st.text_input("Screenshot Notes")
    mistake = st.text_input("Mistake Made? (Yes/No + What?)")
    lesson = st.text_area("Lesson Learned")
    action_plan = st.text_area("Next Action Plan")

    submitted = st.form_submit_button("Save Trade")

    if submitted:
        df = load_data()
        new_trade = {
            "Trade ID": trade_id,
            "Date/Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Market Bias": market_bias,
            "Trade Type": trade_type,
            "Setup/Strategy Name": setup,
            "Entry Price": entry_price,
            "Exit Price": exit_price,
            "Stop Loss (SL)": sl,
            "Take Profit (TP)": tp,
            "Lot Size": lot_size,
            "Risk ($ or %)": risk,
            "Reward ($ or %)": reward,
            "Result (Win/Loss/BE)": result,
            "P/L ($)": pl,
            "R Multiple": r_multiple,
            "Emotional State (Before)": em_before,
            "Emotional State (During)": em_during,
            "Emotional State (After)": em_after,
            "Execution Grade": execution_grade,
            "Screenshot (Entry/Exit)": screenshot_note,
            "Mistake Made? (Yes/No + What?)": mistake,
            "Lesson Learned": lesson,
            "Next Action Plan": action_plan,
            "Session": session,
            "News Impact (Yes/No)": news_impact,
            "Slippage": slippage,
            "Volatility Measure": volatility,
            "Market Conditions": market_condition,
            "Time in Trade": time_in_trade,
            "Confidence Rating (1–10)": confidence
        }
        df = pd.concat([df, pd.DataFrame([new_trade])], ignore_index=True)
        save_data(df)
        st.success("Trade saved successfully!")

# Display existing entries
st.markdown("### 📄 Current Journal Entries")
data = load_data()
st.dataframe(data, use_container_width=True)
