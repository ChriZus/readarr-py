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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from readarr.models.profile_format_item import ProfileFormatItem
from readarr.models.quality_profile_quality_item import QualityProfileQualityItem

class QualityProfile(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    upgrade_allowed: Optional[bool]
    cutoff: Optional[int]
    min_format_score: Optional[int]
    cutoff_format_score: Optional[int]
    format_items: Optional[List]
    items: Optional[List]
    __properties = ["id", "name", "upgradeAllowed", "cutoff", "minFormatScore", "cutoffFormatScore", "formatItems", "items"]

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
    def from_json(cls, json_str: str) -> QualityProfile:
        """Create an instance of QualityProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in format_items (list)
        _items = []
        if self.format_items:
            for _item in self.format_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formatItems'] = _items
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

        # set to None if format_items (nullable) is None
        if self.format_items is None:
            _dict['formatItems'] = None

        # set to None if items (nullable) is None
        if self.items is None:
            _dict['items'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QualityProfile:
        """Create an instance of QualityProfile from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QualityProfile.parse_obj(obj)

        _obj = QualityProfile.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "upgrade_allowed": obj.get("upgradeAllowed"),
            "cutoff": obj.get("cutoff"),
            "min_format_score": obj.get("minFormatScore"),
            "cutoff_format_score": obj.get("cutoffFormatScore"),
            "format_items": [ProfileFormatItem.from_dict(_item) for _item in obj.get("formatItems")] if obj.get("formatItems") is not None else None,
            "items": [QualityProfileQualityItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj

