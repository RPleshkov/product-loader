from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

engine = create_async_engine(
    url=settings.postgres.get_url,
    pool_size=settings.postgres.pool_size,
    max_overflow=settings.postgres.max_overflow,
    echo=settings.postgres.echo,
)


session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)
