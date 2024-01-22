from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from core.data.database import get_db
from core.dtos.pet_dto import PetDto
from core.crud import pets_crud

router = APIRouter(
    prefix="/pets",
    tags=["pets"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.post("/", status_code=201)
def create_pet(pet_dto: PetDto, db: Session = Depends(get_db)):
    if len(pet_dto.name) > 30:
        raise HTTPException(status_code=400, detail="name must be less than 31 characters")
    return pets_crud.create_pet(db=db, pet_dto=pet_dto)


@router.get("/")
def read_pets(limit: int = 20, db: Session = Depends(get_db)):
    if limit < 1:
        raise HTTPException(status_code=400, detail="limit must be greater than 0")
    pets = pets_crud.get_pets(db, limit=limit)
    return pets


@router.get("/{pet_id}")
def read_pet(pet_id: int, db: Session = Depends(get_db)):
    db_pet = pets_crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


@router.put("/{pet_id}")
def update_pet(pet_id: int, pet_dto: PetDto, db: Session = Depends(get_db)):
    db_pet = pets_crud.update_pet(db, pet_id=pet_id, pet_dto=pet_dto)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return db_pet


@router.delete("/")
def delete_pets(ids: list[int], db: Session = Depends(get_db)):
    deleted_count = 0
    errors = []
    for pet_id in ids:
        if pets_crud.delete_pet(db, pet_id):
            deleted_count += 1
        else:
            errors.append({
                "id": pet_id,
                "error": "Pet with the matching ID was not found."
            })

    return {
        "deleted": deleted_count,
        "errors": errors
    }
