from io import BytesIO, StringIO
from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from shared.schemas.delete_request import DeleteRequest
from shared.schemas.client import ClientUpdate, ClientCreate
import pandas as pd
from utils.CRUD_client import (
    get_all,
    delete,
    update,
    add
)

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_all", response_class=JSONResponse)
async def get_all_records():
    return await get_all()


@router.post("/delete", response_class=JSONResponse)
async def delete_record(data: DeleteRequest):
    result =  await delete(id=data.id)
    return {"success": result}


@router.post("/update", response_class=JSONResponse)
async def update_record(data: ClientUpdate):
    return await update(id=data.id, model_update=data)


@router.post("/add", response_class=JSONResponse)
async def add_record(data: ClientCreate):
    return await add(model_create=data)


@router.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    content: bytes = await file.read()
    if file.filename.endswith('.csv'):
        df: pd.DataFrame = pd.read_csv(StringIO(content.decode('utf-8')))
    elif file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
        df = pd.read_excel(BytesIO(content))
    else:
        raise HTTPException(status_code=400,
                            detail="Неподдерживаемый формат файла")
    return await add(df.to_dict(orient='records'))
