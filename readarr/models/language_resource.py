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


from typing import Optional
from pydantic import BaseModel

class LanguageResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    name_lower: Optional[str]
    __properties = ["id", "name", "nameLower"]

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
    def from_json(cls, json_str: str) -> LanguageResource:
        """Create an instance of LanguageResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "name_lower",
                          },
                          exclude_none=True)
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if name_lower (nullable) is None
        if self.name_lower is None:
            _dict['nameLower'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LanguageResource:
        """Create an instance of LanguageResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return LanguageResource.parse_obj(obj)

        _obj = LanguageResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "name_lower": obj.get("nameLower")
        })
        return _obj

