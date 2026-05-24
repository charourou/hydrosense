import pandas as pd

url = "https://hubeau.eaufrance.fr/api/v1/niveaux_nappes/chroniques.csv?bss_id=BSS001EUKK&size=5000"
df = pd.read_csv(url, sep=";") # L'API Hub'eau renvoie généralement un CSV séparé par des points-virgules
print(df.head())
print(df.columns)


# Index(['code_bss', 'bss_id', 'urn_bss', 'date_mesure', 'timestamp_mesure',
    #    'niveau_nappe_eau', 'mode_obtention', 'statut', 'qualification',
    #    'code_continuite', 'nom_continuite', 'code_producteur',
    #    'nom_producteur', 'code_nature_mesure', 'nom_nature_mesure',
    #    'profondeur_nappe'],
    #   dtype='object')
