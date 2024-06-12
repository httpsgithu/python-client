# coding: utf-8

"""
    Wavefront REST API Documentation

    <p>The REST API enables you to interact with the Wavefront service by using standard REST API tools. You can use the REST API to automate commonly executed operations, for example to tag sources automatically.</p><p>When you make REST API calls outside the REST API documentation UI, to authenticate to the service, you must use an API token associated with a user account or a service account. For information on how to get the API token and examples, see <a href=\"http://docs.wavefront.com/using_wavefront_api.html\">Use the Wavefront REST API.</a></p>  # noqa: E501

    OpenAPI spec version: v2
    Contact: chitimba@wavefront.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import wavefront_api_client
from wavefront_api_client.api.event_api import EventApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.event_api.EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_event_tag(self):
        """Test case for add_event_tag

        Add a tag to a specific event  # noqa: E501
        """
        pass

    def test_close_user_event(self):
        """Test case for close_user_event

        Close a specific event  # noqa: E501
        """
        pass

    def test_create_event(self):
        """Test case for create_event

        Create a specific event  # noqa: E501
        """
        pass

    def test_delete_user_event(self):
        """Test case for delete_user_event

        Delete a specific user event  # noqa: E501
        """
        pass

    def test_get_alert_event_queries_slug(self):
        """Test case for get_alert_event_queries_slug

        If the specified event is associated with an alert, returns a slug encoding the queries having to do with that alert firing or resolution  # noqa: E501
        """
        pass

    def test_get_alert_firing_details(self):
        """Test case for get_alert_firing_details

        Return details of a particular alert firing, including all the series that fired during the referred alert firing  # noqa: E501
        """
        pass

    def test_get_alert_firing_events(self):
        """Test case for get_alert_firing_events

        Get firings events of an alert within a time range  # noqa: E501
        """
        pass

    def test_get_all_events_with_time_range(self):
        """Test case for get_all_events_with_time_range

        List all the events for a customer within a time range  # noqa: E501
        """
        pass

    def test_get_event(self):
        """Test case for get_event

        Get a specific event  # noqa: E501
        """
        pass

    def test_get_event_tags(self):
        """Test case for get_event_tags

        Get all tags associated with a specific event  # noqa: E501
        """
        pass

    def test_get_related_events_with_time_span(self):
        """Test case for get_related_events_with_time_span

        List all related events for a specific firing event with a time span of one hour  # noqa: E501
        """
        pass

    def test_remove_event_tag(self):
        """Test case for remove_event_tag

        Remove a tag from a specific event  # noqa: E501
        """
        pass

    def test_set_event_tags(self):
        """Test case for set_event_tags

        Set all tags associated with a specific event  # noqa: E501
        """
        pass

    def test_update_user_event(self):
        """Test case for update_user_event

        Update a specific user event.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
