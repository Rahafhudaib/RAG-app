from SRC.controllers.BaseContraller import BaseController
from fastapi import UploadFile
from SRC.models.enums.ResponseEnums import ResponseSignal as ResponseEnums
class DataController(BaseController):
    def __init__(self):
        super().__init__()  
        self.filesize_scale = 1024 * 1024  # 1 MB in bytes
    def validate_upload_file(self, file: UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseEnums.FILE_TYPE_NOT_ALLOWED.value
        if file.size > self.app_settings.FILE_MAX_SIZE_MB * self.filesize_scale:
            return False, ResponseEnums.FILE_SIZE_EXCEEDED.value
        return True, ResponseEnums.FILE_VALIDATE_SUCCESS.value
        