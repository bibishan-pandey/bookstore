build:
	docker-compose build --no-cache
	docker-compose up -d --force-recreate

up:
	docker-compose up -d

run: up
	docker-compose run app sh -c "pre-commit install && pre-commit install -t pre-push"
	docker-compose exec app pre-commit run

make_migrations: up
	docker-compose exec app python manage.py makemigrations

migrate: up
	docker-compose exec app python manage.py migrate

fake_migrate: up
	docker-compose exec app python manage.py migrate --fake

bash: up
	docker-compose exec app /bin/bash

test:
	docker-compose exec -T app pytest

db_shell: up
	docker exec -it bookstore_db_1 /bin/bash

superuser: up
	docker-compose exec app python manage.py createsuperuser

stop:
	docker-compose down

clean:
	rm -rf postgres_data
