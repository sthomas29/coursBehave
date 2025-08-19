# Created by sthomas at 18/08/2025
Feature: Mon Premier projet BDD

  L'objectif de ce fichier est de découvrir la syntaxe de base de Gherkin en Python avec Behave.

  Background:
    Given J'ouvre mon terminal "<shell>"
    When Je me déplace dans le répertoire "<path>"

    # Syntaxe du datatable avec des pipe | est similaire au MarkDown (MD)
    When J'affiche le contenu avec "ls -la"
      |Type       | Nom   |
      |Directory  | Rep1  |
      |File       | File1 |
      |Directory  | Rep2  |
      |Directory  | Rep3  |
      |File       | File2 |

    And Je regarde le contenu du répertoire
    Then Je ferme le répertoire

  Scenario Outline: Démo 4 - Manipulation des scénarios outline

  Examples:
    |shell    | path              |
    |bash     | /home/sthomas     |
    |cmd      | c:\Users\sthomas  |
    |pwsh     | PS:\Users\sthomas |


  Scenario Outline: "Démo 5 - Manipulation du Background 1"

    Examples:
      |shell    | path              |
      |bash     | /home/sthomas     |

  Scenario Outline: "Démo 5 - Manipulation du Background 2"

    Examples:
      |shell    | path              |
      |pwsh     | PS:\Users\sthomas |


  Scenario: "Démo 5 - Manipulation du Background 3 (sans étapes complémentaires)"


