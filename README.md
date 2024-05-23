
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

| Name                | Default value | Description                    |
|---------------------|---------------|--------------------------------|
| DOCUMENTS_APP_PORT  | 8000          | Port of documents service      |
| PROJECT_NAME        | service       |                                |
| GLOBAL_SERVICE_PATH | ""            | Path for api gateway           |
| DOCS_URL            | /docs         | Settings for API documentation |
| REDOC_URL           | /redoc        | Settings for API documentation |
| OPENAPI_URL         | /openapi.json | Settings for API documentation |
| DEBUG               | false         | Enable for local development   |
| LOGGING_LEVEL       | INFO          | Logging level                  |
| ACCESS_LOG          | false         | Fastapi access logs            |
| SERVICE_TOKEN       |               | Service token                  |

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

