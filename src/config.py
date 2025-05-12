from dataclasses import dataclass, field

from environs import Env
from pydantic import NatsDsn, PostgresDsn

env = Env()
env.read_env()


@dataclass
class PostgresConfig:

    host: str = env("DB_HOST")
    port: int = env.int("DB_PORT")
    name: str = env("DB_NAME")
    username: str = env("DB_USERNAME")
    password: str = env("DB_PASSWORD")

    pool_size: int = 20
    max_overflow: int = 5
    echo: bool = False

    def __post_init__(self):
        self.naming_convention: dict[str, str] = {
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }

    @property
    def get_url(self):
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
                path=self.name,
            )
        )


@dataclass
class NatsConfig:

    host: str = env("NATS_HOST")
    port: int = env.int("NATS_PORT")
    token: str = env("NATS_TOKEN")

    @property
    def get_url(self):
        return str(
            NatsDsn.build(
                scheme="nats",
                host=self.host,
                port=self.port,
            )
        )


@dataclass(frozen=True)
class Settings:

    postgres: PostgresConfig = field(default_factory=PostgresConfig)
    nats: NatsConfig = field(default_factory=NatsConfig)


settings = Settings()
