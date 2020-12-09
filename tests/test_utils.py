import io

from zcasino.utils import prompt_number


def test_prompt_number_returns_a_number(capsys, monkeypatch):
    """Vérifie que prompt_number retourne un entier."""
    # On simule une entrée utilisateur pour éviter de bloquer sur input()
    monkeypatch.setattr('sys.stdin', io.StringIO('10'))
    # On exécute la fonction à tester
    result = prompt_number("un message pour l'utilisateur")
    # On vérifie le résultat de la fonction avec assert
    assert isinstance(result, int)


def test_prompt_number_writes_message_to_stdout(capsys, monkeypatch):
    """Vérifie que le message passé en paramètre de la fonction est affiché
    à l'utilisateur."""
    # On simule le fait que l'utilisateur a entré le nombre 10
    monkeypatch.setattr('sys.stdin', io.StringIO('10'))
    # On exécute la fonction à tester
    result = prompt_number("un message pour l'utilisateur")
    # On capture le texte affiché sur la sortie standard
    captured = capsys.readouterr()
    # On teste que le test capturé sur la sortie du terminal est bien celui en
    # paramètre de la fonction à test, prompt_number
    assert captured.out == "un message pour l'utilisateur"


def test_prompt_number_asks_question_twice_if_nonint_answer(
    capsys, monkeypatch
):
    """Vérifie que le message est affiché une seconde fois si l'utilisateur
    saisit une chaine de caractères à la place d'un entier."""
    # On simule le fait que l'utilisateur a entré la chaine "aaa"
    # puis, au second essai, le nombre 10
    monkeypatch.setattr('sys.stdin', io.StringIO('aaa\n10'))
    # On exécute la fonction à tester
    result = prompt_number("un message pour l'utilisateur")
    # On capture le texte affiché sur la sortie standard
    captured = capsys.readouterr()
    # On vérifie le comportement attendu
    assert (
        captured.out == "un message pour l'utilisateur" * 2
    ), "Le texte doit être affiché deux fois"


def test_prompt_number_returns_a_number_larger_than_min(capsys, monkeypatch):
    """Vérifie que le message est affiché tant que l'utilisateur ne répond pas
    avec une nombre supérieur à la valeur minimale demandée."""
    # On simule le fait que l'utilisateur a entré les nombres 1, puis 2, puis
    # 3, puis 4, puis 5
    monkeypatch.setattr('sys.stdin', io.StringIO('1\n2\n3\n4\n5'))
    # On exécute la fonction à tester
    result = prompt_number("un message pour l'utilisateur", min_=5)
    # On capture le texte affiché sur la sortie standard
    captured = capsys.readouterr()
    # On vérifie le comportement attendu
    assert captured.out == "un message pour l'utilisateur" * 5, (
        "Le texte doit être affiché tant que l'utilisateur n'a pas saisie un "
        "entier correct, soit 5 fois"
    )
    assert (
        result == 5
    ), "Le résultat retourné doit être le premier entier supérieur à min_"
