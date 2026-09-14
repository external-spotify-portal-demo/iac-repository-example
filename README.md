# Central IaC Repository (Pulumi)

Central repository for managing GCP infrastructure via Pulumi, organized by division. New databases are added through a Backstage template that creates a Pull Request.

## Adding a New PostgreSQL Database

Use the **GCP - PostgreSQL Database** template in Backstage to add a new Cloud SQL PostgreSQL instance. The template drops a `postgres-<name>.yaml` config file into the chosen division's directory and opens a Pull Request.

Each division's `__main__.py` auto-discovers all `postgres-*.yaml` files and provisions one database per file.

## Repository Structure

```
.
├── divisions/                 # One directory per division/suborganization
│   ├── acme-a/
│   │   ├── Pulumi.yaml        # Pulumi project definition
│   │   ├── Pulumi.production.yaml
│   │   ├── __main__.py        # Auto-discovers postgres-*.yaml files
│   │   └── postgres-app.yaml  # A PostgreSQL database config
│   └── acme-b/
│       ├── Pulumi.yaml
│       ├── Pulumi.production.yaml
│       ├── __main__.py
│       └── postgres-app.yaml
├── components/postgres/       # Shared Pulumi component for PostgreSQL
├── templates/postgres/        # Backstage scaffolder template
└── README.md
```

## CI/CD

- **Pull Requests:** `pulumi preview` runs for any changed divisions
- **Merge to main:** `pulumi up` runs automatically for changed divisions
