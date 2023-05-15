# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from readarr.models.backup_type import BackupType

class BackupResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    path: Optional[str]
    type: Optional[BackupType]
    size: Optional[int]
    time: Optional[datetime]
    __properties = ["id", "name", "path", "type", "size", "time"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BackupResource:
        """Create an instance of BackupResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BackupResource:
        """Create an instance of BackupResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BackupResource.parse_obj(obj)

        _obj = BackupResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "type": obj.get("type"),
            "size": obj.get("size"),
            "time": obj.get("time")
        })
        return _obj

