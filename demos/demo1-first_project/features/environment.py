import logging
import time
import os
from dotenv import load_dotenv

def before_all(context):
    print ("Avant tout")

    load_dotenv()

    env = context.config.userdata.get("env", "pro")

    if env == "dev":
        context.base_url = os.getenv("BASE_URL_DEV", "https://default.dev.com")
        context.browser = os.getenv("BROWSER_DEV", "opera")

    elif env == "prod":
        context.base_url = os.getenv("BASE_URL_PROD", "https://default.prod.com")
        context.browser = os.getenv("BROWSER_PROD", "opera")

    else:
        context.base_url = os.getenv("BASE_URL_DEFAULT", "https://default.prod.com")
        context.browser = os.getenv("BROWSER_DEFAULT", "opera")


    # Création d'un logger pour enregistrer tous les évènements du programme
    logger = logging.getLogger("Démo 6")
    logger.setLevel(logging.INFO)

    # Création d'un formatteur commun
    # Liste des paramètres du Formatter ici :
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Création du handler (gestionnaire de sortie)
    file_handler = logging.FileHandler('logs/demo7_hooks.log', mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Niveau de log minimum à enregistrer dans le fichier
    file_handler.setFormatter(formatter)

    # Ajout du handler au logger
    logger.addHandler(file_handler)

    context.LOGGER = logger


def after_all(context):
    print("Après tout")


def before_feature(context, feature):
    print(f"Avant la feature {feature.name}\n")

    print(context.base_url)
    print(context.browser)


def after_feature(context, feature):
    print(f"Fin feature {feature.name}")


def before_scenario(context, scenario):
    print(f"Début scénario {scenario.name}")

def after_scenario(context, scenario):
    print(f"Fin scénario {scenario.name}")

def before_step(context, step):
    print(f"Début step {step.name}")


def after_step(context, step):
    print("Fin step OK")
    time.sleep(1)
    print(f"Fin step {step.name}\n")


