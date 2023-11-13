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


from typing import Any, ClassVar, Dict, Optional
from pydantic import BaseModel

class NamingConfigResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    rename_books: Optional[bool]
    replace_illegal_characters: Optional[bool]
    colon_replacement_format: Optional[int]
    standard_book_format: Optional[str]
    author_folder_format: Optional[str]
    include_author_name: Optional[bool]
    include_book_title: Optional[bool]
    include_quality: Optional[bool]
    replace_spaces: Optional[bool]
    separator: Optional[str]
    number_style: Optional[str]
    __properties = ["id", "renameBooks", "replaceIllegalCharacters", "colonReplacementFormat", "standardBookFormat", "authorFolderFormat", "includeAuthorName", "includeBookTitle", "includeQuality", "replaceSpaces", "separator", "numberStyle"]

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
    def from_json(cls, json_str: str) -> NamingConfigResource:
        """Create an instance of NamingConfigResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if standard_book_format (nullable) is None
        if self.standard_book_format is None:
            _dict['standardBookFormat'] = None

        # set to None if author_folder_format (nullable) is None
        if self.author_folder_format is None:
            _dict['authorFolderFormat'] = None

        # set to None if separator (nullable) is None
        if self.separator is None:
            _dict['separator'] = None

        # set to None if number_style (nullable) is None
        if self.number_style is None:
            _dict['numberStyle'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NamingConfigResource:
        """Create an instance of NamingConfigResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NamingConfigResource.parse_obj(obj)

        _obj = NamingConfigResource.parse_obj({
            "id": obj.get("id"),
            "rename_books": obj.get("renameBooks"),
            "replace_illegal_characters": obj.get("replaceIllegalCharacters"),
            "colon_replacement_format": obj.get("colonReplacementFormat"),
            "standard_book_format": obj.get("standardBookFormat"),
            "author_folder_format": obj.get("authorFolderFormat"),
            "include_author_name": obj.get("includeAuthorName"),
            "include_book_title": obj.get("includeBookTitle"),
            "include_quality": obj.get("includeQuality"),
            "replace_spaces": obj.get("replaceSpaces"),
            "separator": obj.get("separator"),
            "number_style": obj.get("numberStyle")
        })
        return _obj

