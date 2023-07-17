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

from datetime import datetime
from typing import List, Optional, Union
from pydantic import BaseModel
from readarr.models.author_resource import AuthorResource
from readarr.models.book_resource import BookResource
from readarr.models.custom_format_resource import CustomFormatResource
from readarr.models.download_protocol import DownloadProtocol
from readarr.models.quality_model import QualityModel
from readarr.models.tracked_download_state import TrackedDownloadState
from readarr.models.tracked_download_status import TrackedDownloadStatus
from readarr.models.tracked_download_status_message import TrackedDownloadStatusMessage

class QueueResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    author_id: Optional[int]
    book_id: Optional[int]
    author: Optional[AuthorResource]
    book: Optional[BookResource]
    quality: Optional[QualityModel]
    custom_formats: Optional[List]
    custom_format_score: Optional[int]
    size: Optional[float]
    title: Optional[str]
    sizeleft: Optional[float]
    timeleft: Optional[str]
    estimated_completion_time: Optional[datetime]
    status: Optional[str]
    tracked_download_status: Optional[TrackedDownloadStatus]
    tracked_download_state: Optional[TrackedDownloadState]
    status_messages: Optional[List]
    error_message: Optional[str]
    download_id: Optional[str]
    protocol: Optional[DownloadProtocol]
    download_client: Optional[str]
    indexer: Optional[str]
    output_path: Optional[str]
    download_forced: Optional[bool]
    __properties = ["id", "authorId", "bookId", "author", "book", "quality", "customFormats", "customFormatScore", "size", "title", "sizeleft", "timeleft", "estimatedCompletionTime", "status", "trackedDownloadStatus", "trackedDownloadState", "statusMessages", "errorMessage", "downloadId", "protocol", "downloadClient", "indexer", "outputPath", "downloadForced"]

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
    def from_json(cls, json_str: str) -> QueueResource:
        """Create an instance of QueueResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of author
        if self.author:
            _dict['author'] = self.author.to_dict()
        # override the default output from pydantic by calling `to_dict()` of book
        if self.book:
            _dict['book'] = self.book.to_dict()
        # override the default output from pydantic by calling `to_dict()` of quality
        if self.quality:
            _dict['quality'] = self.quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in custom_formats (list)
        _items = []
        if self.custom_formats:
            for _item in self.custom_formats:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customFormats'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in status_messages (list)
        _items = []
        if self.status_messages:
            for _item in self.status_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['statusMessages'] = _items
        # set to None if author_id (nullable) is None
        if self.author_id is None:
            _dict['authorId'] = None

        # set to None if book_id (nullable) is None
        if self.book_id is None:
            _dict['bookId'] = None

        # set to None if custom_formats (nullable) is None
        if self.custom_formats is None:
            _dict['customFormats'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if estimated_completion_time (nullable) is None
        if self.estimated_completion_time is None:
            _dict['estimatedCompletionTime'] = None

        # set to None if status (nullable) is None
        if self.status is None:
            _dict['status'] = None

        # set to None if status_messages (nullable) is None
        if self.status_messages is None:
            _dict['statusMessages'] = None

        # set to None if error_message (nullable) is None
        if self.error_message is None:
            _dict['errorMessage'] = None

        # set to None if download_id (nullable) is None
        if self.download_id is None:
            _dict['downloadId'] = None

        # set to None if download_client (nullable) is None
        if self.download_client is None:
            _dict['downloadClient'] = None

        # set to None if indexer (nullable) is None
        if self.indexer is None:
            _dict['indexer'] = None

        # set to None if output_path (nullable) is None
        if self.output_path is None:
            _dict['outputPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> QueueResource:
        """Create an instance of QueueResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return QueueResource.parse_obj(obj)

        _obj = QueueResource.parse_obj({
            "id": obj.get("id"),
            "author_id": obj.get("authorId"),
            "book_id": obj.get("bookId"),
            "author": AuthorResource.from_dict(obj.get("author")) if obj.get("author") is not None else None,
            "book": BookResource.from_dict(obj.get("book")) if obj.get("book") is not None else None,
            "quality": QualityModel.from_dict(obj.get("quality")) if obj.get("quality") is not None else None,
            "custom_formats": [CustomFormatResource.from_dict(_item) for _item in obj.get("customFormats")] if obj.get("customFormats") is not None else None,
            "custom_format_score": obj.get("customFormatScore"),
            "size": obj.get("size"),
            "title": obj.get("title"),
            "sizeleft": obj.get("sizeleft"),
            "timeleft": obj.get("timeleft"),
            "estimated_completion_time": obj.get("estimatedCompletionTime"),
            "status": obj.get("status"),
            "tracked_download_status": obj.get("trackedDownloadStatus"),
            "tracked_download_state": obj.get("trackedDownloadState"),
            "status_messages": [TrackedDownloadStatusMessage.from_dict(_item) for _item in obj.get("statusMessages")] if obj.get("statusMessages") is not None else None,
            "error_message": obj.get("errorMessage"),
            "download_id": obj.get("downloadId"),
            "protocol": obj.get("protocol"),
            "download_client": obj.get("downloadClient"),
            "indexer": obj.get("indexer"),
            "output_path": obj.get("outputPath"),
            "download_forced": obj.get("downloadForced")
        })
        return _obj

