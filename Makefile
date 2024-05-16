up: down
	docker compose -f docker-compose.dev.yml up --build

build:
	docker compose -f docker-compose.dev.yml build

down:
	docker compose -f docker-compose.dev.yml down
