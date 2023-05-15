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
from typing import List, Optional
from pydantic import BaseModel
from readarr.models.links import Links
from readarr.models.media_cover import MediaCover
from readarr.models.ratings import Ratings

class EditionResource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[int]
    book_id: Optional[int]
    foreign_edition_id: Optional[str]
    title_slug: Optional[str]
    isbn13: Optional[str]
    asin: Optional[str]
    title: Optional[str]
    language: Optional[str]
    overview: Optional[str]
    format: Optional[str]
    is_ebook: Optional[bool]
    disambiguation: Optional[str]
    publisher: Optional[str]
    page_count: Optional[int]
    release_date: Optional[datetime]
    images: Optional[List]
    links: Optional[List]
    ratings: Optional[Ratings]
    monitored: Optional[bool]
    manual_add: Optional[bool]
    remote_cover: Optional[str]
    grabbed: Optional[bool]
    __properties = ["id", "bookId", "foreignEditionId", "titleSlug", "isbn13", "asin", "title", "language", "overview", "format", "isEbook", "disambiguation", "publisher", "pageCount", "releaseDate", "images", "links", "ratings", "monitored", "manualAdd", "remoteCover", "grabbed"]

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
    def from_json(cls, json_str: str) -> EditionResource:
        """Create an instance of EditionResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of ratings
        if self.ratings:
            _dict['ratings'] = self.ratings.to_dict()
        # set to None if foreign_edition_id (nullable) is None
        if self.foreign_edition_id is None:
            _dict['foreignEditionId'] = None

        # set to None if title_slug (nullable) is None
        if self.title_slug is None:
            _dict['titleSlug'] = None

        # set to None if isbn13 (nullable) is None
        if self.isbn13 is None:
            _dict['isbn13'] = None

        # set to None if asin (nullable) is None
        if self.asin is None:
            _dict['asin'] = None

        # set to None if title (nullable) is None
        if self.title is None:
            _dict['title'] = None

        # set to None if language (nullable) is None
        if self.language is None:
            _dict['language'] = None

        # set to None if overview (nullable) is None
        if self.overview is None:
            _dict['overview'] = None

        # set to None if format (nullable) is None
        if self.format is None:
            _dict['format'] = None

        # set to None if disambiguation (nullable) is None
        if self.disambiguation is None:
            _dict['disambiguation'] = None

        # set to None if publisher (nullable) is None
        if self.publisher is None:
            _dict['publisher'] = None

        # set to None if release_date (nullable) is None
        if self.release_date is None:
            _dict['releaseDate'] = None

        # set to None if images (nullable) is None
        if self.images is None:
            _dict['images'] = None

        # set to None if links (nullable) is None
        if self.links is None:
            _dict['links'] = None

        # set to None if remote_cover (nullable) is None
        if self.remote_cover is None:
            _dict['remoteCover'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EditionResource:
        """Create an instance of EditionResource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return EditionResource.parse_obj(obj)

        _obj = EditionResource.parse_obj({
            "id": obj.get("id"),
            "book_id": obj.get("bookId"),
            "foreign_edition_id": obj.get("foreignEditionId"),
            "title_slug": obj.get("titleSlug"),
            "isbn13": obj.get("isbn13"),
            "asin": obj.get("asin"),
            "title": obj.get("title"),
            "language": obj.get("language"),
            "overview": obj.get("overview"),
            "format": obj.get("format"),
            "is_ebook": obj.get("isEbook"),
            "disambiguation": obj.get("disambiguation"),
            "publisher": obj.get("publisher"),
            "page_count": obj.get("pageCount"),
            "release_date": obj.get("releaseDate"),
            "images": [MediaCover.from_dict(_item) for _item in obj.get("images")] if obj.get("images") is not None else None,
            "links": [Links.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "ratings": Ratings.from_dict(obj.get("ratings")) if obj.get("ratings") is not None else None,
            "monitored": obj.get("monitored"),
            "manual_add": obj.get("manualAdd"),
            "remote_cover": obj.get("remoteCover"),
            "grabbed": obj.get("grabbed")
        })
        return _obj

