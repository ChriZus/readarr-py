# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.3.18.2411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RescanAfterRefreshType(str, Enum):
    """
    RescanAfterRefreshType
    """

    """
    allowed enum values
    """
    ALWAYS = 'always'
    AFTERMANUAL = 'afterManual'
    NEVER = 'never'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RescanAfterRefreshType from a JSON string"""
        return cls(json.loads(json_str))


