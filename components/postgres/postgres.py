import pulumi
import pulumi_gcp as gcp


class PostgresDatabase(pulumi.ComponentResource):
    def __init__(self, name: str, opts=None, **kwargs):
        super().__init__("custom:database:PostgresDatabase", name, None, opts)

        config = pulumi.Config("postgres")
        region = config.get("region") or "europe-west1"
        tier = config.get("tier") or "db-custom-2-8192"
        database_version = config.get("databaseVersion") or "POSTGRES_15"
        disk_size = config.get_int("diskSize") or 50
        database_name = config.get("databaseName") or "app"

        self.instance = gcp.sql.DatabaseInstance(
            f"{name}-instance",
            name=name,
            database_version=database_version,
            region=region,
            deletion_protection=True,
            settings=gcp.sql.DatabaseInstanceSettingsArgs(
                tier=tier,
                disk_size=disk_size,
                backup_configuration=gcp.sql.DatabaseInstanceSettingsBackupConfigurationArgs(
                    enabled=True,
                    start_time="03:00",
                    point_in_time_recovery_enabled=True,
                ),
                maintenance_window=gcp.sql.DatabaseInstanceSettingsMaintenanceWindowArgs(
                    day=7,
                    hour=3,
                ),
                ip_configuration=gcp.sql.DatabaseInstanceSettingsIpConfigurationArgs(
                    ipv4_enabled=True,
                ),
                database_flags=[
                    gcp.sql.DatabaseInstanceSettingsDatabaseFlagArgs(
                        name="log_checkpoints",
                        value="on",
                    ),
                ],
            ),
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.database = gcp.sql.Database(
            f"{name}-db",
            name=database_name,
            instance=self.instance.name,
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.register_outputs(
            {
                "connectionName": self.instance.connection_name,
                "ipAddress": self.instance.ip_address,
                "databaseName": self.database.name,
            }
        )
