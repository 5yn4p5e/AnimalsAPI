from pydantic import BaseModel
from core.models.pet import AnimalType


class PetDto(BaseModel):
    """
        Необходим для более удобной работы с api
    """
    name: str
    type: AnimalType

    class Config:
        from_attributes = True
