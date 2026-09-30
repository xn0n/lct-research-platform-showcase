# Дерево приватной реализации

Полный состав tracked-путей проверенной реализации: **93 файлов**. Дерево получено из Git; пути относительны корню приватного проекта. Содержимое файлов и рабочие данные здесь не опубликованы. Файлы из дерева не входят в эту витрину; это документ о составе реализации.

```text
/
├── backend/
│   ├── alembic/
│   │   ├── versions/
│   │   │   └── 0001_initial_schema.py
│   │   ├── env.py
│   │   ├── README
│   │   └── script.py.mako
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── excluded.py
│   │   │   │   ├── history.py
│   │   │   │   ├── results.py
│   │   │   │   ├── router.py
│   │   │   │   ├── searches.py
│   │   │   │   ├── session.py
│   │   │   │   └── technologies.py
│   │   │   ├── deps.py
│   │   │   └── health.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── errors.py
│   │   │   ├── exceptions.py
│   │   │   └── security.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   ├── compat.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── candidate.py
│   │   │   ├── idempotency.py
│   │   │   ├── job.py
│   │   │   ├── result.py
│   │   │   ├── search.py
│   │   │   ├── session.py
│   │   │   └── source.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── common.py
│   │   │   ├── error.py
│   │   │   ├── excluded.py
│   │   │   ├── health.py
│   │   │   ├── history.py
│   │   │   ├── result.py
│   │   │   ├── search.py
│   │   │   └── technology.py
│   │   ├── services/
│   │   │   ├── analysis/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── fixtures.py
│   │   │   │   ├── gateway.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── stub.py
│   │   │   │   └── verifier.py
│   │   │   ├── collection/
│   │   │   │   ├── connectors/
│   │   │   │   │   ├── arxiv.py
│   │   │   │   │   ├── base.py
│   │   │   │   │   ├── direct.py
│   │   │   │   │   ├── openalex.py
│   │   │   │   │   └── web.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── manager.py
│   │   │   │   ├── normalizer.py
│   │   │   │   ├── schemas.py
│   │   │   │   └── ssrf.py
│   │   │   ├── pagination.py
│   │   │   ├── pipeline.py
│   │   │   ├── search_service.py
│   │   │   └── session_service.py
│   │   ├── tasks/
│   │   │   ├── celery_app.py
│   │   │   └── worker.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_collection.py
│   │   ├── test_collection_pipeline.py
│   │   ├── test_e2e_api.py
│   │   ├── test_errors.py
│   │   ├── test_health.py
│   │   ├── test_scenarios_and_edge_cases.py
│   │   ├── test_schemas.py
│   │   └── test_security.py
│   ├── .env.example
│   ├── alembic.ini
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── pytest.ini
│   └── requirements.txt
├── collectors/
│   └── .gitkeep
├── frontend/
│   └── src/
│       └── .gitkeep
├── infra/
│   ├── .gitkeep
│   └── docker-compose.yml
├── ml/
│   ├── baseline/
│   │   └── .gitkeep
│   ├── classifier/
│   │   └── .gitkeep
│   ├── embeddings/
│   │   └── .gitkeep
│   ├── evaluation/
│   │   └── .gitkeep
│   ├── maturity/
│   │   └── .gitkeep
│   └── training/
│       └── .gitkeep
├── models/
│   ├── .gitkeep
│   └── README.md
├── tests/
│   └── .gitkeep
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

[Вернуться к витрине](../README.md) · [Архитектура](ARCHITECTURE.md)
