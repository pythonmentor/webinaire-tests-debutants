import sys

from zcasino.utils import prompt_number


def test_prompt_number_returns_a_number(monkeypatch):
    """Vérifie que notre fonction prompt_number retourne un entier."""

    def user_input(message):
        print(message, end="")
        return "10"

    monkeypatch.setattr('builtins.input', user_input)

    result = prompt_number("un message pour l'utilisateur")
    assert isinstance(result, int)


def test_prompt_number_writes_message_to_stdout(capsys, monkeypatch):
    """Vérifie que le message passé en paramètre de la fonction est affiché
    à l'utilisateur."""

    def user_input(message):
        print(message, end="")
        return "10"

    monkeypatch.setattr('builtins.input', user_input)
    result = prompt_number("un message pour l'utilisateur")
    captured = capsys.readouterr()
    assert captured.out == "un message pour l'utilisateur"


def test_prompt_number_asks_question_twice_if_nonint_answer(
    capsys, monkeypatch
):
    """Vérifie que le message est affiché une seconde si l'utilisateur entre
    une chaine de caractères à la place d'un entier."""
    inputs = ["aaa", "10"]

    def user_input(message):
        print(message, end="")
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', user_input)
    result = prompt_number("un message pour l'utilisateur")
    captured = capsys.readouterr()
    assert captured.out == "un message pour l'utilisateur" * 2


def test_prompt_number_returns_a_number_larger_than_min(capsys, monkeypatch):
    def user_input(message, inputs=["1", "10"]):
        print(message, end="")
        return inputs.pop(0)

    monkeypatch.setattr('builtins.input', user_input)
    result = prompt_number("un message pour l'utilisateur", min_=5)
    captured = capsys.readouterr()
    assert captured.out == "un message pour l'utilisateur" * 2
    assert result == 10