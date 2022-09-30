#!/usr/bin/python
"""Contains City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
