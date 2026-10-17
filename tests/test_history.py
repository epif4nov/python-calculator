from calculator.history import History


def test_history_order_and_clear():
    history = History()
    history.add_entry("1 + 2 = 3")
    history.add_entry("3 / 0 = error")
    assert history.get_all() == ["1 + 2 = 3", "3 / 0 = error"]
    history.clear()
    assert history.get_all() == []


def test_history_snapshot_cannot_mutate_storage():
    history = History()
    history.add_entry("original")
    snapshot = history.get_all()
    snapshot.append("external mutation")
    assert history.get_all() == ["original"]
