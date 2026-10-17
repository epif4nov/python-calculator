from calculator.cli import run


def test_invalid_number_retries_without_losing_session(monkeypatch, capsys):
    answers = iter(["1", "not a number", "2", "3", "9", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    run()
    output = capsys.readouterr().out
    assert "Ошибка: введите число" in output
    assert "2.0 + 3.0 = 5.0" in output
    assert "До свидания!" in output


def test_zero_division_recorded_in_history(monkeypatch, capsys):
    answers = iter(["4", "7", "0", "9", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    run()
    assert "7.0 / 0.0 = ошибка (деление на ноль)" in capsys.readouterr().out


def test_memory_retries_invalid_input(monkeypatch, capsys):
    answers = iter(["5", "oops", "9", "7", "8", "7", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    run()
    output = capsys.readouterr().out
    assert "Текущее число: 9.0" in output and "Текущее число: 0.0" in output
