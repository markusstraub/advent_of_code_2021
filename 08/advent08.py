import more_itertools
from collections import namedtuple

NoteEntry = namedtuple("NoteEntry", "patterns output")


def gen_note_entries(filename="test_advent08.txt"):
    """return test data if no file is given"""
    with open(filename) as file:
        for line in file:
            tokens = line.strip().split(" | ")
            yield NoteEntry(tokens[0].split(" "), tokens[1].split(" "))


def count_1478(entries):
    """simply count how often 1, 4, 7 or 8 are contained in the output"""
    count = 0
    for entry in entries:
        by_len = more_itertools.map_reduce(entry.output, keyfunc=len, reducefunc=len)
        only_1478 = {k: v for k, v in by_len.items() if k in [2, 3, 4, 7]}
        count += sum(only_1478.values())
    return count


def subtract_string(stringa, stringb):
    return "".join(set(stringa).difference(set(stringb)))


def is_subset(stringa, stringb):
    return set(stringa).issubset(set(stringb))


def decode(entry):
    by_len = more_itertools.map_reduce(entry.patterns, keyfunc=len)
    digit2code = {}

    # decode trivial parts
    digit2code[1] = by_len.get(2)[0]
    digit2code[4] = by_len.get(4)[0]
    digit2code[7] = by_len.get(3)[0]
    digit2code[8] = by_len.get(7)[0]

    # 0, 6, 9 use six segments each
    candidates = by_len.get(6)

    code = filter(lambda x: is_subset(digit2code[4], x), candidates)
    digit2code[9] = list(code)[0]

    subtracted = subtract_string(digit2code[8], digit2code[7])
    code = filter(lambda x: is_subset(subtracted, x), candidates)
    digit2code[6] = list(code)[0]

    remaining = set(candidates).difference([digit2code[6], digit2code[9]])
    digit2code[0] = list(remaining)[0]

    # 2, 3, 5 use five segments each
    candidates = by_len.get(5)

    code = filter(lambda x: is_subset(digit2code[1], x), candidates)
    digit2code[3] = list(code)[0]

    subtracted = subtract_string(digit2code[9], digit2code[1])
    code = filter(lambda x: is_subset(subtracted, x), candidates)
    digit2code[5] = list(code)[0]

    remaining = set(candidates).difference([digit2code[3], digit2code[5]])
    digit2code[2] = list(remaining)[0]

    return _convert(digit2code, entry.output)


def _sort(code):
    return "".join(sorted(set(code)))


def _intlist2int(list):
    return int("".join([str(i) for i in list]))


def _convert(digit2code, codes):
    code2digit = {_sort(v): k for k, v in digit2code.items()}
    ints = [code2digit[_sort(code)] for code in codes]
    return _intlist2int(ints)


if __name__ == "__main__":
    count = count_1478(gen_note_entries("advent08.txt"))
    print(f"part1: found {count} instances of 1, 4, 7 or 8 in the entries' outputs")

    decoded = [decode(entry) for entry in gen_note_entries("advent08.txt")]
    print(f"part2: sum of all decoded outputs is {sum(decoded)}.")
