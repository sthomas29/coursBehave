Feature: Mon Premier projet BDD

    L'objectif est de découvrir Gherkin et Behave avec Python
    Background:
        Given   J'ouvre un terminal "git bash"
        When    Je me déplace dans le répertoire "/home/stephane".
        And     J'affiche le contenu du répertoire avec "ls -la"
        And     Je regarde le contenu à "l'écran"
        Then    Je ferme le terminal après "5" actions


    @demo1 @all_demos
    Scenario: Démo 1 Test de mon premier scénario avec Behave
        When    Je me déplace dans le répertoire /home/stephane.
        And     J'affiche le contenu du répertoire avec `ls -la`
        And     Je regarde le contenu
        Then    Je ferme le terminal

    @demo2 @all_demos
    Scenario: Démo 2 Test scénario avec des paramètres avec Behave

    @demo3 @all_demos
    Scenario: Démo 3 Je manipule une DataTable dans un step avec Behave
        When    Je manipule une DataTable dans le répertoire "/home/stephane"
            |Type       |Nom        |
            |Directory  |Rep1       |
            |Directory  |Rep2       |
            |File       |Fichier1   |
            |Directory  |Fichier2   |

    @demo4 @scenario_outline
    Scenario Outline: Démo4 : Je créé un scénario avec "Scenario Outline" et j'y insère plusieurs jeux de données.
        Given   L’utilisateur ouvre la page de connexion
        When    Il saisit l’email "<email>"
        And     Il saisit le mot de passe "<password>"
        And     <nom> clique sur le bouton de connexion
        Then    <nom> doit voir le message "<message>"
    Examples:
        | nom     |email                | password      | message		  |
        | Testeur |testeur1@example.com | pass123       | Welcome		  |
        | Admin   |admin@example.com    | adminpass     | admin access	  |
        | Fake    |fake@example.com     | wrongpass     | invalid login   |
