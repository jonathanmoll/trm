import os

import pandas as pd
from pytest import approx

from trm.engine.var import ValueAtRisk


def test_var_1day():
    data_path = pd.read_excel(os.path.dirname(os.path.abspath(__file__)) + '\\data\\exercise4_test_data.xlsx')
    data_df: pd.DataFrame = data_path
    spot_portfolio_values = data_df[['ccy1', 'ccy2']].iloc[0].to_numpy()
    data_df = data_df.dropna()
    daily_market_rates = data_df[['ccy1', 'ccy2']].to_numpy()
    var_1day = ValueAtRisk.var_1d(spot_portfolio_values, daily_market_rates)
    assert var_1day == approx(-13572.733792, 1e-6)

