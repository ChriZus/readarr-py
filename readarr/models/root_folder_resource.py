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
from readarr.models.monitor_types import MonitorTypes
from readarr.models.new_item_monitor_types import NewItemMonitorTypes

class RootFolderResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    name: Optional[str]
    path: Optional[str]
    default_metadata_profile_id: Optional[int]
    default_quality_profile_id: Optional[int]
    default_monitor_option: Optional[MonitorTypes]
    default_new_item_monitor_option: Optional[NewItemMonitorTypes]
    default_tags: Optional[List]
    is_calibre_library: Optional[bool]
    host: Optional[str]
    port: Optional[int]
    url_base: Optional[str]
    username: Optional[str]
    password: Optional[str]
    library: Optional[str]
    output_format: Optional[str]
    output_profile: Optional[str]
    use_ssl: Optional[bool]
    accessible: Optional[bool]
    free_space: Optional[int]
    total_space: Optional[int]
    __properties = ["id", "name", "path", "defaultMetadataProfileId", "defaultQualityProfileId", "defaultMonitorOption", "defaultNewItemMonitorOption", "defaultTags", "isCalibreLibrary", "host", "port", "urlBase", "username", "password", "library", "outputFormat", "outputProfile", "useSsl", "accessible", "freeSpace", "totalSpace"]

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
    def from_json(cls, json_str: str) -> RootFolderResource:
        """Create an instance of RootFolderResource from a JSON string"""
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

        # set to None if default_tags (nullable) is None
        if self.default_tags is None:
            _dict['defaultTags'] = None

        # set to None if host (nullable) is None
        if self.host is None:
            _dict['host'] = None

        # set to None if url_base (nullable) is None
        if self.url_base is None:
            _dict['urlBase'] = None

        # set to None if username (nullable) is None
        if self.username is None:
            _dict['username'] = None

        # set to None if password (nullable) is None
        if self.password is None:
            _dict['password'] = None

        # set to None if library (nullable) is None
        if self.library is None:
            _dict['library'] = None

        # set to None if output_format (nullable) is None
        if self.output_format is None:
            _dict['outputFormat'] = None

        # set to None if output_profile (nullable) is None
        if self.output_profile is None:
            _dict['outputProfile'] = None

        # set to None if free_space (nullable) is None
        if self.free_space is None:
            _dict['freeSpace'] = None

        # set to None if total_space (nullable) is None
        if self.total_space is None:
            _dict['totalSpace'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RootFolderResource:
        """Create an instance of RootFolderResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RootFolderResource.parse_obj(obj)

        _obj = RootFolderResource.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "path": obj.get("path"),
            "default_metadata_profile_id": obj.get("defaultMetadataProfileId"),
            "default_quality_profile_id": obj.get("defaultQualityProfileId"),
            "default_monitor_option": obj.get("defaultMonitorOption"),
            "default_new_item_monitor_option": obj.get("defaultNewItemMonitorOption"),
            "default_tags": obj.get("defaultTags"),
            "is_calibre_library": obj.get("isCalibreLibrary"),
            "host": obj.get("host"),
            "port": obj.get("port"),
            "url_base": obj.get("urlBase"),
            "username": obj.get("username"),
            "password": obj.get("password"),
            "library": obj.get("library"),
            "output_format": obj.get("outputFormat"),
            "output_profile": obj.get("outputProfile"),
            "use_ssl": obj.get("useSsl"),
            "accessible": obj.get("accessible"),
            "free_space": obj.get("freeSpace"),
            "total_space": obj.get("totalSpace")
        })
        return _obj

