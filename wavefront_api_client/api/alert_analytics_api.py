# coding: utf-8

"""
    Wavefront REST API Documentation

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


class AlertAnalyticsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_global_alert_analytics(self, start, **kwargs):  # noqa: E501
        """Get Global Alert Analytics for a customer  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_alert_analytics(start, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start: Start time in epoch seconds (required)
        :param int end: End time in epoch seconds
        :return: ResponseContainerGlobalAlertAnalytic
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_alert_analytics_with_http_info(start, **kwargs)  # noqa: E501
        else:
            (data) = self.get_global_alert_analytics_with_http_info(start, **kwargs)  # noqa: E501
            return data

    def get_global_alert_analytics_with_http_info(self, start, **kwargs):  # noqa: E501
        """Get Global Alert Analytics for a customer  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_alert_analytics_with_http_info(start, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int start: Start time in epoch seconds (required)
        :param int end: End time in epoch seconds
        :return: ResponseContainerGlobalAlertAnalytic
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start', 'end']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_alert_analytics" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start' is set
        if self.api_client.client_side_validation and ('start' not in params or
                                                       params['start'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `start` when calling `get_global_alert_analytics`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start' in params:
            query_params.append(('start', params['start']))  # noqa: E501
        if 'end' in params:
            query_params.append(('end', params['end']))  # noqa: E501

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
            '/api/v2/alert/analytics/global', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerGlobalAlertAnalytic',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
