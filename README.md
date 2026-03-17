# Forge Backend

Django REST API + Task Engine za Forge platformu.

## Tehnologije

- Python 3.12
- Django 4.2.17
- Django REST Framework
- Celery 5
- PostgreSQL 15
- Redis 7
- Channels 4 (WebSocket)
- Receptor (distributed execution)

## Struktura

```
forge/
├── api/          # REST API (DRF views, serializers, permissions)
├── main/         # Core modeli, signali, tasks, migracije
├── conf/         # Konfiguracija i database-backed settings
├── sso/          # SSO integracija (LDAP, SAML, Social Auth)
├── settings/     # Django settings (development, production)
├── playbooks/    # Ansible playbooks za job execution
├── locale/       # Internacionalizacija
└── ui/           # Legacy UI (awx compatibility)
```

## Development

```bash
# Vagrant VM (obavezno za razvoj)
vagrant up
vagrant ssh

# Pokretanje testova
pytest forge/main/tests/unit/ -v
pytest forge/main/tests/functional/ -v

# Lint
flake8
```

## API

Base URL: `/api/v2/`

Pogledaj [docs/11-api-reference.md](docs/11-api-reference.md) za kompletnu referencu.

## Dokumentacija

- [Backend Django](docs/02-backend-django.md)
- [Task Engine](docs/04-task-engine.md)
- [Authentication & RBAC](docs/05-authentication-rbac.md)
- [Database Schema](docs/06-database-schema.md)
- [Testing Guide](docs/09-testing-guide.md)
- [API Reference](docs/11-api-reference.md)
- [Configuration Reference](docs/12-configuration-reference.md)

## Docker

```bash
docker build -t krlex/forge-backend:latest .
```

## Povezani repozitorijumi

- [forge-frontend](https://github.com/forgeplatform/forge-frontend) — React UI
- [forge-deploy](https://github.com/forgeplatform/forge-deploy) — Docker Compose, Nginx, CI/CD
