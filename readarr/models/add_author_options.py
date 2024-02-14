# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.3.18.2411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.monitor_types import MonitorTypes
from typing import Optional, Set
from typing_extensions import Self

class AddAuthorOptions(BaseModel):
    """
    AddAuthorOptions
    """ # noqa: E501
    monitor: Optional[MonitorTypes] = None
    books_to_monitor: Optional[List[StrictStr]] = Field(default=None, alias="booksToMonitor")
    monitored: Optional[StrictBool] = None
    search_for_missing_books: Optional[StrictBool] = Field(default=None, alias="searchForMissingBooks")
    __properties: ClassVar[List[str]] = ["monitor", "booksToMonitor", "monitored", "searchForMissingBooks"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AddAuthorOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if books_to_monitor (nullable) is None
        # and model_fields_set contains the field
        if self.books_to_monitor is None and "books_to_monitor" in self.model_fields_set:
            _dict['booksToMonitor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddAuthorOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "monitor": obj.get("monitor"),
            "booksToMonitor": obj.get("booksToMonitor"),
            "monitored": obj.get("monitored"),
            "searchForMissingBooks": obj.get("searchForMissingBooks")
        })
        return _obj


