from fastapi import FastAPI , APIRouter
base_router=APIRouter(prefix="/api_v_1", tags=["api_v_1"])


@base_router.get("/")   ##اي ابليكيشن بالدنيا انتبهييي يكون برد عالديفلت راوت لاغراض الهيلث تشيك وغيرهم
def read_root():
    return {"Hello": "World"}