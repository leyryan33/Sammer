import yahoo_finance as yh
import pandas as pd


def main():
    yahoo = yh.Share('VXX')
    historical_prices = yahoo.get_historical('2016-09-01', '2016-09-10')
    price_frame = pd.DataFrame(index= [d['Date'] for d in historical_prices], columns=['Adj_Close'])
    for price_dict in historical_prices:
        price_frame.loc[price_dict['Date'], 'Adj_Close'] = price_dict['Adj_Close']

    price_frame = price_frame.sort_index()
    print price_frame


if __name__ == "__main__":
    main()

