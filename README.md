# Central IaC Repository (Pulumi)

Central repository for managing GCP infrastructure via Pulumi, organized by division. New databases are added through a Backstage template that creates a Pull Request.

## Adding a New PostgreSQL Database

Use the **GCP - PostgreSQL Database** template in Backstage to add a new Cloud SQL PostgreSQL instance for a division. The template creates a Pull Request with the Pulumi configuration, which gets applied automatically after merge.

## Repository Structure

```
.
├── divisions/                 # One directory per division/suborganization
│   ├── acme-a/
│   │   ├── Pulumi.yaml        # Pulumi project definition
│   │   ├── Pulumi.production.yaml
│   │   └── postgres.yaml      # PostgreSQL database config
│   └── acme-b/
│       ├── Pulumi.yaml
│       ├── Pulumi.production.yaml
│       └── postgres.yaml
├── components/postgres/       # Shared Pulumi component for PostgreSQL
│   ├── __init__.py
│   └── postgres.py
├── templates/postgres/        # Backstage scaffolder template
│   ├── template.yaml
│   └── skeleton/
└── README.md
```

## CI/CD

- **Pull Requests:** `pulumi preview` runs for any changed divisions
- **Merge to main:** `pulumi up` runs automatically for changed divisions
