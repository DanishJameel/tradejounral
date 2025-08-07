# 📈 US100 Trade Journal - Streamlit App

A comprehensive trade journal application for tracking US100 trading activities with screenshot support and Excel data persistence.

## 🚀 Features

- **Trade Entry Form**: Complete trade details including entry/exit prices, stop loss, take profit
- **Screenshot Upload**: Upload and store trade screenshots
- **Excel Data Persistence**: All data is automatically saved to Excel file
- **Data Visualization**: View all trades in expandable format with full details
- **Download Functionality**: Download your complete trade journal as Excel file
- **Error Handling**: Robust error handling for data loading and saving

## 📋 Requirements

- Python 3.7+
- Streamlit
- Pandas
- OpenPyXL
- Pillow (PIL)

## 🛠️ Installation

1. **Clone or download the project files**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Local Development

1. **Run the application:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and go to `http://localhost:8501`

## ☁️ Streamlit Cloud Deployment

### Method 1: Direct Upload
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and set:
   - **Main file path**: `app.py`
   - **App URL**: Choose your preferred URL
5. Click "Deploy!"

### Method 2: GitHub Integration
1. Push your code to GitHub
2. Connect your GitHub repository to Streamlit Cloud
3. Deploy automatically

## 📁 File Structure

```
tradejournal/
├── app.py                          # Main application file
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── US100_Trade_Journal_Entries.xlsx # Data file (auto-created)
├── trade_screenshots/              # Screenshots directory (auto-created)
└── README.md                       # This file
```

## 🔧 Data Persistence

### How it works:
- **Excel File**: `US100_Trade_Journal_Entries.xlsx` stores all trade data
- **Screenshots**: Saved in `trade_screenshots/` directory
- **Automatic Saving**: Data is saved immediately after each trade entry
- **Error Recovery**: If file is corrupted, app creates new file with existing data

### Important Notes:
- ✅ **Data persists between app restarts**
- ✅ **Data persists between deployments**
- ✅ **Excel file is automatically created on first use**
- ✅ **Download functionality available**

## 🚨 Troubleshooting

### Data Loss Issues:

1. **Check File Permissions:**
   - Ensure the app has write permissions to the directory
   - Check if the Excel file is not locked by another process

2. **Verify File Path:**
   - The app shows the current file path in the sidebar
   - Make sure the path is accessible

3. **Refresh Data:**
   - Use the "🔄 Refresh Data" button in the sidebar
   - This reloads data from the Excel file

4. **Download Backup:**
   - Always download your Excel file as backup
   - Use the "📥 Download Excel File" button

### Common Issues:

**Issue**: "Error loading data"
- **Solution**: Check if Excel file exists and is not corrupted
- **Action**: Delete the Excel file and restart - it will be recreated

**Issue**: "Error saving data"
- **Solution**: Check disk space and file permissions
- **Action**: Try refreshing the page and saving again

**Issue**: Screenshots not loading
- **Solution**: Check if screenshot files exist in the directory
- **Action**: Re-upload screenshots if needed

## 📊 Data Fields

The application tracks the following trade information:

### Basic Trade Info:
- Trade ID (unique identifier)
- Date/Time
- Market Bias (Bullish/Bearish/Neutral)
- Trade Type (Buy/Sell)
- Setup/Strategy Name

### Price Information:
- Entry Price
- Exit Price
- Stop Loss (SL)
- Take Profit (TP)
- Lot Size

### Results:
- Risk ($ or %)
- Reward ($ or %)
- Result (Win/Loss/Break Even)
- P/L ($)
- R Multiple

### Analysis:
- Emotional State (Before/During/After)
- Execution Grade (A/B/C)
- Mistake Made
- Lesson Learned
- Next Action Plan

### Market Context:
- Session (London/New York/Asia)
- News Impact
- Slippage
- Volatility Measure
- Market Conditions
- Time in Trade
- Confidence Rating

## 🔒 Data Security

- All data is stored locally in Excel format
- Screenshots are stored in local directory
- No data is sent to external servers
- Download your data regularly as backup

## 📞 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure proper file permissions
4. Try refreshing the application

## 🎯 Best Practices

1. **Regular Backups**: Download your Excel file regularly
2. **Unique Trade IDs**: Use unique identifiers for each trade
3. **Complete Data**: Fill in all relevant fields for better analysis
4. **Screenshot Organization**: Use descriptive trade IDs for screenshots

---

**Happy Trading! 📈** 