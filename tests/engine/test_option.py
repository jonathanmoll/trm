from datetime import date

from pytest import fixture, approx

from trm.engine.option import VanillaOption


@fixture(scope='module')
def option_strike_st_s0() -> VanillaOption:
    return VanillaOption(date(2022, 11, 23), date(2023, 1, 10), 19, 17, 0.005, 0.35)


@fixture(scope='module')
def option_strike_et_s0() -> VanillaOption:
    return VanillaOption(date(2022, 11, 23), date(2023, 1, 10), 19, 19, 0.005, 0.35)


@fixture(scope='module')
def option_strike_gt_s0() -> VanillaOption:
    return VanillaOption(date(2022, 11, 23), date(2023, 1, 10), 19, 21, 0.005, 0.35)


def test_strike_smaller_than_so(option_strike_st_s0):
    # test call price
    assert option_strike_st_s0.call_price == approx(2.247748815, 1e-6)
    # test put price
    assert option_strike_st_s0.put_price == approx(0.236602241, 1e-6)


def test_equal_to_than_so(option_strike_et_s0):
    # test call price
    assert option_strike_et_s0.call_price == approx(0.967349492, 1e-6)
    # test put price
    assert option_strike_et_s0.put_price == approx(0.954891556, 1e-6)


def test_strike_greater_than_so(option_strike_gt_s0):
    # test call price
    assert option_strike_gt_s0.call_price == approx(0.313324743, 1e-6)
    # test put price
    assert option_strike_gt_s0.put_price == approx(2.299555446, 1e-6)
