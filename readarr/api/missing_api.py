# coding: utf-8

"""
    Readarr

    Readarr API docs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr

from typing import Optional

from readarr.models.book_resource import BookResource
from readarr.models.book_resource_paging_resource import BookResourcePagingResource
from readarr.models.sort_direction import SortDirection

from readarr.api_client import ApiClient
from readarr.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MissingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_wanted_missing(self, page : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_key : Optional[StrictStr] = None, sort_direction : Optional[SortDirection] = None, include_author : Optional[StrictBool] = None, monitored : Optional[StrictBool] = None, **kwargs) -> BookResourcePagingResource:  # noqa: E501
        """get_wanted_missing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_wanted_missing(page, page_size, sort_key, sort_direction, include_author, monitored, async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_author:
        :type include_author: bool
        :param monitored:
        :type monitored: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BookResourcePagingResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_wanted_missing_with_http_info(page, page_size, sort_key, sort_direction, include_author, monitored, **kwargs)  # noqa: E501

    @validate_arguments
    def get_wanted_missing_with_http_info(self, page : Optional[StrictInt] = None, page_size : Optional[StrictInt] = None, sort_key : Optional[StrictStr] = None, sort_direction : Optional[SortDirection] = None, include_author : Optional[StrictBool] = None, monitored : Optional[StrictBool] = None, **kwargs):  # noqa: E501
        """get_wanted_missing  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_wanted_missing_with_http_info(page, page_size, sort_key, sort_direction, include_author, monitored, async_req=True)
        >>> result = thread.get()

        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_author:
        :type include_author: bool
        :param monitored:
        :type monitored: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BookResourcePagingResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'page_size',
            'sort_key',
            'sort_direction',
            'include_author',
            'monitored'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wanted_missing" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))
        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))
        if _params.get('sort_key') is not None:  # noqa: E501
            _query_params.append(('sortKey', _params['sort_key']))
        if _params.get('sort_direction') is not None:  # noqa: E501
            _query_params.append(('sortDirection', _params['sort_direction']))
        if _params.get('include_author') is not None:  # noqa: E501
            _query_params.append(('includeAuthor', _params['include_author']))
        if _params.get('monitored') is not None:  # noqa: E501
            _query_params.append(('monitored', _params['monitored']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "BookResourcePagingResource",
        }

        return self.api_client.call_api(
            '/api/v1/wanted/missing', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_wanted_missing_by_id(self, id : StrictInt, **kwargs) -> BookResource:  # noqa: E501
        """get_wanted_missing_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_wanted_missing_by_id(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: BookResource
        """
        kwargs['_return_http_data_only'] = True
        return self.get_wanted_missing_by_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_wanted_missing_by_id_with_http_info(self, id : StrictInt, **kwargs):  # noqa: E501
        """get_wanted_missing_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_wanted_missing_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(BookResource, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_wanted_missing_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['apikey', 'X-Api-Key']  # noqa: E501

        _response_types_map = {
            '200': "BookResource",
        }

        return self.api_client.call_api(
            '/api/v1/wanted/missing/{id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
