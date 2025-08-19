import logging


def before_all(context):
    print ("Avant tout")

    # Création d'un logger pour enregistrer tous les évènements du programme
    logger = logging.getLogger("Démo 6")
    logger.setLevel(logging.INFO)

    # Création d'un formatteur commun
    # Liste des paramètres du Formatter ici :
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Création du handler (gestionnaire de sortie)
    file_handler = logging.FileHandler('demo7_hooks.log', mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Niveau de log minimum à enregistrer dans le fichier
    file_handler.setFormatter(formatter)

    # Ajout du handler au logger
    logger.addHandler(file_handler)

    context.LOGGER = logger


def after_all(context):
    print("Après tout")


def before_feature(context, feature):
    print(f"Avant la feature {feature.name}")

def after_feature(context, feature):
    print(f"Fin feature {feature.name}")


def before_scenario(context, scenario):
    print(f"Début scénario {scenario.name}")

def after_scenario(context, scenario):
    print(f"Fin scénario {scenario.name}")

def before_step(context, step):
    print(f"Début step {step.name}")


def after_step(context, step):
    name = step.name
    # print("Fin step : "  + name )
    print(f"Fin step {name}")


