import glob
import os

import pulumi
import yaml

from components.postgres import PostgresDatabase

division = os.path.basename(os.path.dirname(__file__))

for path in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "postgres-*.yaml"))):
    name = os.path.splitext(os.path.basename(path))[0]
    with open(path) as f:
        cfg = yaml.safe_load(f).get("config", {})

    db = PostgresDatabase(
        f"{division}-{name}",
        region=cfg.get("postgres:region", "europe-west1"),
        tier=cfg.get("postgres:tier", "db-custom-2-8192"),
        database_version=cfg.get("postgres:databaseVersion", "POSTGRES_15"),
        disk_size=int(cfg.get("postgres:diskSize", "50")),
        database_name=cfg.get("postgres:databaseName", "app"),
    )

    pulumi.export(f"{name}/connectionName", db.instance.connection_name)
    pulumi.export(f"{name}/ipAddress", db.instance.ip_address)
    pulumi.export(f"{name}/databaseName", db.database.name)
