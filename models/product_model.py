from pydantic import BaseModel, RootModel


class ProductModel(BaseModel):
    title: str
    imageLocation: str | None = None
    categoryName: str
    price: str
    quantity: str | None = None


class ListProductModel(RootModel):
    root: list[ProductModel] = []
