import time
import logging
from behave import *

# Création d'un logger pour enregistrer tous les évènements du programme
logger = logging.getLogger("First_project")
logger.setLevel(logging.INFO)

# Création d'un formatteur commun
# Liste des paramètres du Formatter ici :
# https://docs.python.org/3/library/logging.html#logrecord-attributes
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Création du handler (gestionnaire de sortie)
file_handler = logging.FileHandler('demo4_scenario_outline.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # Niveau de log minimum à enregistrer dans le fichier
file_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(file_handler)

@given(u"J'ouvre mon terminal {shell}")
def open_terminal(context, shell):

    # Récupération de la valeur transmise dans le fichier Guerkin
    # dans la  variable 'shell'

    # Remplacement des guillemets doubles par une chaine vide ""
    shell = shell.replace('"', "")

    print(f"P: J'ouvre mon terminal {shell}")
    logger.info(f"J'ouvre mon terminal {shell}")

    time.sleep(2)

@when(u"Je me déplace dans le répertoire {path}")
def deplacer_dans_repertoire(context, path):
    print(f"P: Je me déplace dans le répertoire {path}")
    logger.info(f"Je me déplace dans le répertoire {path}")
    time.sleep(2)

@when("J'affiche le contenu avec {cmd}")
def affiche_contenu(context, cmd):

    #print(f"Nb enregistrements Table : {context.table}")

    print(f"P: J'affiche le contenu avec {cmd}")
    logger.info(f"J'affiche le contenu avec {cmd}")

    # Le contenu du tableau est stocké dans la variable 'table' du 'contexte'
    for row in context.table:
        logger.info(f"J'affiche la ligne {row['Type']} {row['Nom']}")
        time.sleep(1)

    time.sleep(1)

@when("Je regarde le contenu du répertoire")
def regarde_contenu(context):
    print("P: Je regarde le contenu du répertoire")
    logger.info("Je regarde le contenu du répertoire")
    time.sleep(2)

@then("Je ferme le répertoire")
def ferme_repertoire(context):
    print("P: Je ferme le répertoire")
    logger.info("Je ferme le répertoire")
    time.sleep(2)


