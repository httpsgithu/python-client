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


class QueryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def query_api(self, q, s, g, **kwargs):  # noqa: E501
        """Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity  # noqa: E501

        Long time spans and small granularities can take a long time to calculate  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_api(q, s, g, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: the query expression to execute (required)
        :param str s: the start time of the query window in epoch milliseconds (required)
        :param str g: the granularity of the points returned (required)
        :param str n: name used to identify the query
        :param str query_type: the query type of the query
        :param str e: the end time of the query window in epoch milliseconds (null to use now)
        :param str p: the approximate maximum number of points to return (may not limit number of points exactly)
        :param bool i: whether series with only points that are outside of the query window will be returned (defaults to true)
        :param bool auto_events: whether events for sources included in the query will be automatically returned by the query
        :param str summarization: summarization strategy to use when bucketing points together
        :param bool list_mode: retrieve events more optimally displayed for a list
        :param bool strict: do not return points outside the query window [s;e), defaults to false
        :param str view: view of the query result, metric or histogram, defaults to metric
        :param bool include_obsolete_metrics: include metrics that have not been reporting recently, defaults to false
        :param bool sorted: sorts the output so that returned series are in order, defaults to false
        :param bool cached: whether the query cache is used, defaults to true
        :param list[str] dimension_tuples:
        :param bool use_raw_qk:
        :return: QueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_api_with_http_info(q, s, g, **kwargs)  # noqa: E501
        else:
            (data) = self.query_api_with_http_info(q, s, g, **kwargs)  # noqa: E501
            return data

    def query_api_with_http_info(self, q, s, g, **kwargs):  # noqa: E501
        """Perform a charting query against Wavefront servers that returns the appropriate points in the specified time window and granularity  # noqa: E501

        Long time spans and small granularities can take a long time to calculate  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_api_with_http_info(q, s, g, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str q: the query expression to execute (required)
        :param str s: the start time of the query window in epoch milliseconds (required)
        :param str g: the granularity of the points returned (required)
        :param str n: name used to identify the query
        :param str query_type: the query type of the query
        :param str e: the end time of the query window in epoch milliseconds (null to use now)
        :param str p: the approximate maximum number of points to return (may not limit number of points exactly)
        :param bool i: whether series with only points that are outside of the query window will be returned (defaults to true)
        :param bool auto_events: whether events for sources included in the query will be automatically returned by the query
        :param str summarization: summarization strategy to use when bucketing points together
        :param bool list_mode: retrieve events more optimally displayed for a list
        :param bool strict: do not return points outside the query window [s;e), defaults to false
        :param str view: view of the query result, metric or histogram, defaults to metric
        :param bool include_obsolete_metrics: include metrics that have not been reporting recently, defaults to false
        :param bool sorted: sorts the output so that returned series are in order, defaults to false
        :param bool cached: whether the query cache is used, defaults to true
        :param list[str] dimension_tuples:
        :param bool use_raw_qk:
        :return: QueryResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['q', 's', 'g', 'n', 'query_type', 'e', 'p', 'i', 'auto_events', 'summarization', 'list_mode', 'strict', 'view', 'include_obsolete_metrics', 'sorted', 'cached', 'dimension_tuples', 'use_raw_qk']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_api" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'q' is set
        if self.api_client.client_side_validation and ('q' not in params or
                                                       params['q'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `q` when calling `query_api`")  # noqa: E501
        # verify the required parameter 's' is set
        if self.api_client.client_side_validation and ('s' not in params or
                                                       params['s'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `s` when calling `query_api`")  # noqa: E501
        # verify the required parameter 'g' is set
        if self.api_client.client_side_validation and ('g' not in params or
                                                       params['g'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `g` when calling `query_api`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'n' in params:
            query_params.append(('n', params['n']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501
        if 'query_type' in params:
            query_params.append(('queryType', params['query_type']))  # noqa: E501
        if 's' in params:
            query_params.append(('s', params['s']))  # noqa: E501
        if 'e' in params:
            query_params.append(('e', params['e']))  # noqa: E501
        if 'g' in params:
            query_params.append(('g', params['g']))  # noqa: E501
        if 'p' in params:
            query_params.append(('p', params['p']))  # noqa: E501
        if 'i' in params:
            query_params.append(('i', params['i']))  # noqa: E501
        if 'auto_events' in params:
            query_params.append(('autoEvents', params['auto_events']))  # noqa: E501
        if 'summarization' in params:
            query_params.append(('summarization', params['summarization']))  # noqa: E501
        if 'list_mode' in params:
            query_params.append(('listMode', params['list_mode']))  # noqa: E501
        if 'strict' in params:
            query_params.append(('strict', params['strict']))  # noqa: E501
        if 'view' in params:
            query_params.append(('view', params['view']))  # noqa: E501
        if 'include_obsolete_metrics' in params:
            query_params.append(('includeObsoleteMetrics', params['include_obsolete_metrics']))  # noqa: E501
        if 'sorted' in params:
            query_params.append(('sorted', params['sorted']))  # noqa: E501
        if 'cached' in params:
            query_params.append(('cached', params['cached']))  # noqa: E501
        if 'dimension_tuples' in params:
            query_params.append(('dimensionTuples', params['dimension_tuples']))  # noqa: E501
            collection_formats['dimensionTuples'] = 'multi'  # noqa: E501
        if 'use_raw_qk' in params:
            query_params.append(('useRawQK', params['use_raw_qk']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/x-javascript; charset=UTF-8', 'application/javascript; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/chart/api', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QueryResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_raw(self, metric, **kwargs):  # noqa: E501
        """Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags  # noqa: E501

        An API to check if ingested points are as expected.  Points ingested within a single second are averaged when returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_raw(metric, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: metric to query ingested points for (cannot contain wildcards) (required)
        :param str host: host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used.
        :param str source: source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used.
        :param int start_time: start time in epoch milliseconds (cannot be more than a day in the past) null to use an hour before endTime
        :param int end_time: end time in epoch milliseconds (cannot be more than a day in the past) null to use now
        :return: list[RawTimeseries]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_raw_with_http_info(metric, **kwargs)  # noqa: E501
        else:
            (data) = self.query_raw_with_http_info(metric, **kwargs)  # noqa: E501
            return data

    def query_raw_with_http_info(self, metric, **kwargs):  # noqa: E501
        """Perform a raw data query against Wavefront servers that returns second granularity points grouped by tags  # noqa: E501

        An API to check if ingested points are as expected.  Points ingested within a single second are averaged when returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_raw_with_http_info(metric, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric: metric to query ingested points for (cannot contain wildcards) (required)
        :param str host: host to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used.
        :param str source: source to query ingested points for (cannot contain wildcards). host or source is equivalent, only one should be used.
        :param int start_time: start time in epoch milliseconds (cannot be more than a day in the past) null to use an hour before endTime
        :param int end_time: end time in epoch milliseconds (cannot be more than a day in the past) null to use now
        :return: list[RawTimeseries]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['metric', 'host', 'source', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_raw" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'metric' is set
        if self.api_client.client_side_validation and ('metric' not in params or
                                                       params['metric'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `metric` when calling `query_raw`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'host' in params:
            query_params.append(('host', params['host']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501
        if 'metric' in params:
            query_params.append(('metric', params['metric']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/chart/raw', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RawTimeseries]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
