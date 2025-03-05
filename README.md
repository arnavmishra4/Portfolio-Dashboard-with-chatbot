# Stock Market Dashboard & Trading Bot

## Overview
This project encompasses multiple components focused on stock market analysis, prediction, and automation. It includes a stock market dashboard, predictive modeling, an auto-trading bot, and an LLM-based financial analysis tool.

## Features
### 1. **Stock Market Dashboard**
- Scrapes live stock data from the internet to ensure consistent and reliable information.
- Bypasses free APIs that often return inconsistent or garbage data.
- Future improvements include enabling users to add their newly bought stocks.

### 2. **Stock Price Prediction Models**
- **ARIMA Model**: A statistical approach to forecasting future stock prices based on historical trends.
- **RNN LSTM Model**: Leverages deep learning techniques and large datasets to predict stock price movements, accounting for cyclical market behavior.

### 3. **Automated Trading Bot**
- Implements machine learning (ML) and deep learning (DL) models to analyze market trends and execute trades.
- Uses statistical tools to optimize trading decisions based on live market data.
- Conducts backtesting on historical data to evaluate performance before live deployment.

### 4. **LLM for Financial Analysis**
- Extracts financial data from the annual reports of the top 100 companies.
- Processes and cleans data for potential training of a domain-specific large language model (LLM).
- Future work involves structuring the data into a Q&A format for improved model usability.

## Installation & Usage
### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `requests`, `beautifulsoup4`, `tensorflow`, `sklearn`, etc.
- Web scraping setup (e.g., Selenium or BeautifulSoup for dashboard data fetching)

### Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/stock-trading-dashboard.git
cd stock-trading-dashboard

# Install dependencies
pip install -r requirements.txt
```

### Running the Dashboard
```sh
python dashboard.py
```

### Running Stock Price Prediction
```sh
python prediction.py
```

### Running Auto-Trading Bot
```sh
python trading_bot.py
```

## Future Improvements
- Enhance user interactivity in the dashboard by allowing manual stock additions.
- Fine-tune LLM training for better financial insights.
- Optimize auto-trading strategies using reinforcement learning.

## Contributing
Feel free to fork the repository and submit pull requests with improvements!

## License
MIT License
