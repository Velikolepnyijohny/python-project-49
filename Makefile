install:
	uv sync
brain-games:
	uv run brain-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check brain_games
brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime
