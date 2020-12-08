import io
import sys

from zcasino.utils import prompt_number


def test_prompt_number_returns_a_number():
    """Vérifie que notre fonction prompt_number retourne un entier."""
    # On simule le fait que l'utilisateur a entré le nombre 10
    sys.stdin = io.StringIO("10")

    result = prompt_number("un message pour l'utilisateur")
    assert isinstance(result, int)


def test_prompt_number_writes_message_to_stdout():
    """Vérifie que le message passé en paramètre de la fonction est affiché
    à l'utilisateur."""
    # On simule le fait que l'utilisateur a entré le nombre 10
    sys.stdin = io.StringIO("10")
    # On capture la texte affiché à l'utilisateur
    sys.stdout = io.StringIO()

    result = prompt_number("un message pour l'utilisateur")
    # On capture le texte affiché sur la sortie standard
    assert sys.stdout.getvalue() == "un message pour l'utilisateur"


def test_prompt_number_asks_question_twice_if_nonint_answer():
    """Vérifie que le message est affiché une seconde fois si l'utilisateur entre
    une chaine de caractères à la place d'un entier."""
    # On simule le fait que l'utilisateur a entré la chaine "aaa"
    # puis le nombre 10
    sys.stdin = io.StringIO("aaa\n10")
    # On capture la texte affiché à l'utilisateur
    sys.stdout = io.StringIO()

    result = prompt_number("un message pour l'utilisateur")
    # On capture le texte affiché sur la sortie standard
    assert sys.stdout.getvalue() == "un message pour l'utilisateur" * 2


def test_prompt_number_returns_a_number_larger_than_min():
    """Vérifie que le message est affiché tant que l'utilisateur ne répond pas
    avec une nombre supérieur à la valeur minimale demandée."""
    # On simule le fait que l'utilisateur a entré les nombre 1, puis 2, puis
    # 3, puis 4, puis 5
    sys.stdin = io.StringIO("1\n2\n3\n4\n5")
    # On capture la texte affiché à l'utilisateur
    sys.stdout = io.StringIO()

    result = prompt_number("un message pour l'utilisateur", min_=5)
    # On vérifie que le message est affiché jusqu'à ce que l'utiliateur
    # donne un nombre plus grand que le minimum, soit 5 fois.
    assert sys.stdout.getvalue() == "un message pour l'utilisateur" * 5
    assert result == 5