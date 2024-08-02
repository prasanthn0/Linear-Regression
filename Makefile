.PHONY: setup_pyenv init_project activate_env remove_env data features train predict run clean test

# Variables
PROJECT_NAME=regression-from-scratch
POETRY=poetry
PROJECT_DIR=$(shell pwd)
PYTHON_VERSION=3.10.12
PYENV=pyenv

# Ensure the correct Python version is installed with pyenv
setup_pyenv:
	@if ! $(PYENV) versions | grep -q $(PYTHON_VERSION); then \
		echo "Python $(PYTHON_VERSION) not found. Installing..."; \
		$(PYENV) install $(PYTHON_VERSION); \
	fi
	$(PYENV) local $(PYTHON_VERSION)

# Initialize the poetry project if pyproject.toml is not present
init_project: 
	@if [ ! -f "$(PROJECT_DIR)/pyproject.toml" ]; then \
		echo "pyproject.toml not found. Creating a new Poetry project..."; \
		echo "[tool.poetry]" > pyproject.toml; \
		echo 'name = "$(PROJECT_NAME)"' >> pyproject.toml; \
		echo 'version = "0.1.0"' >> pyproject.toml; \
		echo 'description = ""' >> pyproject.toml; \
		echo 'authors = ["Prasanth N <prasanth061993@gmail.com>"]' >> pyproject.toml; \
		echo "" >> pyproject.toml; \
		echo "[tool.poetry.dependencies]" >> pyproject.toml; \
		echo 'python = "^$(PYTHON_VERSION)"' >> pyproject.toml; \
		echo "" >> pyproject.toml; \
		echo "[build-system]" >> pyproject.toml; \
		echo 'requires = ["poetry-core>=1.0.0"]' >> pyproject.toml; \
		echo 'build-backend = "poetry.core.masonry.api"' >> pyproject.toml; \
	else \
		echo "pyproject.toml found."; \
	fi
	@echo "Updating dependencies..."
	$(POETRY) update
	$(POETRY) install

# Activate the poetry environment and update dependencies
activate_env: init_project
	@echo "Activating the poetry environment..."
	@$(POETRY) shell

data:
	@echo "Creating dataset from booking_log and participant_log.."
	${BINARIES}/python -m src.data.make_dataset