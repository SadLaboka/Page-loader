install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

lint:
	poetry run flake8 page_loader
	poetry run flake8 tests

coverage:
	poetry run pytest --cov=page_loader --cov-report=xml
