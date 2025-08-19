import time
import logging
from behave import *

TIME_MAX=1

@given(u"J'ouvre un terminal")
def open_terminal(context):
    pass

@when(u"Je me déplace dans le répertoire {path}.")
def deplacerDansRepertoire(context,path):
    pass

@when(u"J'affiche le contenu du répertoire avec `ls -la`")
def lancer_recherche(context):
    pass

@When(u"Je regarde le contenu")
def regarderContenu(context):
    pass

@then(u'Je ferme le terminal')
def cliquer_bouton(context):
    pass

@given(u"J'ouvre un terminal {cmd}")
def open_terminal(context, cmd):
    cmd = cmd.replace('"', '')
    context.LOGGER.error(f"J'ouvre mon terminal avec {str(cmd)}")
    context.LOGGER.critical(f"J'ouvre mon terminal avec {context.browser}")


@when(u"Je manipule une DataTable dans le répertoire {path}")
def deplacerDansRepertoireAvecDataTable(context,path):
    for row in context.table:
        print(f"{row['Type']} / {row['Nom']}")

@when(u"J'affiche le contenu du répertoire avec {cmd}")
def lancer_recherche(context, cmd):
    pass

@When("Je regarde le contenu à {stdout}")
def regarderContenu(context,stdout):
    pass

@then('Je ferme le terminal après {nb} actions')
def cliquer_bouton(context, nb):
    nb = int(nb.replace('"', ''))
    pass

@given(u"L’utilisateur ouvre la page de connexion")
def open_terminal(context):
    pass

@when('Il saisit l’email "{email}"')
def step_enter_email(context, email):
    pass

@when('Il saisit le mot de passe "{password}"')
def step_enter_password(context, password):
    pass

@when('{nom} clique sur le bouton de connexion')
def step_click_login_button(context, nom):
    pass

@then('{nom} doit voir le message "{message}"')
def step_verify_welcome_message(context, nom, message):
    pass