up: down build
	docker compose -f docker-compose.dev.yml up

build:
	docker compose -f docker-compose.dev.yml build --build-arg SERVICE="documents"

down:
	docker compose -f docker-compose.dev.yml down

test:
	docker compose run --build --rm app pytest -s
