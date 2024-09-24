from main import main_condition, main_infinite


def test_condition_1(capsys, monkeypatch):
    # Simulate user input 'no' and ensure the prompt is printed
    inputs = iter(['no'])
    monkeypatch.setattr('builtins.input', lambda prompt: (print(prompt, end=''), next(inputs))[1])

    # Run the function
    main_condition()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out == 'Carry on?\n'  # Only one prompt should be printed


def test_condition_2(capsys, monkeypatch):
    # Simulate user input 'yes', 'n', 'y', then 'no' and ensure the prompt is printed
    inputs = iter(['yes', 'n', 'y', 'no'])
    monkeypatch.setattr('builtins.input', lambda prompt: (print(prompt, end=''), next(inputs))[1])

    # Run the function
    main_condition()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if four prompts were printed before the loop ended
    assert captured.out == 'Carry on?\nCarry on?\nCarry on?\nCarry on?\n'


def test_infinite_1(capsys, monkeypatch):
    # Simulate user input 'no' and ensure the prompt is printed
    inputs = iter(['no'])
    monkeypatch.setattr('builtins.input', lambda prompt: (print(prompt, end=''), next(inputs))[1])

    # Run the function
    main_infinite()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out == 'Carry on?\n'  # Only one prompt should be printed before breaking


def test_infinite_2(capsys, monkeypatch):
    # Simulate user input 'yes', 'n', 'y', then 'no' and ensure the prompt is printed
    inputs = iter(['yes', 'n', 'y', 'no'])
    monkeypatch.setattr('builtins.input', lambda prompt: (print(prompt, end=''), next(inputs))[1])

    # Run the function
    main_infinite()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if four prompts were printed before the loop ended
    assert captured.out == 'Carry on?\nCarry on?\nCarry on?\nCarry on?\n'
