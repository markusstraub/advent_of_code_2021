import itertools
import more_itertools

test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class DiagnosticBitSum:
    @staticmethod
    def zero():
        return DiagnosticBitSum([0])

    @staticmethod
    def from_string(string):
        int_array = [int(bit) for bit in list(string)]
        return DiagnosticBitSum(int_array)

    def __init__(self, int_array):
        self.int_array = int_array

    def __add__(self, other):
        return DiagnosticBitSum(
            [
                a + b
                for a, b in itertools.zip_longest(
                    self.int_array, other.int_array, fillvalue=0
                )
            ]
        )

    def calc_gamma(self, record_count):
        bits = [1 if val > (record_count - val) else 0 for val in self.int_array]
        return DiagnosticBitSum(bits)

    def calc_epsilon(self, record_count):
        bits = [1 if val < (record_count - val) else 0 for val in self.int_array]
        return DiagnosticBitSum(bits)

    def calc_power_consumption(self, record_count):
        return (
            self.calc_gamma(record_count).to_decimal()
            * self.calc_epsilon(record_count).to_decimal()
        )

    def to_decimal(self):
        result = 0
        current_bit_value = 1
        for bit in reversed(self.int_array):
            result += current_bit_value * bit
            current_bit_value *= 2
        return result

    def __repr__(self):
        strings = [str(bit) for bit in self.int_array]
        return "".join(strings)


def gen_diagnostics(filename=None):
    """return list of bits (as int), test data if no file is given"""
    if filename is None:
        yield from (
            DiagnosticBitSum.from_string(line) for line in test_input.split("\n")
        )
    else:
        with open(filename) as file:
            for line in file:
                yield DiagnosticBitSum.from_string(line.strip())


if __name__ == "__main__":
    filename = "advent03.txt"
    record_count = more_itertools.ilen(gen_diagnostics(filename))
    print(f"found {record_count} diagnostic bits.")

    accumulated = DiagnosticBitSum.zero()
    for bits in gen_diagnostics(filename):
        accumulated += bits

    power_consumption = accumulated.calc_power_consumption(record_count)
    print(f"part1: submarine power consumption is {power_consumption}.")
