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


class MonitoredServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def batch_update(self, **kwargs):  # noqa: E501
        """Update multiple applications and services in a batch. Batch size is limited to 100.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_update(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MonitoredServiceDTO] body: Example Body:  <pre>[{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" },{   \"satisfiedLatencyMillis\": \"100\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }]</pre>
        :return: ResponseContainer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.batch_update_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.batch_update_with_http_info(**kwargs)  # noqa: E501
            return data

    def batch_update_with_http_info(self, **kwargs):  # noqa: E501
        """Update multiple applications and services in a batch. Batch size is limited to 100.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.batch_update_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[MonitoredServiceDTO] body: Example Body:  <pre>[{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" },{   \"satisfiedLatencyMillis\": \"100\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }]</pre>
        :return: ResponseContainer
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
                    " to method batch_update" % key
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
            '/api/v2/monitoredservice/services', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_components(self, **kwargs):  # noqa: E501
        """Get all monitored services with components  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_components(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_components_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_components_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_components_with_http_info(self, **kwargs):  # noqa: E501
        """Get all monitored services with components  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_components_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
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
                    " to method get_all_components" % key
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

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/monitoredservice/components', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_services(self, **kwargs):  # noqa: E501
        """Get all monitored services  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_services(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_services_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_services_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_services_with_http_info(self, **kwargs):  # noqa: E501
        """Get all monitored services  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_services_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
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
                    " to method get_all_services" % key
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

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/monitoredservice', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component(self, application, service, component, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component(application, service, component, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :param str component: (required)
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_with_http_info(application, service, component, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_with_http_info(application, service, component, **kwargs)  # noqa: E501
            return data

    def get_component_with_http_info(self, application, service, component, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_with_http_info(application, service, component, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :param str component: (required)
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'service', 'component']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if self.api_client.client_side_validation and ('application' not in params or
                                                       params['application'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `application` when calling `get_component`")  # noqa: E501
        # verify the required parameter 'service' is set
        if self.api_client.client_side_validation and ('service' not in params or
                                                       params['service'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `service` when calling `get_component`")  # noqa: E501
        # verify the required parameter 'component' is set
        if self.api_client.client_side_validation and ('component' not in params or
                                                       params['component'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `component` when calling `get_component`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application' in params:
            path_params['application'] = params['application']  # noqa: E501
        if 'service' in params:
            path_params['service'] = params['service']  # noqa: E501
        if 'component' in params:
            path_params['component'] = params['component']  # noqa: E501

        query_params = []

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
            '/api/v2/monitoredservice/{application}/{service}/{component}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_service(self, application, service, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service(application, service, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_service_with_http_info(application, service, **kwargs)  # noqa: E501
        else:
            (data) = self.get_service_with_http_info(application, service, **kwargs)  # noqa: E501
            return data

    def get_service_with_http_info(self, application, service, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_service_with_http_info(application, service, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'service']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if self.api_client.client_side_validation and ('application' not in params or
                                                       params['application'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `application` when calling `get_service`")  # noqa: E501
        # verify the required parameter 'service' is set
        if self.api_client.client_side_validation and ('service' not in params or
                                                       params['service'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `service` when calling `get_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application' in params:
            path_params['application'] = params['application']  # noqa: E501
        if 'service' in params:
            path_params['service'] = params['service']  # noqa: E501

        query_params = []

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
            '/api/v2/monitoredservice/{application}/{service}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_services_of_application(self, application, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services_of_application(application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param bool include_component:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_services_of_application_with_http_info(application, **kwargs)  # noqa: E501
        else:
            (data) = self.get_services_of_application_with_http_info(application, **kwargs)  # noqa: E501
            return data

    def get_services_of_application_with_http_info(self, application, **kwargs):  # noqa: E501
        """Get a specific application  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_services_of_application_with_http_info(application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param bool include_component:
        :param int offset:
        :param int limit:
        :return: ResponseContainerPagedMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'include_component', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_services_of_application" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if self.api_client.client_side_validation and ('application' not in params or
                                                       params['application'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `application` when calling `get_services_of_application`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application' in params:
            path_params['application'] = params['application']  # noqa: E501

        query_params = []
        if 'include_component' in params:
            query_params.append(('includeComponent', params['include_component']))  # noqa: E501
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

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/monitoredservice/{application}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerPagedMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_service(self, application, service, **kwargs):  # noqa: E501
        """Update a specific service  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service(application, service, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :param MonitoredServiceDTO body: Example Body:  <pre>{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }</pre>
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_service_with_http_info(application, service, **kwargs)  # noqa: E501
        else:
            (data) = self.update_service_with_http_info(application, service, **kwargs)  # noqa: E501
            return data

    def update_service_with_http_info(self, application, service, **kwargs):  # noqa: E501
        """Update a specific service  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_service_with_http_info(application, service, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: (required)
        :param str service: (required)
        :param MonitoredServiceDTO body: Example Body:  <pre>{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }</pre>
        :return: ResponseContainerMonitoredServiceDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'service', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_service" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if self.api_client.client_side_validation and ('application' not in params or
                                                       params['application'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `application` when calling `update_service`")  # noqa: E501
        # verify the required parameter 'service' is set
        if self.api_client.client_side_validation and ('service' not in params or
                                                       params['service'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `service` when calling `update_service`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application' in params:
            path_params['application'] = params['application']  # noqa: E501
        if 'service' in params:
            path_params['service'] = params['service']  # noqa: E501

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
            '/api/v2/monitoredservice/{application}/{service}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseContainerMonitoredServiceDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
