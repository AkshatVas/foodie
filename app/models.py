from pydantic import BaseModel

class Restaurant(BaseModel):
    id: str
    name: str | None
    address: str | None
    city: str | None
    state: str | None
