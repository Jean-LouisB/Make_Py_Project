# Py Project Packagor

`py_project_packagor` est un générateur interactif de structure pour démarrer un
package Python. Sa commande `py-init` demande les informations du projet, puis
crée les fichiers de base nécessaires à sa construction et à sa documentation.

## Installation globale

Il est conseiller une installation globale.

```bash
pip install Py-Project-Packagor
```

Redémarrez ensuite le terminal si nécessaire.

Pour mettre à jour l'installation locale après avoir modifié le code :

```bash
pip install --force .
```

## Utilisation

Placez-vous dans le dossier où vous souhaitez créer le nouveau projet, puis
lancez :

```bash
py-init
```

La commande demande le nom du projet, sa version, sa description, le nom de
l'auteur et son adresse e-mail. Les valeurs affichées entre parenthèses sont
des suggestions ; renseignez notamment le nom et l'e-mail de l'auteur pour les
inscrire dans les métadonnées du package.

Le nom du projet est utilisé pour créer le dossier du module sous `src/` ; il
est converti en minuscules et les espaces sont remplacés par des underscores.

### Exemple de structure générée

```text
mon_projet/
├── README.md
├── pyproject.toml
└── src/
    └── mon_projet/
        ├── __init__.py
        └── py.typed
```

Le fichier `pyproject.toml` contient les métadonnées du package et sa
configuration de build avec setuptools. Un fichier marqueur `py.typed` est
également créé dans le module.

> **Attention :** la commande écrit ou remplace `README.md`, `pyproject.toml`,
> `src/<nom_du_module>/__init__.py` et `src/<nom_du_module>/py.typed` dans le
> dossier courant. Lancez-la dans un dossier adapté et sauvegardez tout fichier
> que vous souhaitez conserver.

## Construire le package généré

Dans le dossier du nouveau projet, construisez les distributions avec `build` :

```bash
python -m pip install build
python -m build
```

Les fichiers de distribution sont créés dans `dist/`.
