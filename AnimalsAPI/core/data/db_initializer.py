from core.data.database import get_db
from core.models.pet import Pet, AnimalType


def init_entities():
    """
        Данный метод создаёт три сущности, если таблица с питомцами пуста
    """
    db = get_db()
    if not db.query(Pet).all():
        pet1 = Pet(name="boy", type=AnimalType.cat)
        pet2 = Pet(name="girl", type=AnimalType.dog)
        pet3 = Pet(name="rex", type=AnimalType.dog)
        pets_to_add = [pet1, pet2, pet3]
        for pet in pets_to_add:
            db.add(pet)
        db.commit()
        db.close()
