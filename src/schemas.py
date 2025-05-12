from pydantic import BaseModel


class ProductSchema(BaseModel):
    title: str
    guid: str | None
    origin: str
    code: str
    origin_url: str
    preview_img: str | None
    price: int
    other_info: dict
