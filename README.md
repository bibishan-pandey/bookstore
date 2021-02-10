### BookStore

#### First Time Setup only

##### Make sure you install docker in your machine

Windows (yuck): https://docs.docker.com/docker-for-windows/install/

Linux: https://docs.docker.com/engine/install/ubuntu/

Mac: https://docs.docker.com/docker-for-mac/install/

##### Steps

1. Clone the repository

```
  git clone <repository_clone_url>
```

2. Install required python dependencies
```
  source venv/bin/activate
  pip install -r requirements.txt
```

#### Usage

```
  source venv/bin/activate
  python manage.py runserver
```

#### Running with docker-compose

1. (For windows only) Install Chocolatey: https://chocolatey.org/docs/installation
```
  choco install make
```

2. Build:
```
  make build
```

3. Run:
```
  make run
```

4. Make Migrations:
```
  make make_migrations
```

5. Migrate:
```
  make migrate
```

6. Create superuser:
```
  make superuser
```

7. Stop Docker:
```
  make stop
```

8. Clean Postgres Data (Run only when necessary):
```
  make clean
```

9. Running Test
```
  make test
```

10. Open Database Shell
```
  make db_shell
```

11. Open Bash
```
  make bash
```

#### Enable running test on each commit
Install pre-commit hook automatically runs with
```
  make build
```
This should enable running test and other configurations each time you commit.

2. To disable this feature, navigate to `.git/hooks` from root of the project and delete `pre-commit` sym link.

#### NOTE:

To run the django-server on the browser use [0.0.0.0:8000](http://0.0.0.0:8000/) or [127.0.0.1/8000](http://127.0.0.1:8000/) depending on the OS
