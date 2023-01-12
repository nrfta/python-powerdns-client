# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from powerdns_client.api_client import ApiClient


class AutoprimaryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_autoprimary(self, autoprimary, server_id, **kwargs):  # noqa: E501
        """Add an autoprimary  # noqa: E501

        This methods add a new autoprimary server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_autoprimary(autoprimary, server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Autoprimary autoprimary: autoprimary entry to add (required)
        :param str server_id: The id of the server to manage the list of autoprimaries on (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_autoprimary_with_http_info(autoprimary, server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_autoprimary_with_http_info(autoprimary, server_id, **kwargs)  # noqa: E501
            return data

    def create_autoprimary_with_http_info(self, autoprimary, server_id, **kwargs):  # noqa: E501
        """Add an autoprimary  # noqa: E501

        This methods add a new autoprimary server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_autoprimary_with_http_info(autoprimary, server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Autoprimary autoprimary: autoprimary entry to add (required)
        :param str server_id: The id of the server to manage the list of autoprimaries on (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['autoprimary', 'server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_autoprimary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'autoprimary' is set
        if ('autoprimary' not in params or
                params['autoprimary'] is None):
            raise ValueError("Missing the required parameter `autoprimary` when calling `create_autoprimary`")  # noqa: E501
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `create_autoprimary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'autoprimary' in params:
            body_params = params['autoprimary']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/autoprimaries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_autoprimary(self, server_id, ip, nameserver, **kwargs):  # noqa: E501
        """Delete the autoprimary entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_autoprimary(server_id, ip, nameserver, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to delete the autoprimary from (required)
        :param str ip: IP address of autoprimary (required)
        :param str nameserver: DNS name of the autoprimary (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_autoprimary_with_http_info(server_id, ip, nameserver, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_autoprimary_with_http_info(server_id, ip, nameserver, **kwargs)  # noqa: E501
            return data

    def delete_autoprimary_with_http_info(self, server_id, ip, nameserver, **kwargs):  # noqa: E501
        """Delete the autoprimary entry  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_autoprimary_with_http_info(server_id, ip, nameserver, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to delete the autoprimary from (required)
        :param str ip: IP address of autoprimary (required)
        :param str nameserver: DNS name of the autoprimary (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'ip', 'nameserver']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_autoprimary" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `delete_autoprimary`")  # noqa: E501
        # verify the required parameter 'ip' is set
        if ('ip' not in params or
                params['ip'] is None):
            raise ValueError("Missing the required parameter `ip` when calling `delete_autoprimary`")  # noqa: E501
        # verify the required parameter 'nameserver' is set
        if ('nameserver' not in params or
                params['nameserver'] is None):
            raise ValueError("Missing the required parameter `nameserver` when calling `delete_autoprimary`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501
        if 'ip' in params:
            path_params['ip'] = params['ip']  # noqa: E501
        if 'nameserver' in params:
            path_params['nameserver'] = params['nameserver']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/autoprimaries/{ip}/{nameserver}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_autoprimaries(self, server_id, **kwargs):  # noqa: E501
        """Get a list of autoprimaries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_autoprimaries(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to manage the list of autoprimaries on (required)
        :return: Autoprimary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_autoprimaries_with_http_info(server_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_autoprimaries_with_http_info(server_id, **kwargs)  # noqa: E501
            return data

    def get_autoprimaries_with_http_info(self, server_id, **kwargs):  # noqa: E501
        """Get a list of autoprimaries  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_autoprimaries_with_http_info(server_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str server_id: The id of the server to manage the list of autoprimaries on (required)
        :return: Autoprimary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_autoprimaries" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params or
                params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `get_autoprimaries`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader']  # noqa: E501

        return self.api_client.call_api(
            '/servers/{server_id}/autoprimaries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Autoprimary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)