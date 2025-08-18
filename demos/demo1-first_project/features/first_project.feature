# Created by sthomas at 18/08/2025
Feature: Mon Premier projet BDD

  L'objectif de ce fichier est de découvrir la syntaxe de base de Gherkin en Python avec Behave.

  Scenario: Test de mon premier scénario

    Given J'ouvre mon terminal "Powershell"
    When Je me déplace dans le répertoire "/home/sthomas"
    # And J'affiche le contenu avec 'dir'

    # Syntaxe du datatable avec des pipe | est similaire au MarkDown (MD)
    And J'affiche le contenu avec "ls -la"
      |Type       | Nom   |
      |Directory  | Rep1  |
      |File       | File1 |
      |Directory  | Rep2  |
      |Directory  | Rep3  |
      |File       | File2 |

    And Je regarde le contenu du répertoire
    Then Je ferme le répertoire
