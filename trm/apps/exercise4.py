
import pandas as pd

from trm.engine.var import ValueAtRisk


def main():

    # read data as dataframe
    data_df: pd.DataFrame = pd.read_excel('input/exercise4_input.xlsx')

    # get spot portfolio values as ndarray
    spot_portfolio_values = data_df[['ccy1', 'ccy2']].iloc[0].to_numpy()

    # get daily market rates as ndarray
    data_df = data_df.dropna()
    daily_market_rates = data_df[['ccy1', 'ccy2']].to_numpy()

    # calculate 1 day var
    var_1day = ValueAtRisk.var_1d(spot_portfolio_values, daily_market_rates)

    # print result to console
    print(var_1day)


if __name__ == '__main__':
    main()
