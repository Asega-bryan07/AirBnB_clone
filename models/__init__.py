#!/usr/bin/python3

"""
__init__ magic FileStorage for models directory
Initializes the package
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
