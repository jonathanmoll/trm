import numpy as np


class ValueAtRisk:
    """ Class with static value at risk calculation methods """

    @staticmethod
    def var_1d(spot_portfolio_values:  np.ndarray, daily_market_rates: np.ndarray) -> float:
        """ calculates 1day VaR based on spot portfolio values and daily market rates

        Args:
            spot_portfolio_values: 1-d array with spot portfolio values
            daily_market_rates: 2-d array where the number of columns equals the array-length of spot_portfolio_values

        Returns:
            1 day VaR

        """
        market_rate_shifts = daily_market_rates[:-1, :] / daily_market_rates[1:, :] - 1
        pnl_vectors = market_rate_shifts * spot_portfolio_values
        total_pnl = np.sum(pnl_vectors, axis=1)
        sorted_pnl = np.sort(total_pnl)
        return 0.4 * sorted_pnl[1] + 0.6 * sorted_pnl[2]
