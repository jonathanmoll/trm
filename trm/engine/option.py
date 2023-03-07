import math
from datetime import date

from scipy.stats import norm


class VanillaOption:
    """ Class for calculating the put and call price of european vanilla options

    Attributes:
        _s0 (float): stock price at time t=0
        _k (float): strike price
        _t (float): time to maturity
        _r (float): continuous compounded risk-free rate
        _vol (float): volatility
        _call_price (float): call option price
        _put_price (float): put option price

    """

    def __init__(self,
                 trade_date: date,
                 expiry_date: date,
                 stock_price_t0: float,
                 strike_price: float,
                 risk_free_rate: float,
                 volatility: float):
        """ Initializes the object by setting the class attributes

        Args:
            trade_date: trade date
            expiry_date: expiry date
            stock_price_t0: stock price at t0
            strike_price: strike price
            risk_free_rate: annualized risk-free rate
            volatility: volatility of the stock
        """

        self._s0 = stock_price_t0
        self._k = strike_price
        self._t = (expiry_date - trade_date).days / 365
        self._r = math.log(1 + risk_free_rate)
        self._vol = volatility
        self._call_price = None
        self._put_price = None

    @property
    def call_price(self) -> float:
        """ Returns the call option price """
        if self._call_price is None:
            self._calc_call_price()
        return self._call_price

    @property
    def put_price(self) -> float:
        """ Returns the put option price """
        if self._put_price is None:
            self._calc_put_price()
        return self._put_price

    def _d1(self) -> float:
        """ Returns d1 of the bs-equation """
        numerator = math.log(self._s0 / self._k) + (self._r + (self._vol ** 2) / 2) * self._t
        denominator = self._vol * self._t ** (1/2)
        return numerator / denominator

    def _d2(self, d1: float = None) -> float:
        """ Returns d2 of the bs-equation

        Args:
            d1: d1 of the option value equation, if None, d1 is (re)calculated.

        """
        if d1 is None:
            d1 = self._d1()
        return d1 - self._vol * self._t ** (1/2)

    def _calc_call_price(self):
        """ Calculates the option call price with bs-equation and sets class attribute _call_price """
        d1 = self._d1()
        d2 = self._d2(d1)
        self._call_price = norm.cdf(d1) * self._s0 - norm.cdf(d2) * self._k * math.exp(-self._r * self._t)

    def _calc_put_price(self):
        """ Calculates the option put price with put call parity and sets class attribute _put_price """
        if self._call_price is None:
            self._calc_call_price()
        self._put_price = self._call_price - self._s0 + self._k * math.exp(-self._r * self._t)


