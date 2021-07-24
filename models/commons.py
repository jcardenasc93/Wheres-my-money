""" Module with commons definitions for the app Schemas """

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class DateTimeModelMixin(BaseModel):
    """ Model mixin definition for created_at and
    updated_at fields
    """
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()


class AppObjectId(ObjectId):
    """ This class is a custom validator regards Pydantic
    doesn't support ObjectId types, and MongoDB documents has
    an '_id' field with this type
    """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectId')
        return ObjectId(v)

    @classmethod
    def __modifiy_schema__(cls, field_schema):
        field_schema.update(type='string')


class DocumentIdMixin(BaseModel):
    id_: Optional[AppObjectId] = Field(alias="_id")
