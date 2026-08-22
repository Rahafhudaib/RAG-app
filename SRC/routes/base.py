from fastapi import FastAPI , APIRouter
import os
base_router=APIRouter(prefix="/api_v_1", tags=["api_v_1"])


@base_router.get("/")   ##اي ابليكيشن بالدنيا انتبهييي يكون برد عالديفلت راوت لاغراض الهيلث تشيك وغيرهم
async def read_root():
    app_name=os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSION")
    return {"app_name": app_name, "app_version": app_version}
