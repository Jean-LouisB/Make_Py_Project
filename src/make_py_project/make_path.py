import os
from pathlib import Path
from .init import Project


def make_paths(project: Project):
    parent = Path.cwd()
    src = parent / "src"
    if not src.exists():
        os.mkdir(src)

    project_path = src / f"{project.norm_project_name}"
    if not project_path.exists():
        os.mkdir(project_path)

    return parent, src, project_path
