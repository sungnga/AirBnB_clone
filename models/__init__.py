#!/usr/bin/python3
"""Initialization for Models"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
