import math
from datetime import date

from scipy.stats import norm


class VanillaOption:

    def __init__(self,
                 trade_date: date,
                 expiry_date: date,
                 stock_price_t0: float,
                 strike_price: float,
                 risk_free_rate: float,
                 volatility: float):

        self._s0 = stock_price_t0
        self._k = strike_price
        self._t = (expiry_date - trade_date).days / 365
        self._r = math.log(1 + risk_free_rate)
        self._vol = volatility
        self._call_price = None
        self._put_price = None

    def _d1(self):
        numerator = math.log(self._s0 / self._k) + (self._r + (self._vol ** 2) / 2) * self._t
        denominator = self._vol * self._t ** (1/2)
        return numerator / denominator

    def _d2(self, d1: float):
        return d1 - self._vol * self._t ** (1/2)

    def _calc_call_price(self):
        d1 = self._d1()
        d2 = self._d2(d1)
        self._call_price = norm.cdf(d1) * self._s0 - norm.cdf(d2) * self._k * math.exp(-self._r * self._t)

    def _calc_put_price(self):
        if self._call_price is None:
            self._calc_call_price()
        self._put_price = self._call_price - self._s0 + self._k * math.exp(-self._r * self._t)

    def get_call_price(self):
        if self._call_price is None:
            self._calc_call_price()
        return self._call_price

    def get_put_price(self):
        if self._put_price is None:
            self._calc_put_price()
        return self._put_price

