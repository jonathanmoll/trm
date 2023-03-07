import numpy as np


class ValueAtRisk:

    @staticmethod
    def var_1d(spot_portfolio_values:  np.ndarray, daily_market_rates: np.ndarray) -> float:

        market_rate_shifts = daily_market_rates[:-1, :] / daily_market_rates[1:, :] - 1
        pnl_vectors = market_rate_shifts * spot_portfolio_values
        total_pnl = np.sum(pnl_vectors, axis=1)
        sorted_pnl = np.sort(total_pnl)
        return 0.4 * sorted_pnl[1] + 0.6 * sorted_pnl[2]
