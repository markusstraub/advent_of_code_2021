from advent03 import DiagnosticBitSum, gen_diagnostics
import os


def test_diagnostic_bits():
    zero = DiagnosticBitSum.zero()
    assert repr(zero) == "0"
    bits_a = DiagnosticBitSum.from_string("01001")
    bits_b = DiagnosticBitSum([1, 1, 1, 0, 0])

    assert repr(zero + bits_a) == "01001"
    assert repr(bits_a + zero) == "01001"
    assert repr(bits_a + bits_b) == "12101"


def test_to_decimal():
    assert DiagnosticBitSum.from_string("00000").to_decimal() == 0
    assert DiagnosticBitSum.from_string("00001").to_decimal() == 1
    assert DiagnosticBitSum.from_string("01010").to_decimal() == 10
    assert DiagnosticBitSum.from_string("11111").to_decimal() == 31


def test_rates_and_power_consumption():
    accumulated = DiagnosticBitSum.zero()
    for bits in gen_diagnostics():
        accumulated += bits

    gamma = accumulated.calc_gamma(record_count=12)
    assert repr(gamma) == "10110"
    assert gamma.to_decimal() == 22

    epsilon = accumulated.calc_epsilon(record_count=12)
    assert repr(epsilon) == "01001"
    assert epsilon.to_decimal() == 9

    assert accumulated.calc_power_consumption(record_count=12) == 198
