from .init import Project


def get_pyproject_contain(project: Project):
    return f"""
[project]
name = "{project.project_name}"
version = "{project.version}"
description = "{project.description}"
authors = {project.author_to_dict}
readme = "README.md"

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

# [project.scripts]
# script_cde = "{project.norm_project_name}.module:method"

[tool.setuptools.packages.find]
where = ["src"]
include = ["{project.norm_project_name}*"]

[tool.setuptools.package-data]
func = ["py.typed"]
    """
