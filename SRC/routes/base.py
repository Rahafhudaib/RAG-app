from fastapi import FastAPI , APIRouter
from SRC.helpers.config import get_settings
base_router=APIRouter(prefix="/api_v_1", tags=["api_v_1"])


@base_router.get("/")   ##اي ابليكيشن بالدنيا انتبهييي يكون برد عالديفلت راوت لاغراض الهيلث تشيك وغيرهم
async def read_root():
    app_settings = get_settings()
    app_name=app_settings.APP_NAME
    app_version=app_settings.APP_VERSION
    return {"app_name": app_name, "app_version": app_version}
