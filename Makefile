# PKGS = api generator
PKG = api

.PHONY: clean init

init: clean
	pipenv --python 3.8
	pipenv install --dev
	pipenv run pre-commit install

lint:
	pipenv run flake8 ${PKG} --max-line-length=120
	pipenv run pylint --rcfile=setup.cfg ${PKG}/**

analysis:
	pipenv run bandit ${PKG}

format:
	pipenv run black ${PKG}
	pipenv run isort ${PKG}

ci-bundle: analysis format lint test

test:
	cd api && pipenv run pytest -vv --cov-report=term-missing --cov=endpoints --cov tests
