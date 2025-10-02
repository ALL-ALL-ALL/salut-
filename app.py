import plotly.express as px
import pandas as pd

# Exemple -
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')


# a. 1er graphique - les ventes par produit. - 
# a. 1er graphique - les ventes par produit. -  
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
figure = px.pie(données, values='qte',names='produit',title='ventes par produit')
figure.write_html('les-ventes-par-produit.html')
print('les-ventes-par-produit.html creer avec succés :-)')


# b. 2ièm graphique - le chiffre d'affaires par produit. -
# b. 2ièm graphique - le chiffre d'affaires par produit. -
données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
# créer une colonne "chiffre d'affaires" qui contient le chiffre d'affaires (prix * quantité) pour chaque ligne
données["chiffre d'affaires"] = données["prix"] * données["qte"]

#
figure.write_html('le chiffre daffaires par produit')
print('le chiffre daffaires par produit.html creer avec succès :-)')

