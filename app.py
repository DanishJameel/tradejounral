import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64
from PIL import Image
import io

# Excel file path - use absolute path for better reliability
FILE_PATH = os.path.join(os.getcwd(), "US100_Trade_Journal_Entries.xlsx")
# Screenshots directory
SCREENSHOTS_DIR = "trade_screenshots"

# Create screenshots directory if it doesn't exist
if not os.path.exists(SCREENSHOTS_DIR):
    os.makedirs(SCREENSHOTS_DIR)

# Load or create DataFrame with better error handling
def load_data():
    try:
        if os.path.exists(FILE_PATH):
            # Read Excel with string dtype for Trade ID to avoid type conflicts
            df = pd.read_excel(FILE_PATH, dtype={'Trade ID': str})
            st.success(f"✅ Data loaded successfully from {FILE_PATH}")
            return df
        else:
            st.info(f"📝 Creating new Excel file at {FILE_PATH}")
            columns = [
                "Trade ID", "Date/Time", "Market Bias", "Trade Type", "Setup/Strategy Name",
                "Entry Price", "Exit Price", "Stop Loss (SL)", "Take Profit (TP)", "Lot Size",
                "Risk ($ or %)", "Reward ($ or %)", "Result (Win/Loss/BE)", "P/L ($)", "R Multiple",
                "Emotional State (Before)", "Emotional State (During)", "Emotional State (After)",
                "Execution Grade", "Screenshot (Entry/Exit)", "Mistake Made? (Yes/No + What?)",
                "Lesson Learned", "Next Action Plan",
                "Session", "News Impact (Yes/No)", "Slippage", "Volatility Measure",
                "Market Conditions", "Time in Trade", "Confidence Rating (1–10)", "Screenshot Path"
            ]
            df = pd.DataFrame(columns=columns)
            # Save the empty dataframe to create the file
            save_data(df)
            return df
    except Exception as e:
        st.error(f"❌ Error loading data: {e}")
        # Return empty dataframe as fallback
        columns = [
            "Trade ID", "Date/Time", "Market Bias", "Trade Type", "Setup/Strategy Name",
            "Entry Price", "Exit Price", "Stop Loss (SL)", "Take Profit (TP)", "Lot Size",
            "Risk ($ or %)", "Reward ($ or %)", "Result (Win/Loss/BE)", "P/L ($)", "R Multiple",
            "Emotional State (Before)", "Emotional State (During)", "Emotional State (After)",
            "Execution Grade", "Screenshot (Entry/Exit)", "Mistake Made? (Yes/No + What?)",
            "Lesson Learned", "Next Action Plan",
            "Session", "News Impact (Yes/No)", "Slippage", "Volatility Measure",
            "Market Conditions", "Time in Trade", "Confidence Rating (1–10)", "Screenshot Path"
        ]
        return pd.DataFrame(columns=columns)

# Save DataFrame with better error handling
def save_data(df):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
        
        # Save to Excel with explicit engine
        df.to_excel(FILE_PATH, index=False, engine='openpyxl')
        st.success(f"💾 Data saved successfully to {FILE_PATH}")
        return True
    except Exception as e:
        st.error(f"❌ Error saving data: {e}")
        return False

# Function to save uploaded image
def save_screenshot(uploaded_file, trade_id):
    if uploaded_file is not None:
        try:
            # Create filename with trade ID and timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{trade_id}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            
            # Save the image
            with open(filepath, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"📸 Screenshot saved: {filename}")
            return filepath
        except Exception as e:
            st.error(f"❌ Error saving screenshot: {e}")
            return None
    return None

# Function to display image
def display_image(image_path):
    if image_path and os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            st.image(image, caption="Trade Screenshot", use_column_width=True)
            return True
        except Exception as e:
            st.error(f"Error loading image: {e}")
            return False
    return False

# Function to delete image
def delete_screenshot(image_path):
    if image_path and os.path.exists(image_path):
        try:
            os.remove(image_path)
            return True
        except Exception as e:
            st.error(f"Error deleting image: {e}")
            return False
    return False

# Streamlit UI
st.set_page_config(page_title="US100 Trade Journal", layout="wide")
st.title("📈 US100 Trade Journal")

# Display file path info for debugging
st.sidebar.markdown("### 📁 File Information")
st.sidebar.write(f"**Excel File:** {FILE_PATH}")
st.sidebar.write(f"**Screenshots:** {SCREENSHOTS_DIR}")

# Add a refresh button to reload data
if st.sidebar.button("🔄 Refresh Data"):
    st.rerun()

st.markdown("Enter your trade details below. All data will be saved to an Excel file.")

# Load data at the start
data = load_data()

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

    st.markdown("### 📸 Screenshot Upload")
    
    screenshot_file = st.file_uploader(
        "Upload Trade Screenshot (PNG, JPG, JPEG)", 
        type=['png', 'jpg', 'jpeg'],
        help="Upload a screenshot of your trade entry/exit or chart analysis"
    )
    
    if screenshot_file:
        st.success(f"✅ Screenshot uploaded: {screenshot_file.name}")
        # Display preview
        image = Image.open(screenshot_file)
        st.image(image, caption="Screenshot Preview", width=300)

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
        if not trade_id:
            st.error("Please enter a Trade ID!")
        else:
            # Check if trade ID already exists
            if not data.empty and trade_id in data['Trade ID'].values:
                st.error(f"Trade ID '{trade_id}' already exists! Please use a unique Trade ID.")
            else:
                # Save screenshot if uploaded
                screenshot_path = None
                if screenshot_file:
                    screenshot_path = save_screenshot(screenshot_file, trade_id)
                
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
                    "Confidence Rating (1–10)": confidence,
                    "Screenshot Path": screenshot_path
                }
                
                # Add new trade to dataframe
                data = pd.concat([data, pd.DataFrame([new_trade])], ignore_index=True)
                
                # Save the updated dataframe
                if save_data(data):
                    st.success("✅ Trade saved successfully!")
                    st.balloons()
                    # Clear form by rerunning
                    st.rerun()
                else:
                    st.error("❌ Failed to save trade. Please try again.")

# Display existing entries with screenshot functionality
st.markdown("### 📄 Current Journal Entries")

if not data.empty:
    st.write(f"📊 Total trades recorded: {len(data)}")
    
    # Add screenshot display and deletion functionality
    for index, row in data.iterrows():
        with st.expander(f"Trade ID: {row['Trade ID']} - {row['Date/Time']} - {row['Result (Win/Loss/BE)']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                # Display trade details
                st.write(f"**Market Bias:** {row['Market Bias']}")
                st.write(f"**Trade Type:** {row['Trade Type']}")
                st.write(f"**Entry Price:** {row['Entry Price']}")
                st.write(f"**Exit Price:** {row['Exit Price']}")
                st.write(f"**P/L:** ${row['P/L ($)']}")
                st.write(f"**Result:** {row['Result (Win/Loss/BE)']}")
                st.write(f"**Execution Grade:** {row['Execution Grade']}")
                
                if pd.notna(row['Lesson Learned']):
                    st.write(f"**Lesson Learned:** {row['Lesson Learned']}")
            
            with col2:
                # Screenshot section
                st.markdown("**📸 Screenshot**")
                screenshot_path = row.get('Screenshot Path')
                
                if screenshot_path and pd.notna(screenshot_path):
                    if display_image(screenshot_path):
                        # Delete button
                        if st.button(f"🗑️ Delete Screenshot", key=f"delete_{index}"):
                            if delete_screenshot(screenshot_path):
                                # Remove from dataframe
                                data.at[index, 'Screenshot Path'] = None
                                save_data(data)
                                st.success("Screenshot deleted successfully!")
                                st.rerun()
                else:
                    st.info("No screenshot uploaded for this trade")
    
    # Display full dataframe with error handling
    st.markdown("### 📊 Complete Trade Data")
    try:
        # Convert dataframe to string representation for display to avoid Arrow issues
        display_data = data.copy()
        # Ensure all columns are string type for display
        for col in display_data.columns:
            display_data[col] = display_data[col].astype(str)
        st.dataframe(display_data, use_container_width=True)
    except Exception as e:
        st.error(f"Error displaying dataframe: {e}")
        # Fallback: show as text
        st.text("Data loaded but display error occurred. Use download button to view data.")
    
    # Add download button for Excel file
    if st.button("📥 Download Excel File"):
        try:
            # Create a download link for the Excel file
            with open(FILE_PATH, "rb") as file:
                excel_data = file.read()
            
            st.download_button(
                label="📥 Download US100_Trade_Journal_Entries.xlsx",
                data=excel_data,
                file_name="US100_Trade_Journal_Entries.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"Error creating download link: {e}")
else:
    st.info("No trades recorded yet. Start by adding your first trade above!")