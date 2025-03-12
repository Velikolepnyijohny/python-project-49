install: build
	pip install .

brain-games: install
	brain-games

build:
	uv build
package-install: build
	uv tool install dist/*.whl
.PHONY: install build brain-games
