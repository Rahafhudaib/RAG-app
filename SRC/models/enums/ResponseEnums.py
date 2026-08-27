from enum import Enum

class ResponseSignal(Enum):
    FILE_VALIDATE_SUCCESS = "File validation successful."
    FILE_VALIDATE_FAILURE = "File validation failed."
    FILE_TYPE_NOT_ALLOWED = "File type not allowed."
    FILE_SIZE_EXCEEDED = "File size exceeded the maximum limit."
    FILE_UPLOAD_SUCCESS = "File uploaded successfully."
    FILE_UPLOAD_FAILURE = "File upload failed."