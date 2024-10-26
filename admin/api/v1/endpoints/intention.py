from fastapi import APIRouter
from fastapi.responses import JSONResponse
from shared.schemas.delete_request import DeleteRequest
from shared.schemas.intention import IntentionUpdate, IntentionCreate
from utils.CRUD_intention import (
    get_all,
    delete,
    update,
    add
)

router = APIRouter(
    prefix="/Intention",
    tags=["Intention"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_all", response_class=JSONResponse)
async def get_all_records():
    return await get_all()


@router.post("/delete", response_class=JSONResponse)
async def delete_record(data: DeleteRequest):
    result = await delete(id=data.id)
    return {"success": result}


@router.post("/update", response_class=JSONResponse)
async def update_record(data: IntentionUpdate):
    return await update(id=data.id, model_update=data)


@router.post("/add", response_class=JSONResponse)
async def add_record(data: IntentionCreate):
    return await add(model_create=data)
