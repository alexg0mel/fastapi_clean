
# Fastapi Documents service (clean code version) (monorepo version)
By the way, it just so happens that the development is being done as an Domain-Driven Design (DDD).


## Global challenges:
 - Minimal cohesion between layers,
 - minimal dependence on framework (fastapi)
 - monorepo

## Layers:
 - Models
 - Services
 - Infrastructure
 - - repository (async postgesql)
 - - messaging system (NATS)
 - - requests to other services - rest (aiohttp)
 - Controller (framework)
 - - App



### Envs

| Name                  | Default value | Description                    |
|-----------------------|---------------|--------------------------------|
| *_APP_PORT            | 8000          | Port of documents service      |
| *_PROJECT_NAME        | service       |                                |
| *_GLOBAL_SERVICE_PATH | ""            | Path for api gateway           |
| *_DOCS_URL            | /docs         | Settings for API documentation |
| *_REDOC_URL           | /redoc        | Settings for API documentation |
| *_OPENAPI_URL         | /openapi.json | Settings for API documentation |
| DEBUG                 | false         | Enable for local development   |
| LOGGING_LEVEL         | INFO          | Logging level                  |
| ACCESS_LOG            | false         | Fastapi access logs            |
| SERVICE_TOKEN         |               | Service token                  |
| *_POSTGRES_DB         |               | Service database name          |
| POSTGRES_USER         |               | Database user                  |
| POSTGRES_PASSWORD     |               | Database password              |
| POSTGRES_SERVICE      |               | Database host                  |
| POSTGRES_PORT         | 5432          | Database port                  |

### Run

```shell
$ make
```

### Run tests

```shell
$ make test
```

### Run linting

```shell
flake8
```

