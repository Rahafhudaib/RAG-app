from fastapi import FastAPI , APIRouter , Depends, UploadFile ,status
from SRC.controllers.DataContraller import DataController
from SRC.helpers.config import get_settings, Settings
from fastapi.responses import JSONResponse

data_router=APIRouter(prefix="/api_v_1/data", tags=["api_v_1","data"])
@data_router.get("/upload/{project_id}")
async def upload_data(project_id: str,file: UploadFile, app_settings: Settings = Depends(get_settings)):
   is_valid,signal = DataController().validate_upload_file(file)
   if not is_valid:
         return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"is_valid": is_valid, "signal": signal})
   return  {"is_valid": is_valid, "signal": signal}
