install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl --force-reinstall

package-uninstall:
		python3 -m pip uninstall hexlet-code

lint:
		poetry run flake8 gendiff

pytest:
		poetry run  pytest --cov=gendiff

test-coverage:
		poetry run pytest --cov=gendiff --cov-report xml