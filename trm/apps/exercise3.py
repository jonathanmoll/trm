from typing import Tuple
import pandas as pd

from trm.engine.option import VanillaOption


def add_call_and_put_price(row: pd.Series) -> Tuple[float, float]:
    # create VanillaOption object
    option = VanillaOption(row['trade_date'], row['expiry_date'], row['stock_price_t0'], row['strike_price'],
                           row['risk_free_rate'], row['volatility'])

    # return tuple of call- and put price
    return option.get_call_price(), option.get_put_price()


def main():
    # read excel and convert dates to datetime.date format
    position_df = pd.read_excel('input/exercise3_input.xlsx')
    position_df['trade_date'] = position_df['trade_date'].dt.date
    position_df['expiry_date'] = position_df['expiry_date'].dt.date

    # apply 'add_call_and_put_price' and add results to and of df
    position_df[['call', 'put']] = position_df.apply(add_call_and_put_price, axis=1, result_type='expand')

    # write results to excel
    position_df.to_excel('output/exercise3_output.xlsx', index=False)


if __name__ == '__main__':
    main()
