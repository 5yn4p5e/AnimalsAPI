from sqlalchemy.orm import Session
from core.dtos.pet_dto import PetDto
from core.models.pet import Pet


def create_pet(db: Session, pet_dto: PetDto):
    """
        Создаёт питомца в БД.
        Ответ - сущность питомца с заполненными id и временем создания
    """
    db_pet = Pet(name=pet_dto.name, type=pet_dto.type)
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    db.close()
    return db_pet


def get_pets(db: Session, limit: int = 20):
    """
        Выдаёт первые limit объектов из БД
    """
    pets_list = db.query(Pet).limit(limit).all()
    db.close()
    return pets_list


def get_pet(db: Session, pet_id: int):
    """
        Выдаёт питомца с заданным id.
        Обработка несуществующего id есть в endpoint'ах
    """
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    db.close()
    return pet


def update_pet(db: Session, pet_id: int, pet_dto: PetDto):
    """
        Обновляет питомца с заданным id.
        Обработка несуществующего id есть в endpoint'ах.
        Ответ - обновленная сущность с временем обновления
    """
    pet = db.query(Pet).filter(Pet.id == pet_id).first()
    pet.name = pet_dto.name
    pet.type = pet_dto.type
    db.commit()
    db.close()
    return pet


def delete_pet(db: Session, pet_id: int):
    """
        Удаляет питомца с заданным id.
        Возвращает True, если сущность с id была в бд,
        False - если таковой не нашлось
    """
    db_pet = db.query(Pet).filter(Pet.id == pet_id).first()
    if db_pet is not None:
        db.delete(db_pet)
        db.commit()
        db.close()
        return True
    return False
