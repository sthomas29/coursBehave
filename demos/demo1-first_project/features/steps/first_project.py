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
file_handler = logging.FileHandler('first_project.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # Niveau de log minimum à enregistrer dans le fichier
file_handler.setFormatter(formatter)

# Ajout du handler au logger
logger.addHandler(file_handler)

@given("J'ouvre mon terminal")
def open_terminal(context):
    print("P: J'ouvre mon terminal")
    logger.info("J'ouvre mon terminal")
    time.sleep(2)

@when("Je me déplace dans le répertoire /home/sthomas")
def deplacer_dans_repertoire(context):
    print("P: Je me déplace dans le répertoire /home/sthomas")
    logger.info("Je me déplace dans le répertoire /home/sthomas")
    time.sleep(2)

@when("J'affiche le contenu avec 'ls -la'")
def affiche_contenu(context):
    print("P: J'affiche le contenu avec 'ls -la'")
    logger.info("J'affiche le contenu avec 'ls -la'")
    time.sleep(2)

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


