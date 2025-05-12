from faststream import Logger
from faststream.nats import NatsRouter, PullSub
from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.database.models import OtherInfo, Product
from src.database.session import session_factory
from src.schemas import ProductSchema

router = NatsRouter()


@router.subscriber(
    durable="TEST_STREAM",
    stream="TEST_STREAM",
    subject="TEST_STREAM",
    pull_sub=PullSub(batch_size=20, timeout=10),
)
async def message_handler(
    data: list[ProductSchema],
    logger: Logger,
):
    product_dicts = [product.model_dump(exclude={"other_info"}) for product in data]
    try:
        async with session_factory() as session:
            async with session.begin():
                result = await session.execute(
                    insert(Product).returning(Product), product_dicts
                )
                inserted_products = result.scalars().all()

                other_infos = [
                    {"product_id": p.id, "other_info": data[i].other_info}
                    for i, p in enumerate(inserted_products)
                ]

                if other_infos:
                    await session.execute(insert(OtherInfo), other_infos)
    except IntegrityError as e:
        logger.warning("Дублирование по guid: %s" % [i.guid for i in data])
    except SQLAlchemyError as e:
        logger.error("Ошибка SQLAlchemy: %s" % e, exc_info=True)
    except ConnectionRefusedError as e:
        logger.critical("Ошибка подключения к базе данных: %s" % e)
    except Exception as e:
        logger.critical("Неожиданная ошибка: %s" % e, exc_info=True)
