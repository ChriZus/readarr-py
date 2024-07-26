# coding: utf-8

"""
    Readarr

    Readarr API docs

    The version of the OpenAPI document: v0.3.18.2411
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr
from typing import Optional
from readarr.models.queue_bulk_resource import QueueBulkResource
from readarr.models.queue_resource_paging_resource import QueueResourcePagingResource
from readarr.models.sort_direction import SortDirection

from readarr.api_client import ApiClient, RequestSerialized
from readarr.api_response import ApiResponse
from readarr.rest import RESTResponseType


class QueueApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def delete_queue(
        self,
        id: StrictInt,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """delete_queue


        :param id: (required)
        :type id: int
        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_serialize(
            id=id,
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_queue_with_http_info(
        self,
        id: StrictInt,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """delete_queue


        :param id: (required)
        :type id: int
        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_serialize(
            id=id,
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_queue_without_preload_content(
        self,
        id: StrictInt,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """delete_queue


        :param id: (required)
        :type id: int
        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_serialize(
            id=id,
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_queue_serialize(
        self,
        id,
        remove_from_client,
        blocklist,
        skip_redownload,
        change_category,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if remove_from_client is not None:
            
            _query_params.append(('removeFromClient', remove_from_client))
            
        if blocklist is not None:
            
            _query_params.append(('blocklist', blocklist))
            
        if skip_redownload is not None:
            
            _query_params.append(('skipRedownload', skip_redownload))
            
        if change_category is not None:
            
            _query_params.append(('changeCategory', change_category))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter




        # authentication setting
        _auth_settings: List[str] = [
            'apikey', 
            'X-Api-Key'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/queue/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def delete_queue_bulk(
        self,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        queue_bulk_resource: Optional[QueueBulkResource] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """delete_queue_bulk


        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param queue_bulk_resource:
        :type queue_bulk_resource: QueueBulkResource
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_bulk_serialize(
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            queue_bulk_resource=queue_bulk_resource,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_queue_bulk_with_http_info(
        self,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        queue_bulk_resource: Optional[QueueBulkResource] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """delete_queue_bulk


        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param queue_bulk_resource:
        :type queue_bulk_resource: QueueBulkResource
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_bulk_serialize(
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            queue_bulk_resource=queue_bulk_resource,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_queue_bulk_without_preload_content(
        self,
        remove_from_client: Optional[StrictBool] = None,
        blocklist: Optional[StrictBool] = None,
        skip_redownload: Optional[StrictBool] = None,
        change_category: Optional[StrictBool] = None,
        queue_bulk_resource: Optional[QueueBulkResource] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """delete_queue_bulk


        :param remove_from_client:
        :type remove_from_client: bool
        :param blocklist:
        :type blocklist: bool
        :param skip_redownload:
        :type skip_redownload: bool
        :param change_category:
        :type change_category: bool
        :param queue_bulk_resource:
        :type queue_bulk_resource: QueueBulkResource
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_queue_bulk_serialize(
            remove_from_client=remove_from_client,
            blocklist=blocklist,
            skip_redownload=skip_redownload,
            change_category=change_category,
            queue_bulk_resource=queue_bulk_resource,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _delete_queue_bulk_serialize(
        self,
        remove_from_client,
        blocklist,
        skip_redownload,
        change_category,
        queue_bulk_resource,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if remove_from_client is not None:
            
            _query_params.append(('removeFromClient', remove_from_client))
            
        if blocklist is not None:
            
            _query_params.append(('blocklist', blocklist))
            
        if skip_redownload is not None:
            
            _query_params.append(('skipRedownload', skip_redownload))
            
        if change_category is not None:
            
            _query_params.append(('changeCategory', change_category))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if queue_bulk_resource is not None:
            _body_params = queue_bulk_resource



        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json', 
                        'text/json', 
                        'application/*+json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        # authentication setting
        _auth_settings: List[str] = [
            'apikey', 
            'X-Api-Key'
        ]

        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/api/v1/queue/bulk',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def get_queue(
        self,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        sort_key: Optional[StrictStr] = None,
        sort_direction: Optional[SortDirection] = None,
        include_unknown_author_items: Optional[StrictBool] = None,
        include_author: Optional[StrictBool] = None,
        include_book: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> QueueResourcePagingResource:
        """get_queue


        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_unknown_author_items:
        :type include_unknown_author_items: bool
        :param include_author:
        :type include_author: bool
        :param include_book:
        :type include_book: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_queue_serialize(
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_unknown_author_items=include_unknown_author_items,
            include_author=include_author,
            include_book=include_book,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': "QueueResourcePagingResource",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_queue_with_http_info(
        self,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        sort_key: Optional[StrictStr] = None,
        sort_direction: Optional[SortDirection] = None,
        include_unknown_author_items: Optional[StrictBool] = None,
        include_author: Optional[StrictBool] = None,
        include_book: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[QueueResourcePagingResource]:
        """get_queue


        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_unknown_author_items:
        :type include_unknown_author_items: bool
        :param include_author:
        :type include_author: bool
        :param include_book:
        :type include_book: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_queue_serialize(
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_unknown_author_items=include_unknown_author_items,
            include_author=include_author,
            include_book=include_book,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': "QueueResourcePagingResource",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_queue_without_preload_content(
        self,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        sort_key: Optional[StrictStr] = None,
        sort_direction: Optional[SortDirection] = None,
        include_unknown_author_items: Optional[StrictBool] = None,
        include_author: Optional[StrictBool] = None,
        include_book: Optional[StrictBool] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """get_queue


        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param sort_key:
        :type sort_key: str
        :param sort_direction:
        :type sort_direction: SortDirection
        :param include_unknown_author_items:
        :type include_unknown_author_items: bool
        :param include_author:
        :type include_author: bool
        :param include_book:
        :type include_book: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_queue_serialize(
            page=page,
            page_size=page_size,
            sort_key=sort_key,
            sort_direction=sort_direction,
            include_unknown_author_items=include_unknown_author_items,
            include_author=include_author,
            include_book=include_book,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '2XX': "QueueResourcePagingResource",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_queue_serialize(
        self,
        page,
        page_size,
        sort_key,
        sort_direction,
        include_unknown_author_items,
        include_author,
        include_book,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if sort_key is not None:
            
            _query_params.append(('sortKey', sort_key))
            
        if sort_direction is not None:
            
            _query_params.append(('sortDirection', sort_direction.value))
            
        if include_unknown_author_items is not None:
            
            _query_params.append(('includeUnknownAuthorItems', include_unknown_author_items))
            
        if include_author is not None:
            
            _query_params.append(('includeAuthor', include_author))
            
        if include_book is not None:
            
            _query_params.append(('includeBook', include_book))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'apikey', 
            'X-Api-Key'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/api/v1/queue',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


