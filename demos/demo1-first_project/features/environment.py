
def before_all(context):
    print ("Avant tout")
    pass

def after_all(context):
    print("Après tout")
    pass

def before_feature(context, feature):
    print(f"Avant la feature {feature.name}")

def after_feature(context, feature):
    print(f"Fin feature {feature.name}")
    pass

def before_scenario(context, scenario):
    print(f"Début scénario {scenario.name}")

def after_scenario(context, scenario):
    print(f"Fin scénario {scenario.name}")

def before_step(context, step):
    print(f"Début step {step.name}")
    pass

def after_step(context, step):
    print(f"Fin step {step.name}")
    pass


