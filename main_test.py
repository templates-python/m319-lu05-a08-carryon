from main import main_condition, main_infinite


def test_condition_1(capsys, monkeypatch):
    inputs = iter(['no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main_condition()
    captured = capsys.readouterr()
    assert captured.out == ''

def test_condition_2(capsys, monkeypatch):
    inputs = iter(['yes', 'n', 'y', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main_condition()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_infinite_1(capsys, monkeypatch):
    inputs = iter(['no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main_infinite()
    captured = capsys.readouterr()
    assert captured.out == ''


def test_infinite_2(capsys, monkeypatch):
    inputs = iter(['yes', 'n', 'y', 'no'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main_infinite()
    captured = capsys.readouterr()
    assert captured.out == ''
