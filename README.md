# python-poetry-template

[![CI](https://github.com/kkml4220/python-poetry-template/actions/workflows/CI.yml/badge.svg)](https://github.com/kkml4220/python-poetry-template/actions/workflows/CI.yml)

![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![vscode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

`poetry` template repository

## Installation

- Python: 3.12.0

```bash
# install poetry
pip install poetry
# Poetry to use project-specific virtual env
poetry config virtualenvs.in-project true
# install virtual env
poetry install
# init scripts
poetry run task init
```

## Usage

### Task

```bash
# format
poetry run task format
# lint
poetry run task lint
# pytest
poetry run task test
# sphinx update docs
poetry run task docs
```
