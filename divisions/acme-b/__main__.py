import pulumi
from components.postgres import PostgresDatabase

db = PostgresDatabase("acme-b-postgres")

pulumi.export("connectionName", db.instance.connection_name)
pulumi.export("ipAddress", db.instance.ip_address)
pulumi.export("databaseName", db.database.name)
