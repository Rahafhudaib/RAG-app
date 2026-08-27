from fastapi import FastAPI , APIRouter , Depends, UploadFile
from SRC.helpers.config import get_settings, Settings
from conrollers import DataContraller
data_router=APIRouter(prefix="/api_v_1/data", tags=["api_v_1","data"])
@data_router.get("/upload/{project_id}")
async def upload_data(project_id: str,file: UploadFile, app_settings: Settings = Depends(get_settings)):
   is_valid = DataContraller.DataController().validate_upload_file(file)
   return is_valid
