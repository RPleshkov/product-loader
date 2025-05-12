from faststream import FastStream
from faststream.nats import NatsBroker

from src.config import settings
from src.handlers import main_router

broker = NatsBroker(
    servers=settings.nats.get_url,
    token=settings.nats.token,
)

broker.include_router(main_router)

app = FastStream(broker)
