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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from readarr.models.quality_model import QualityModel
from typing import Optional, Set
from typing_extensions import Self

class BookFileListResource(BaseModel):
    """
    BookFileListResource
    """ # noqa: E501
    book_file_ids: Optional[List[StrictInt]] = Field(default=None, alias="bookFileIds")
    quality: Optional[QualityModel] = None
    __properties: ClassVar[List[str]] = ["bookFileIds", "quality"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BookFileListResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # set to None if book_file_ids (nullable) is None
        # and model_fields_set contains the field
        if self.book_file_ids is None and "book_file_ids" in self.model_fields_set:
            _dict['bookFileIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BookFileListResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bookFileIds": obj.get("bookFileIds"),
            "quality": QualityModel.from_dict(obj["quality"]) if obj.get("quality") is not None else None
        })
        return _obj


