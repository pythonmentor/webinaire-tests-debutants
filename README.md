# Webinaire: Testez dès que vous savez marcher avec vos premiers projets Python

Ce dépôt de code contient le code développé lors du webinaire et après. La 
vidéo suivante a été réalisée en complément de ce code:

TODO

## Dépendances
Après avoir installé si nécessaire pipenv à l'aide de la commande pip install pipenv,
vous pouvez installer les dépendances et activer l'environnement virtuel
à l'aide des deux commandes suivantes:

```
$ pipenv install --dev
$ pipenv shell
```

## Exécution des tests
Une fois les dépendances installées et l'environnement virtuel activé, vous pouvez
exécuter les tests à l'aide de la commande:

```
$ pytest -v
```