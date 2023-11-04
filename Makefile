install:
	poetry install

diff:
	poetry run gendiff gendiff/tests/fixtures/json/nested_file1.json gendiff/tests/fixtures/json/nested_file2.json

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
