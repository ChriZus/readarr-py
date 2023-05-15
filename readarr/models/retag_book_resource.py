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
from readarr.models.tag_difference import TagDifference

class RetagBookResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    author_id: Optional[int]
    book_id: Optional[int]
    track_numbers: Optional[List]
    book_file_id: Optional[int]
    path: Optional[str]
    changes: Optional[List]
    __properties = ["id", "authorId", "bookId", "trackNumbers", "bookFileId", "path", "changes"]

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
    def from_json(cls, json_str: str) -> RetagBookResource:
        """Create an instance of RetagBookResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        # set to None if track_numbers (nullable) is None
        if self.track_numbers is None:
            _dict['trackNumbers'] = None

        # set to None if path (nullable) is None
        if self.path is None:
            _dict['path'] = None

        # set to None if changes (nullable) is None
        if self.changes is None:
            _dict['changes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RetagBookResource:
        """Create an instance of RetagBookResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RetagBookResource.parse_obj(obj)

        _obj = RetagBookResource.parse_obj({
            "id": obj.get("id"),
            "author_id": obj.get("authorId"),
            "book_id": obj.get("bookId"),
            "track_numbers": obj.get("trackNumbers"),
            "book_file_id": obj.get("bookFileId"),
            "path": obj.get("path"),
            "changes": [TagDifference.from_dict(_item) for _item in obj.get("changes")] if obj.get("changes") is not None else None
        })
        return _obj

