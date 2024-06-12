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
from wavefront_api_client.api.recent_traces_search_api import RecentTracesSearchApi  # noqa: E501
from wavefront_api_client.rest import ApiException


class TestRecentTracesSearchApi(unittest.TestCase):
    """RecentTracesSearchApi unit test stubs"""

    def setUp(self):
        self.api = wavefront_api_client.api.recent_traces_search_api.RecentTracesSearchApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_recent_traces_search(self):
        """Test case for create_recent_traces_search

        Create a search  # noqa: E501
        """
        pass

    def test_get_all_recent_traces_searches(self):
        """Test case for get_all_recent_traces_searches

        Get all searches for a user  # noqa: E501
        """
        pass

    def test_get_recent_traces_search(self):
        """Test case for get_recent_traces_search

        Get a specific search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
