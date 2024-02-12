# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MetadataProfileResource(BaseModel):
    """
    MetadataProfileResource
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    min_popularity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minPopularity")
    skip_missing_date: Optional[StrictBool] = Field(default=None, alias="skipMissingDate")
    skip_missing_isbn: Optional[StrictBool] = Field(default=None, alias="skipMissingIsbn")
    skip_parts_and_sets: Optional[StrictBool] = Field(default=None, alias="skipPartsAndSets")
    skip_series_secondary: Optional[StrictBool] = Field(default=None, alias="skipSeriesSecondary")
    allowed_languages: Optional[StrictStr] = Field(default=None, alias="allowedLanguages")
    min_pages: Optional[StrictInt] = Field(default=None, alias="minPages")
    ignored: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "minPopularity", "skipMissingDate", "skipMissingIsbn", "skipPartsAndSets", "skipSeriesSecondary", "allowedLanguages", "minPages", "ignored"]

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
        """Create an instance of MetadataProfileResource from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if allowed_languages (nullable) is None
        # and model_fields_set contains the field
        if self.allowed_languages is None and "allowed_languages" in self.model_fields_set:
            _dict['allowedLanguages'] = None

        # set to None if ignored (nullable) is None
        # and model_fields_set contains the field
        if self.ignored is None and "ignored" in self.model_fields_set:
            _dict['ignored'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MetadataProfileResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "minPopularity": obj.get("minPopularity"),
            "skipMissingDate": obj.get("skipMissingDate"),
            "skipMissingIsbn": obj.get("skipMissingIsbn"),
            "skipPartsAndSets": obj.get("skipPartsAndSets"),
            "skipSeriesSecondary": obj.get("skipSeriesSecondary"),
            "allowedLanguages": obj.get("allowedLanguages"),
            "minPages": obj.get("minPages"),
            "ignored": obj.get("ignored")
        })
        return _obj


