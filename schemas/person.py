from pydantic import BaseModel

class PersonSchema(BaseModel):
    """Define the schema for Person model."""

    id: int | None = None
    name: str | None = None
    last_name: str | None = None
    email: str | None = None
    phone: str | None = None
    title: str | None = None
    gender: str | None = None