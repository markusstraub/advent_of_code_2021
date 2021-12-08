from advent08 import gen_note_entries, count_1478, decode


def test_generator():
    entries = list(gen_note_entries())
    assert len(entries) == 11
    assert len(entries[0].patterns) == 10
    assert len(entries[0].output) == 4


def test_count_1478():
    assert count_1478(gen_note_entries()) == 26


def test_decode():
    entries = list(gen_note_entries())
    decoded = [decode(entry) for entry in entries]
    assert decoded == [5353, 8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
