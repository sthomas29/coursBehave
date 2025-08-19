import time
import logging
from behave import *

TIME_MAX=1

@given(u"J'ouvre un terminal")
def open_terminal(context):
    print("print: J'ouvre mon terminal")
    logger.info("J'ouvre mon terminal")
    time.sleep(TIME_MAX)

# @when(u"Je me déplace dans le répertoire /home/stephane.")
# def deplacerDansRepertoire(context):
#     print("print: Je me déplace dans le répertoire")
#     logger.info("Je me déplace dans le répertoire")
#     time.sleep(2)

@when(u"Je me déplace dans le répertoire {path}.")
def deplacerDansRepertoire(context,path):
    print(f"print: Je me déplace dans {path}")
    context.LOGGER.info(f"Je me déplace dans {path}")
    time.sleep(TIME_MAX)


@when(u"J'affiche le contenu du répertoire avec `ls -la`")
def lancer_recherche(context):
    print("print: J'affiche le contenu")
    context.LOGGER.info("J'affiche le contenu")
    time.sleep(TIME_MAX)

@When(u"Je regarde le contenu")
def regarderContenu(context):
    print("print: Je regarde le contenu")
    context.LOGGER.info("Je regarde le contenu")
    time.sleep(TIME_MAX)

@then(u'Je ferme le terminal')
def cliquer_bouton(context):
    print("print: Je ferme le terminal")
    context.LOGGER.info("Je ferme le terminal")
    time.sleep(TIME_MAX)

@given(u"J'ouvre un terminal {cmd}")
def open_terminal(context, cmd):
    cmd = cmd.replace('"', '')
    print(f"print: J'ouvre mon terminal avec {cmd}")
    context.LOGGER.info(f"J'ouvre mon terminal avec {str(cmd)}")
    time.sleep(TIME_MAX)



@when(u"Je manipule une DataTable dans le répertoire {path}")
def deplacerDansRepertoireAvecDataTable(context,path):
    print(f"print: Je me déplace dans {path}")
    for row in context.table:
        print(f"{row['Type']} / {row['Nom']}")

    context.LOGGER.info(f"Je me déplace dans {path}")
    time.sleep(TIME_MAX)

@when(u"J'affiche le contenu du répertoire avec {cmd}")
def lancer_recherche(context, cmd):
    print(f"print: J'affiche le contenu avec {cmd}")
    context.LOGGER.info(f"J'affiche le contenu avec {cmd}")
    time.sleep(TIME_MAX)

@When("Je regarde le contenu à {stdout}")
def regarderContenu(context,stdout):
    print(f"print: Je regarde le contenu à {stdout}")
    context.LOGGER.info(f"Je regarde le contenu à {stdout}")
    time.sleep(TIME_MAX)

@then('Je ferme le terminal après {nb} actions')
def cliquer_bouton(context, nb):
    nb = int(nb.replace('"', ''))
    print(type(nb))
    print(f"print: Je ferme le terminal après {nb} actions")
    context.LOGGER.info(f"Je ferme le terminal après {nb} actions")
    time.sleep(TIME_MAX)

@given(u"L’utilisateur ouvre la page de connexion")
def open_terminal(context):
    print(f"print: L’utilisateur ouvre la page de connexion")
    context.LOGGER.info(f"L’utilisateur ouvre la page de connexion")
    time.sleep(TIME_MAX)

@when('Il saisit l’email "{email}"')
def step_enter_email(context, email):
    print(f"print: L’utilisateur saisit l'email {email}")
    context.LOGGER.info(f"L’utilisateur saisit l'email {email}")
    time.sleep(TIME_MAX)

@when('Il saisit le mot de passe "{password}"')
def step_enter_password(context, password):
    print(f"print: L’utilisateur saisit le mot de passe '{password}'")
    context.LOGGER.info(f"L’utilisateur saisit le mot de passe '{password}'")
    time.sleep(TIME_MAX)

@when('{nom} clique sur le bouton de connexion')
def step_click_login_button(context, nom):
    print(f"print: {nom} clique sur le bouton de connexion")
    context.LOGGER.info(f"{nom} clique sur le bouton de connexion")
    time.sleep(TIME_MAX)

@then('{nom} doit voir le message "{message}"')
def step_verify_welcome_message(context, nom, message):
    print(f"print: {nom} doit voir le message {message}.")
    context.LOGGER.info(f"{nom} doit voir le message {message}.")
    time.sleep(TIME_MAX)
