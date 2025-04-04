import yfinance as yf
import pandas as pd

def get_data(ticker, start_date, end_date, interval):
    # Daten von Yahoo Finance herunterladen
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    
    # Nur 'Close'-Preis auswählen und Index zurücksetzen, um die 'Date'-Spalte zu erhalten
    # 'Close' + 'Volume' auswählen und Index zurücksetzen
    data = data[['Close', 'Volume']].reset_index()

    # Spalten umbenennen
    data.columns = ['Date', 'Closing Price', 'Volume']

    
    return data

def save_to_csv(data, filename):
    # DataFrame als CSV speichern
    data.to_csv(filename, index=False)


    # Liste der Coins (Ticker)
tickers = ['BTC-USD', 'ETH-USD', 'SOL-USD', 'BNB-USD', 'DOGE-USD', 'ADA-USD', 'TRX-USD', 'XRP-USD', 'LINK-USD']
start_date = '2022-01-01'
end_date = '2024-01-01'
interval = '1d'  # tägliche Daten

for ticker in tickers:
    data = get_data(ticker, start_date, end_date, interval)
    # Dateiname: CoinName_2022-2024.csv (nur der Coin-Teil wird aus dem Ticker extrahiert)
    coin_name = ticker.split('-')[0]
    filename = f"{coin_name}_2022-2024.csv"
    save_to_csv(data, filename)
    print(f"Data for {ticker} saved to {filename}")
