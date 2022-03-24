install:
	poetry install

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

small-games:
	poetry run small-games
