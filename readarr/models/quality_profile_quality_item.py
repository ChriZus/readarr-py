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


from typing import List, Optional
from pydantic import BaseModel
from readarr.models.quality import Quality

class QualityProfileQualityItem(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    quality: Optional[Quality]
    items: Optional[List]
    allowed: Optional[bool]
    __properties = ["id", "name", "quality", "items", "allowed"]

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
    def from_json(cls, json_str: str) -> QualityProfileQualityItem:
        """Create an instance of QualityProfileQualityItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if name (nullable) is None
        if self.name is None:
            _dict['name'] = None

        # set to None if items (nullable) is None
        if self.items is None:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualityProfileQualityItem:
        """Create an instance of QualityProfileQualityItem from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QualityProfileQualityItem.parse_obj(obj)

        _obj = QualityProfileQualityItem.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "quality": Quality.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "items": [QualityProfileQualityItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "allowed": obj.get("allowed")
        })
        return _obj

