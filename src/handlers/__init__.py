from faststream.nats import NatsRouter

from src.handlers.parse_stream import router as parse_stream_router

main_router = NatsRouter()

main_router.include_router(parse_stream_router)
