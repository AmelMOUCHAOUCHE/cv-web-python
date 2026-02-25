#  CV Web – Python / Data Engineer Style

Site CV personnel généré avec Python (Jinja2 + YAML + Matplotlib).

Le contenu du CV est défini dans `resume.yaml`.
Le site HTML est généré automatiquement via `build.py`.

Un graphique de compétences est produit avec Python pour illustrer l’aspect “data”.

---

## Technologies

- Python 3
- Jinja2 (templating HTML)
- PyYAML (lecture du CV)
- Matplotlib (graphique compétences)
- HTML / CSS

---




Installer les dépendances : pip install pyyaml jinja2 matplotlib


Générer le site : python build.py

--> Cela crée :
    - ist/index.html
    - dist/assets/


    # Portfolio (Python Static Site)

Portfolio multipage généré en Python (YAML + Jinja2).

## Installer
pip install pyyaml jinja2

## Générer
python build.py

## Lancer en local
cd dist
python -m http.server 8000
Ouvrir http://localhost:8000