
Fastapi Documents service (clean code version)

### Envs

| Name                   | Default value                   | Description                         |
|------------------------|---------------------------------|-------------------------------------|
| APP_PORT               | 8000                            | Port of application                 |
| PROJECT_NAME           | tz_3_calculate_markups_service  |                                     |
| GLOBAL_SERVICE_PATH    | ""                              | Path for api gateway                |
| DOCS_URL               | /docs                           | Settings for API documentation      |
| REDOC_URL              | /redoc                          | Settings for API documentation      |
| OPENAPI_URL            | /openapi.json                   | Settings for API documentation      |
| DEBUG                  | false                           | Enable for local development        |
| LOGGING_LEVEL          | INFO                            | Logging level                       |
| ACCESS_LOG             | false                           | Fastapi access logs                 |
| SERVICE_TOKEN          |                                 | Service token                       |

### Run tests

```shell
$ docker compose run --rm app pytest -s
```

### Run linting

Install flake8

```shell
pip install flake8
```

Run flake8

```shell
flake8
```

