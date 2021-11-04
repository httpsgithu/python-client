# wavefront_api_client.EventApi

All URIs are relative to *https://YOUR_INSTANCE.wavefront.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_event_tag**](EventApi.md#add_event_tag) | **PUT** /api/v2/event/{id}/tag/{tagValue} | Add a tag to a specific event
[**close_user_event**](EventApi.md#close_user_event) | **POST** /api/v2/event/{id}/close | Close a specific event
[**create_event**](EventApi.md#create_event) | **POST** /api/v2/event | Create a specific event
[**delete_user_event**](EventApi.md#delete_user_event) | **DELETE** /api/v2/event/{id} | Delete a specific user event
[**get_alert_event_queries_slug**](EventApi.md#get_alert_event_queries_slug) | **GET** /api/v2/event/{id}/alertQueriesSlug | If the specified event is associated with an alert, returns a slug encoding the queries having to do with that alert firing or resolution
[**get_alert_firing_details**](EventApi.md#get_alert_firing_details) | **GET** /api/v2/event/{id}/alertFiringDetails | Return details of a particular alert firing, including all the series that fired during the referred alert firing
[**get_alert_firing_events**](EventApi.md#get_alert_firing_events) | **GET** /api/v2/event/alertFirings | Get firings events of an alert within a time range
[**get_all_events_with_time_range**](EventApi.md#get_all_events_with_time_range) | **GET** /api/v2/event | List all the events for a customer within a time range
[**get_event**](EventApi.md#get_event) | **GET** /api/v2/event/{id} | Get a specific event
[**get_event_tags**](EventApi.md#get_event_tags) | **GET** /api/v2/event/{id}/tag | Get all tags associated with a specific event
[**get_related_events_with_time_span**](EventApi.md#get_related_events_with_time_span) | **GET** /api/v2/event/{id}/events | List all related events for a specific firing event with a time span of one hour
[**remove_event_tag**](EventApi.md#remove_event_tag) | **DELETE** /api/v2/event/{id}/tag/{tagValue} | Remove a tag from a specific event
[**set_event_tags**](EventApi.md#set_event_tags) | **POST** /api/v2/event/{id}/tag | Set all tags associated with a specific event
[**update_user_event**](EventApi.md#update_user_event) | **PUT** /api/v2/event/{id} | Update a specific user event.


# **add_event_tag**
> ResponseContainer add_event_tag(id, tag_value)

Add a tag to a specific event



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Add a tag to a specific event
    api_response = api_instance.add_event_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->add_event_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_user_event**
> ResponseContainerEvent close_user_event(id)

Close a specific event

This API supports only user events. The API does <strong>not</strong> support close of system events (e.g. alert events).

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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Close a specific event
    api_response = api_instance.close_user_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->close_user_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerEvent**](ResponseContainerEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event**
> ResponseContainerEvent create_event(body=body)

Create a specific event

The following fields are readonly and will be ignored when passed in the request: <code>id</code>, <code>isEphemeral</code>, <code>isUserEvent</code>, <code>runningState</code>, <code>canDelete</code>, <code>canClose</code>, <code>creatorType</code>, <code>createdAt</code>, <code>updatedAt</code>, <code>createdEpochMillis</code>, <code>updatedEpochMillis</code>, <code>updaterId</code>, <code>creatorId</code>, and <code>summarizedEvents</code>

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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
body = wavefront_api_client.Event() # Event | Example Body:  <pre>{   \"name\": \"Event API Example\",   \"annotations\": {     \"severity\": \"info\",     \"type\": \"event type\",     \"details\": \"description\"   },   \"tags\" : [     \"eventTag1\"   ],   \"startTime\": 1490000000000,   \"endTime\": 1490000000001 }</pre> (optional)

try:
    # Create a specific event
    api_response = api_instance.create_event(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Event API Example\&quot;,   \&quot;annotations\&quot;: {     \&quot;severity\&quot;: \&quot;info\&quot;,     \&quot;type\&quot;: \&quot;event type\&quot;,     \&quot;details\&quot;: \&quot;description\&quot;   },   \&quot;tags\&quot; : [     \&quot;eventTag1\&quot;   ],   \&quot;startTime\&quot;: 1490000000000,   \&quot;endTime\&quot;: 1490000000001 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerEvent**](ResponseContainerEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_event**
> ResponseContainerEvent delete_user_event(id)

Delete a specific user event

This API supports only user events. The API does <strong>not</strong> support deletion of system events (e.g. alert events).

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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete a specific user event
    api_response = api_instance.delete_user_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->delete_user_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerEvent**](ResponseContainerEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_event_queries_slug**
> ResponseContainerString get_alert_event_queries_slug(id)

If the specified event is associated with an alert, returns a slug encoding the queries having to do with that alert firing or resolution



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # If the specified event is associated with an alert, returns a slug encoding the queries having to do with that alert firing or resolution
    api_response = api_instance.get_alert_event_queries_slug(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_alert_event_queries_slug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerString**](ResponseContainerString.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_firing_details**
> ResponseContainerSetSourceLabelPair get_alert_firing_details(id)

Return details of a particular alert firing, including all the series that fired during the referred alert firing



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | id of an event of type alert or alert-detail, used to lookup the particular alert firing

try:
    # Return details of a particular alert firing, including all the series that fired during the referred alert firing
    api_response = api_instance.get_alert_firing_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_alert_firing_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id of an event of type alert or alert-detail, used to lookup the particular alert firing | 

### Return type

[**ResponseContainerSetSourceLabelPair**](ResponseContainerSetSourceLabelPair.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_firing_events**
> ResponseContainerPagedEvent get_alert_firing_events(alert_id, earliest_start_time_epoch_millis=earliest_start_time_epoch_millis, latest_start_time_epoch_millis=latest_start_time_epoch_millis, limit=limit, asc=asc)

Get firings events of an alert within a time range



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
alert_id = 'alert_id_example' # str | 
earliest_start_time_epoch_millis = 789 # int |  (optional)
latest_start_time_epoch_millis = 789 # int |  (optional)
limit = 100 # int |  (optional) (default to 100)
asc = true # bool |  (optional)

try:
    # Get firings events of an alert within a time range
    api_response = api_instance.get_alert_firing_events(alert_id, earliest_start_time_epoch_millis=earliest_start_time_epoch_millis, latest_start_time_epoch_millis=latest_start_time_epoch_millis, limit=limit, asc=asc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_alert_firing_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  | 
 **earliest_start_time_epoch_millis** | **int**|  | [optional] 
 **latest_start_time_epoch_millis** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]
 **asc** | **bool**|  | [optional] 

### Return type

[**ResponseContainerPagedEvent**](ResponseContainerPagedEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_events_with_time_range**
> ResponseContainerPagedEvent get_all_events_with_time_range(earliest_start_time_epoch_millis=earliest_start_time_epoch_millis, latest_start_time_epoch_millis=latest_start_time_epoch_millis, cursor=cursor, limit=limit)

List all the events for a customer within a time range



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
earliest_start_time_epoch_millis = 789 # int |  (optional)
latest_start_time_epoch_millis = 789 # int |  (optional)
cursor = 'cursor_example' # str |  (optional)
limit = 100 # int |  (optional) (default to 100)

try:
    # List all the events for a customer within a time range
    api_response = api_instance.get_all_events_with_time_range(earliest_start_time_epoch_millis=earliest_start_time_epoch_millis, latest_start_time_epoch_millis=latest_start_time_epoch_millis, cursor=cursor, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_all_events_with_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earliest_start_time_epoch_millis** | **int**|  | [optional] 
 **latest_start_time_epoch_millis** | **int**|  | [optional] 
 **cursor** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedEvent**](ResponseContainerPagedEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> ResponseContainerEvent get_event(id)

Get a specific event



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get a specific event
    api_response = api_instance.get_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerEvent**](ResponseContainerEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_tags**
> ResponseContainerTagsResponse get_event_tags(id)

Get all tags associated with a specific event



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get all tags associated with a specific event
    api_response = api_instance.get_event_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResponseContainerTagsResponse**](ResponseContainerTagsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_related_events_with_time_span**
> ResponseContainerPagedEvent get_related_events_with_time_span(id, is_overlapped=is_overlapped, rendering_method=rendering_method, limit=limit)

List all related events for a specific firing event with a time span of one hour



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
is_overlapped = true # bool |  (optional)
rendering_method = 'rendering_method_example' # str |  (optional)
limit = 100 # int |  (optional) (default to 100)

try:
    # List all related events for a specific firing event with a time span of one hour
    api_response = api_instance.get_related_events_with_time_span(id, is_overlapped=is_overlapped, rendering_method=rendering_method, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_related_events_with_time_span: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **is_overlapped** | **bool**|  | [optional] 
 **rendering_method** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 100]

### Return type

[**ResponseContainerPagedEvent**](ResponseContainerPagedEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_event_tag**
> ResponseContainer remove_event_tag(id, tag_value)

Remove a tag from a specific event



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
tag_value = 'tag_value_example' # str | 

try:
    # Remove a tag from a specific event
    api_response = api_instance.remove_event_tag(id, tag_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->remove_event_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **tag_value** | **str**|  | 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_event_tags**
> ResponseContainer set_event_tags(id, body=body)

Set all tags associated with a specific event



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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = [wavefront_api_client.list[str]()] # list[str] |  (optional)

try:
    # Set all tags associated with a specific event
    api_response = api_instance.set_event_tags(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->set_event_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **list[str]**|  | [optional] 

### Return type

[**ResponseContainer**](ResponseContainer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_event**
> ResponseContainerEvent update_user_event(id, body=body)

Update a specific user event.

This API supports only user events. The API does <strong>not</strong> support update of system events (e.g. alert events). The following fields are readonly and will be ignored when passed in the request: <code>id</code>, <code>isEphemeral</code>, <code>isUserEvent</code>, <code>runningState</code>, <code>canDelete</code>, <code>canClose</code>, <code>creatorType</code>, <code>createdAt</code>, <code>updatedAt</code>, <code>createdEpochMillis</code>, <code>updatedEpochMillis</code>, <code>updaterId</code>, <code>creatorId</code>, and <code>summarizedEvents</code>

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
api_instance = wavefront_api_client.EventApi(wavefront_api_client.ApiClient(configuration))
id = 'id_example' # str | 
body = wavefront_api_client.Event() # Event | Example Body:  <pre>{   \"name\": \"Event API Example\",   \"annotations\": {     \"severity\": \"info\",     \"type\": \"event type\",     \"details\": \"description\"   },   \"tags\" : [     \"eventTag1\"   ],   \"startTime\": 1490000000000,   \"endTime\": 1490000000001 }</pre> (optional)

try:
    # Update a specific user event.
    api_response = api_instance.update_user_event(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->update_user_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Event**](Event.md)| Example Body:  &lt;pre&gt;{   \&quot;name\&quot;: \&quot;Event API Example\&quot;,   \&quot;annotations\&quot;: {     \&quot;severity\&quot;: \&quot;info\&quot;,     \&quot;type\&quot;: \&quot;event type\&quot;,     \&quot;details\&quot;: \&quot;description\&quot;   },   \&quot;tags\&quot; : [     \&quot;eventTag1\&quot;   ],   \&quot;startTime\&quot;: 1490000000000,   \&quot;endTime\&quot;: 1490000000001 }&lt;/pre&gt; | [optional] 

### Return type

[**ResponseContainerEvent**](ResponseContainerEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

