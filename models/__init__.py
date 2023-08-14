from .base_model import BaseModel
# Import other  from the models package if needed
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
