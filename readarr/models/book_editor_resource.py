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

class BookEditorResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    book_ids: Optional[List]
    monitored: Optional[bool]
    delete_files: Optional[bool]
    add_import_list_exclusion: Optional[bool]
    __properties = ["bookIds", "monitored", "deleteFiles", "addImportListExclusion"]

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
    def from_json(cls, json_str: str) -> BookEditorResource:
        """Create an instance of BookEditorResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if book_ids (nullable) is None
        if self.book_ids is None:
            _dict['bookIds'] = None

        # set to None if monitored (nullable) is None
        if self.monitored is None:
            _dict['monitored'] = None

        # set to None if delete_files (nullable) is None
        if self.delete_files is None:
            _dict['deleteFiles'] = None

        # set to None if add_import_list_exclusion (nullable) is None
        if self.add_import_list_exclusion is None:
            _dict['addImportListExclusion'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BookEditorResource:
        """Create an instance of BookEditorResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return BookEditorResource.parse_obj(obj)

        _obj = BookEditorResource.parse_obj({
            "book_ids": obj.get("bookIds"),
            "monitored": obj.get("monitored"),
            "delete_files": obj.get("deleteFiles"),
            "add_import_list_exclusion": obj.get("addImportListExclusion")
        })
        return _obj

