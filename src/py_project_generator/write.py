from .init import Project
from .make_path import make_paths
from .pyproject_contain import get_pyproject_contain
from .readme_contain import get_readme_contain


def write(project: Project):
    parent, _, project_path = make_paths(project)
    pyproject_contain = get_pyproject_contain(project)
    readme_contain = get_readme_contain(project)
    with open(project_path / "__init__.py", "w") as f:
        f.write(f"# {project.project_name.upper()} par {project.author_fullname}\n")

    with open(project_path / "py.typed", "w") as f:
        pass

    with open(parent / "pyproject.toml", "w") as f:
        contain = pyproject_contain.replace("\n", "", 1)
        f.write(contain)

    with open(parent / "README.md", "w") as f:
        contain = readme_contain.replace("\n", "", 1)
        f.write(contain)
