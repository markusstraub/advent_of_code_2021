from advent08 import gen_note_entries, count_1478


def test_generator():
    entries = list(gen_note_entries())
    assert len(entries) == 10
    assert len(entries[0].patterns) == 10
    assert len(entries[0].output) == 4


def test_count_1478():
    assert count_1478(gen_note_entries()) == 26
