#!/usr/bin/env python3

import click
from pathlib import Path


@click.command()
@click.argument('project_dir', type=click.Path(exists=False))
def make_project(project_dir):
    project_dir = Path(project_dir)
    Path.mkdir(project_dir, exist_ok=False)

    readme_contents = """# {0}

## Getting Started

### Prerequisites

### Installing

## Running Tests

## Deployment

## Versioning

## Authors
Author | Contact | Github
--- | --- | ---
Andrew Hoetker | ahoetker@me.com | [ahoetker](https://github.com/ahoetker)

## License
    """.format(project_dir.name)

    gitignore_contents = """# byte-compiled files
*/__pycache__/
*.pyc

# Setuptools data
/dist/
/*.egg-info

# macOS binary records
.DS_Store

# PyCharm files
/.idea/
    """

    setup_py_content = """from setuptools import setup, find_packages

setup(
    name="{0}",
    version="0.1",
    description="placeholder",
    url="placeholder",
    author="Andrew Hoetker",
    author_email="ahoetker@me.com",
    install_requires=[
    ],
    packages=find_packages(),
    zip_safe=False,
)
""".format(project_dir.name)

    readme = Path(project_dir / "README.md")
    Path.touch(readme)
    with readme.open('w') as f:
        f.write(readme_contents)

    gitignore = Path(project_dir / ".gitignore")
    Path.touch(readme)
    with gitignore.open('w') as f:
        f.write(gitignore_contents)

    setup_py = Path(project_dir / "setup.py")
    Path.touch(setup_py)
    with setup_py.open("w") as f:
        f.write(setup_py_content)

    requirements = Path(project_dir / "requirements.txt")
    Path.touch(requirements)

    tests = Path(project_dir / "tests")
    Path.mkdir(tests, exist_ok=False)


if __name__ == "__main__":
    make_project()
