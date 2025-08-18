# Created by sthomas at 18/08/2025
Feature: Mon Premier projet BDD

  L'objectif de ce fichier est de découvrir la syntaxe de base de Gherkin en Python avec Behave.

  Scenario: Test de mon premier scénario

    Given J'ouvre mon terminal
    When Je me déplace dans le répertoire /home/sthomas
    # And J'affiche le contenu avec 'dir'
    And J'affiche le contenu avec 'ls -la'
    And Je regarde le contenu du répertoire
    Then Je ferme le répertoire
