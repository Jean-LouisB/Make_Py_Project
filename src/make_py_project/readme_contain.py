from .init import Project


def get_readme_contain(project: Project):
    return f"""
# Votre Package {project.project_name.upper()}

Créer et activer votre environnement.

Installer build:
```
    pip install build
```

Installer votre package:

```
    python3 -m build
```

Il crée un dossier /dist contenant votre package prêt à être installé.
Ainsi qu'une archive.

## Installer votre package dans un autre projet:

```
pip install from_chemin/dist/nom_de_votre_package

```

    """
