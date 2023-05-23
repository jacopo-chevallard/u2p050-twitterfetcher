.ONESHELL:
.PHONY: help prepare-dev test lint run doc venv env-test
PROJECT_NAME=u2p050-twitterfetcher
PROJECT_MAIN_MODULE=u2p050-twitterfetcher
PROJECT_VERSION=$(shell cat VERSION)
PYTHON_VERSION=3.8

PYTHON=python

dep: ## install required dependencies for build.
	$(PYTHON) -m pip install artifacts-keyring --pre
	@$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install awscli
	$(PYTHON) -m pip install flake8
	$(PYTHON) -m pip install black
	$(PYTHON) -m pip install isort
	$(PYTHON) -m pip install mypy
	$(PYTHON) -m pip install pytest
	$(PYTHON) -m pip install pre-commit

env-test: dep## init test environnement.

	$(PYTHON) -m pip install -r requirements.txt

env-dev: dep## init dev environnement.
	$(PYTHON) -m pip install -r requirements.txt 

env-prod: dep## init prod environnement.
	$(PYTHON) -m pip install -r requirements.txt

welcome: dep env-dev ## Init evrything to get started

lint: ## Check error with code
	@echo "Flake8:" && $(PYTHON) -m flake8 $(PROJECT_MAIN_MODULE) && \
	echo "Black:" && $(PYTHON) -m black $(PROJECT_MAIN_MODULE) && \
	echo "Mypy:" && $(PYTHON) -m mypy main.py $(PROJECT_MAIN_MODULE) --namespace-packages --implicit-optional

fmt: ## Format code.
	@$(PYTHON) -m black $(PROJECT_MAIN_MODULE)
	@$(PYTHON) -m isort $(PROJECT_MAIN_MODULE)

test: venv ## run test.
	@$(PYTHON) -m pytest -v tests/

docker-build-dev: ## build a dev version of the docker image.
	@docker build \
	--build-arg CODEARTIFACT_AUTH_TOKEN \
	-t $(PROJECT_NAME):$(PROJECT_VERSION)-dev .

clean:
	pipenv --rm
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm .env
	rm .coverage

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
