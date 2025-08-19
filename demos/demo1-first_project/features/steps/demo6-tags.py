import time
import logging
from behave import *

# Création d'un logger pour enregistrer tous les évènements du programme
logger = logging.getLogger("Démo 6")
logger.setLevel(logging.INFO)

# Création d'un formatteur commun
# Liste des paramètres du Formatter ici :
# https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Création du handler (gestionnaire de sortie)
file_handler = logging.FileHandler('demos/demo6_tags.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)    #Niveau de log minimum à enregistrer dans le fichier
file_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(file_handler)

@given(u"J'ouvre un terminal")
def open_terminal(context):
    print("print: J'ouvre mon terminal")
    logger.info("J'ouvre mon terminal")
    time.sleep(2)

@when(u"Je me déplace dans le répertoire /home/stephane.")
def deplacerDansRepertoire(context):
    print("print: Je me déplace dans le répertoire")
    logger.info("Je me déplace dans le répertoire")
    time.sleep(2)

@when(u"J'affiche le contenu du répertoire avec `ls -la`")
def lancer_recherche(context):
    print("print: J'affiche le contenu")
    logger.info("J'affiche le contenu")
    time.sleep(2)

@When(u"Je regarde le contenu")
def regarderContenu(context):
    print("print: Je regarde le contenu")
    logger.info("Je regarde le contenu")
    time.sleep(2)

@then(u'Je ferme le terminal')
def cliquer_bouton(context):
    print("print: Je ferme le terminal")
    logger.info("Je ferme le terminal")
    time.sleep(2)

@given(u"J'ouvre un terminal {cmd}")
def open_terminal(context, cmd):
    cmd = cmd.replace('"', '')
    print(f"print: J'ouvre mon terminal avec {cmd}")
    logger.info(f"J'ouvre mon terminal avec {str(cmd)}")
    time.sleep(2)

@when(u"Je me déplace dans le répertoire {path}")
def deplacerDansRepertoire(context,path):
    print(f"print: Je me déplace dans {path}")
    logger.info(f"Je me déplace dans {path}")
    time.sleep(2)

@when(u"Je manipule une DataTable dans le répertoire {path}")
def deplacerDansRepertoireAvecDataTable(context,path):
    print(f"print: Je me déplace dans {path}")
    for row in context.table:
        print(f"{row['Type']} / {row['Nom']}")

    logger.info(f"Je me déplace dans {path}")
    time.sleep(2)

@when(u"J'affiche le contenu du répertoire avec {cmd}")
def lancer_recherche(context, cmd):
    print(f"print: J'affiche le contenu avec {cmd}")
    logger.info(f"J'affiche le contenu avec {cmd}")
    time.sleep(2)

@When("Je regarde le contenu à {stdout}")
def regarderContenu(context,stdout):
    print(f"print: Je regarde le contenu à {stdout}")
    logger.info(f"Je regarde le contenu à {stdout}")
    time.sleep(2)

@then('Je ferme le terminal après {nb} actions')
def cliquer_bouton(context, nb):
    nb = int(nb.replace('"', ''))
    print(type(nb))
    print(f"print: Je ferme le terminal après {nb} actions")
    logger.info(f"Je ferme le terminal après {nb} actions")
    time.sleep(2)

@given(u"L’utilisateur ouvre la page de connexion")
def open_terminal(context):
    print(f"print: L’utilisateur ouvre la page de connexion")
    logger.info(f"L’utilisateur ouvre la page de connexion")
    time.sleep(2)

@when('Il saisit l’email "{email}"')
def step_enter_email(context, email):
    print(f"print: L’utilisateur saisit l'email {email}")
    logger.info(f"L’utilisateur saisit l'email {email}")
    time.sleep(2)

@when('Il saisit le mot de passe "{password}"')
def step_enter_password(context, password):
    print(f"print: L’utilisateur saisit le mot de passe '{password}'")
    logger.info(f"L’utilisateur saisit le mot de passe '{password}'")
    time.sleep(2)

@when('{nom} clique sur le bouton de connexion')
def step_click_login_button(context, nom):
    print(f"print: {nom} clique sur le bouton de connexion")
    logger.info(f"{nom} clique sur le bouton de connexion")
    time.sleep(2)

@then('{nom} doit voir le message "{message}"')
def step_verify_welcome_message(context, nom, message):
    print(f"print: {nom} doit voir le message {message}.")
    logger.info(f"{nom} doit voir le message {message}.")
    time.sleep(2)
