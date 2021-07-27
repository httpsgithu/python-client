# coding: utf-8

"""
    Wavefront REST API

    <p>The Wavefront REST API enables you to interact with Wavefront servers using standard REST API tools. You can use the REST API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make REST API calls outside the Wavefront REST API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wavefront_api_client.api_client import ApiClient


class MetricsPolicyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_metrics_policy(self, **kwargs):  # noqa: E501
        """Get the metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_policy_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_policy_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metrics_policy_with_http_info(self, **kwargs):  # noqa: E501
        """Get the metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics_policy" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/metricspolicy', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMetricsPolicyReadModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metrics_policy_by_version(self, version, **kwargs):  # noqa: E501
        """Get a specific historical version of a metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy_by_version(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int version: (required)
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_policy_by_version_with_http_info(version, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_policy_by_version_with_http_info(version, **kwargs)  # noqa: E501
            return data

    def get_metrics_policy_by_version_with_http_info(self, version, **kwargs):  # noqa: E501
        """Get a specific historical version of a metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy_by_version_with_http_info(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int version: (required)
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics_policy_by_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in params or
                                                       params['version'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `version` when calling `get_metrics_policy_by_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/metricspolicy/history/{version}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMetricsPolicyReadModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_metrics_policy_history(self, **kwargs):  # noqa: E501
        """Get the version history of metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy_history(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_policy_history_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_policy_history_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metrics_policy_history_with_http_info(self, **kwargs):  # noqa: E501
        """Get the version history of metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_policy_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerHistoryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics_policy_history" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/metricspolicy/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerHistoryResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def revert_metrics_policy_by_version(self, version, **kwargs):  # noqa: E501
        """Revert to a specific historical version of a metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revert_metrics_policy_by_version(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int version: (required)
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.revert_metrics_policy_by_version_with_http_info(version, **kwargs)  # noqa: E501
        else:
            (data) = self.revert_metrics_policy_by_version_with_http_info(version, **kwargs)  # noqa: E501
            return data

    def revert_metrics_policy_by_version_with_http_info(self, version, **kwargs):  # noqa: E501
        """Revert to a specific historical version of a metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revert_metrics_policy_by_version_with_http_info(version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int version: (required)
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revert_metrics_policy_by_version" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in params or
                                                       params['version'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `version` when calling `revert_metrics_policy_by_version`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/metricspolicy/revert/{version}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMetricsPolicyReadModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_metrics_policy(self, **kwargs):  # noqa: E501
        """Update the metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metrics_policy(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MetricsPolicyWriteModel body: Example Body:  <pre>{ \"policyRules\": [{   \"name\": \"Policy rule1 name\",   \"description\": \"Policy rule1 description\",   \"prefixes\": [\"revenue.*\"],   \"tags\": [{\"key\":\"sensitive\",  \"value\":\"false\"},              {\"key\":\"source\",  \"value\":\"app1\"}],   \"tagsAnded\": \"true\",   \"accessType\": \"ALLOW\",   \"accounts\": [\"accountId1\", \"accountId2\"],   \"userGroups\": [\"userGroupId1\"],   \"roles\": [\"roleId\"] }, {   \"name\": \"Policy rule2 name\",   \"description\": \"Policy rule2 description\",   \"prefixes\": [\"revenue.*\"],   \"accessType\": \"BLOCK\",   \"accounts\": [\"accountId3\"],   \"userGroups\": [\"userGroupId1\"] }] }</pre>
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_metrics_policy_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_metrics_policy_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_metrics_policy_with_http_info(self, **kwargs):  # noqa: E501
        """Update the metrics policy  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_metrics_policy_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MetricsPolicyWriteModel body: Example Body:  <pre>{ \"policyRules\": [{   \"name\": \"Policy rule1 name\",   \"description\": \"Policy rule1 description\",   \"prefixes\": [\"revenue.*\"],   \"tags\": [{\"key\":\"sensitive\",  \"value\":\"false\"},              {\"key\":\"source\",  \"value\":\"app1\"}],   \"tagsAnded\": \"true\",   \"accessType\": \"ALLOW\",   \"accounts\": [\"accountId1\", \"accountId2\"],   \"userGroups\": [\"userGroupId1\"],   \"roles\": [\"roleId\"] }, {   \"name\": \"Policy rule2 name\",   \"description\": \"Policy rule2 description\",   \"prefixes\": [\"revenue.*\"],   \"accessType\": \"BLOCK\",   \"accounts\": [\"accountId3\"],   \"userGroups\": [\"userGroupId1\"] }] }</pre>
        :return: ResponseContainerMetricsPolicyReadModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_metrics_policy" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/metricspolicy', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMetricsPolicyReadModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
