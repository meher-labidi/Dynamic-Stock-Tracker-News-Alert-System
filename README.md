# Dynamic Stock Tracker & News Alert System

This project is an automated Python application designed to monitor the stock prices of any specified company and send real-time alerts with relevant news articles if significant price changes are detected. It leverages Alpha Vantage for stock data, NewsAPI for fetching the latest news, and Twilio for sending SMS notifications.

## Features
- Monitor stock prices of any specified company.
- Detect significant changes in stock prices.
- Fetch the latest news articles related to the specified company.
- Send SMS notifications with stock price changes and news headlines.

## Requirements
- Python 3.x
- `requests` library
- `twilio` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dynamic-stock-tracker.git
    ```
2. Navigate to the project directory:
    ```sh
    cd dynamic-stock-tracker
    ```
3. Install the required libraries:
    ```sh
    pip install requests twilio
    ```

## Configuration
1. Set up your environment variables for API keys and tokens:
    - `API_KEY`: Your Alpha Vantage API key.
    - `NEWS_API_KEY`: Your NewsAPI key.
    - `TWILIO_SID`: Your Twilio account SID.
    - `TWILIO_AUTH_TOKEN`: Your Twilio authentication token.
    - `TWILIO_PHONE_NUMBER`: Your Twilio phone number for sending messages.
    - `RECIPIENT_PHONE_NUMBER`: Your phone number to receive messages.

2. Replace the placeholder values in the script with your actual API keys, tokens, and phone numbers.

## Usage
1. Edit the script to specify the stock symbol and company name you want to monitor:
    ```python
    STOCK_NAME = "AAPL"  # Example: Apple Inc
    COMPANY_NAME = "Apple Inc"
    ```

2. Run the script:
    ```sh
    python main.py
    ```

3. The application will monitor the specified company's stock prices and send SMS alerts if significant price changes are detected.
