# Fonctionnement des profils

## 1) Utilisation des fichiers setup.XXX.cfg

> - Créer un fichier par profil
> - Respecter la syntaxe habituelle avec les options standards telles que vues dans le cours.

## 2) Prise en compte de la configuration
Dans le fichier Makefile, on rajoute une section telle que celle-ci :
```description
    test:
        @cp setup.test.cfg setup.cfg
        @echo "=== Profil Test ==="
        behave
```
Exemple pour un profil test.
On copie avec cp le contenu du fichier setup.test.cfg dans le fichier setup.cfg.
Puis, on lance `behave` sans option pour qu'il charge le profil copié.

## 3) Chargement de la config depuis le *shell*
Le lancement ne s'opère plus avec la commande `behave` mais avec la commande `make`

*`make test`* lance le script Makefile pour le profil **test** 

 