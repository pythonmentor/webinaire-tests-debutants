def prompt_number(message, min_=None, max_=None):
    """Demande à l'utilisateur à l'aide de message de saisir un entier.

    Si l'utilisateur fournit un objet qui n'est pas un entier, ou un entier qui
    n'est pas entre min et max (non compris), la question est reposée.
    """
    while True:
        response = input(message)
        if response.isdigit():
            number = int(response)
            if min_ is not None and number < min_:
                continue
            if max_ is not None and number >= max_:
                continue
            return number
