# wavefront_api_client.MonitoredServiceApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update**](MonitoredServiceApi.md#batch_update) | **PUT** /api/v2/monitoredservice/services | Update multiple applications and services in a batch. Batch size is limited to 100.
[**get_all_components**](MonitoredServiceApi.md#get_all_components) | **GET** /api/v2/monitoredservice/components | Get all monitored services with components
[**get_all_services**](MonitoredServiceApi.md#get_all_services) | **GET** /api/v2/monitoredservice | Get all monitored services
[**get_component**](MonitoredServiceApi.md#get_component) | **GET** /api/v2/monitoredservice/{application}/{service}/{component} | Get a specific application
[**get_service**](MonitoredServiceApi.md#get_service) | **GET** /api/v2/monitoredservice/{application}/{service} | Get a specific application
[**get_services_of_application**](MonitoredServiceApi.md#get_services_of_application) | **GET** /api/v2/monitoredservice/{application} | Get a specific application
[**update_service**](MonitoredServiceApi.md#update_service) | **PUT** /api/v2/monitoredservice/{application}/{service} | Update a specific service


# **batch_update**
> ResponseContainer batch_update(body=body)

Update multiple applications and services in a batch. Batch size is limited to 100.



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
body = [wavefront_api_client.MonitoredServiceDTO()] # list[MonitoredServiceDTO] | Example Body:  <pre>[{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" },{   \"satisfiedLatencyMillis\": \"100\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }]</pre> (optional)

try:
    # Update multiple applications and services in a batch. Batch size is limited to 100.
    api_response = api_instance.batch_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->batch_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MonitoredServiceDTO]**](MonitoredServiceDTO.md)| Example Body:  &lt;pre&gt;[{   \&quot;satisfiedLatencyMillis\&quot;: \&quot;100000\&quot;,   \&quot;customDashboardLink\&quot;: \&quot;shopping-dashboard\&quot;,   \&quot;hidden\&quot;: \&quot;false\&quot; },{   \&quot;satisfiedLatencyMillis\&quot;: \&quot;100\&quot;,   \&quot;customDashboardLink\&quot;: \&quot;shopping-dashboard\&quot;,   \&quot;hidden\&quot;: \&quot;false\&quot; }]&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_components**
> ResponseContainerPagedMonitoredServiceDTO get_all_components(offset=offset, limit=limit)

Get all monitored services with components



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all monitored services with components
    api_response = api_instance.get_all_components(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->get_all_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMonitoredServiceDTO**](ResponseContainerPagedMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_services**
> ResponseContainerPagedMonitoredServiceDTO get_all_services(offset=offset, limit=limit)

Get all monitored services



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get all monitored services
    api_response = api_instance.get_all_services(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->get_all_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMonitoredServiceDTO**](ResponseContainerPagedMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component**
> ResponseContainerMonitoredServiceDTO get_component(application, service, component)

Get a specific application



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 
service = 'service_example' # str | 
component = 'component_example' # str | 

try:
    # Get a specific application
    api_response = api_instance.get_component(application, service, component)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->get_component: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **service** | **str**|  | 
 **component** | **str**|  | 

### Return type

[**ResponseContainerMonitoredServiceDTO**](ResponseContainerMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service**
> ResponseContainerMonitoredServiceDTO get_service(application, service)

Get a specific application



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 
service = 'service_example' # str | 

try:
    # Get a specific application
    api_response = api_instance.get_service(application, service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->get_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **service** | **str**|  | 

### Return type

[**ResponseContainerMonitoredServiceDTO**](ResponseContainerMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_of_application**
> ResponseContainerPagedMonitoredServiceDTO get_services_of_application(application, include_component=include_component, offset=offset, limit=limit)

Get a specific application



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 
include_component = false # bool |  (optional) (default to false)
offset = 0 # int |  (optional) (default to 0)
limit = 100 # int |  (optional) (default to 100)

try:
    # Get a specific application
    api_response = api_instance.get_services_of_application(application, include_component=include_component, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->get_services_of_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **include_component** | **bool**|  | [optional] [default to false]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedMonitoredServiceDTO**](ResponseContainerPagedMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service**
> ResponseContainerMonitoredServiceDTO update_service(application, service, body=body)

Update a specific service



### Example
```python
from __future__ import print_function
import time
import wavefront_api_client
from wavefront_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = wavefront_api_client.Configuration()
configuration.api_key['X-AUTH-TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-AUTH-TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = wavefront_api_client.MonitoredServiceApi(wavefront_api_client.ApiClient(configuration))
application = 'application_example' # str | 
service = 'service_example' # str | 
body = wavefront_api_client.MonitoredServiceDTO() # MonitoredServiceDTO | Example Body:  <pre>{   \"satisfiedLatencyMillis\": \"100000\",   \"customDashboardLink\": \"shopping-dashboard\",   \"hidden\": \"false\" }</pre> (optional)

try:
    # Update a specific service
    api_response = api_instance.update_service(application, service, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoredServiceApi->update_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | 
 **service** | **str**|  | 
 **body** | [**MonitoredServiceDTO**](MonitoredServiceDTO.md)| Example Body:  &lt;pre&gt;{   \&quot;satisfiedLatencyMillis\&quot;: \&quot;100000\&quot;,   \&quot;customDashboardLink\&quot;: \&quot;shopping-dashboard\&quot;,   \&quot;hidden\&quot;: \&quot;false\&quot; }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerMonitoredServiceDTO**](ResponseContainerMonitoredServiceDTO.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

